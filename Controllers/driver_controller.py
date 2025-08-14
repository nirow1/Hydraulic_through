import time
from threading import Thread

from pymodbus.client import ModbusTcpClient as ModbusClient
from PySide6.QtCore import QThread, Signal
from time import sleep


class DriverController(QThread):
    STEP_EXECUTED_PG = Signal(int)

    def __init__(self):
        super().__init__()
        self.ip = "192.168.1.9"
        self.port = 502
        self.client: ModbusClient | None = None
        self.connected: bool= False
        self.stop_jog_cycle: bool= False
        self.move_to_beginning()
        self.step_number = 0

    def run(self):
        self._connect_to_drivers()

    def _connect_to_drivers(self):
        while not self.connected:
            try:
                self.client = ModbusClient(self.ip, port=self.port)
                self.connected = self.client.connect()
                print(f"connection status Logo: {self.connected}")
                if self.connected:
                    self._enable_drivers()
                else:
                    sleep(5)
            except Exception as e:
                print(e)

    def _enable_drivers(self):
        if self.connected:
            slave = [1]
            for i in slave:
                self.client.write_register(15, 1)

    def set_position(self, pos: int, slave: int = 1):
        if self.connected:
            pos = pos * 512
            disassembled_int = [(pos >> 16) & 0xFFFF, pos & 0xFFFF]

            self.client.write_registers(0x6249, disassembled_int, slave=slave)
            self.client.write_registers(24578, [25], slave=slave)

    def _send_step_command(self):
        if self.connected:
            self.client.write_registers(24578, [17])

    def move_step(self, photogrammetry: bool):
        thread = Thread(target=self._move_step, args=[photogrammetry])
        thread.start()

    def _move_step(self, pg):
        self._send_step_command()
        time.sleep(.5)

        self.step_number += 1
        if self.step_number == 124:
            self.step_number = 0
            self.move_to_beginning()

    def start_jog(self, left: bool):
        if self.connected:
            if left:
                jog_thread = Thread(target=self._jog_to_side, args=[0x4001])
            else:
                jog_thread = Thread(target=self._jog_to_side, args=[0x4002])
            jog_thread.start()

    def _jog_to_side(self, side: int, slave: int=1):
        while not self.stop_jog_cycle:
            self.client.write_register(6145, side, slave=slave)
            time.sleep(0.2)
        self.stop_jog_cycle = False

    def stop_jog(self):
        if self.connected:
            self.stop_jog_cycle = True
            self.client.write_register(6146, 1, slave=1)

    def move_to_beginning(self):
        if self.connected:
            self.client.write_registers(24578, [20])


if __name__ == '__main__':
    driver = DriverController()
    driver.run()


