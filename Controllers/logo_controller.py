import struct
from threading import Lock

from PySide6.QtCore import QThread, Signal
from snap7.logo import Logo
from time import sleep


class LogoController(QThread):
    LOGO_DATA = Signal(float)
    CONNECTION_LOSS = Signal(bool)

    def __init__(self, ip :str="192.168.1.3"):
        super().__init__()
        self.ip = ip
        self.port = 502
        self.connected = False

        self.lock = Lock()

    def run(self):
        self._connect_to_logo()

    def _connect_to_logo(self):
        while not self.connected:
            try:
                self.logo = Logo()
                self.logo.connect(self.ip, 768, self.port)
                self.connected = self.logo.get_connected()
                self.write_logo_byte(0, bytearray(b'\x05'))
                self._get_logo_data()
                break
            except Exception as e:
                print(e)
                sleep(10)

    def _get_logo_data(self):
        while self.connected:
            with self.lock:
                flow = self.logo.db_read(0, 3, 2)
                int_flow = struct.unpack('>H', flow)

            self.LOGO_DATA.emit(int_flow[0]/10)
            sleep(1)

    def write_logo_ushort(self, pos: int, request: int):
        if not self.connected:
            return

        with self.lock:
            try:
                ushort_in_bytes = struct.pack('>H', request)
                print(f"{request}")
                #self.logo.db_write(0, pos, bytearray(ushort_in_bytes))
            except Exception as e:
                print(f"[ERROR] write_logo_ushort: {e}")

    def read_logo_bytes(self, pos: int, size: int):
        if not self.connected:
            return

        with self.lock:
            msg = self.logo.db_read(0, pos, size)
            print(struct.unpack('>H', msg))

    def write_logo_byte(self, pos: int, logo_bytes: bytearray):
        if not self.connected:
            return

        with self.lock:
            try:
                self.logo.db_write(0, pos, logo_bytes)
            except Exception as e:
                print(f"[ERROR] write_logo_ushort: {e}")


    def disconnect(self):
        try:
            self.connected = False
            self.logo.db_write(0, 10, bytearray(b'\x00\x00'))
            sleep(0.2)
            self.logo.disconnect()
            self.quit()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    logo = LogoController("192.168.1.3")
    logo.run()