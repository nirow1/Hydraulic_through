
import numpy as np
import time
import cv2
import os
import re

from Controllers.driver_controller import DriverController
from Qt_files.Qt_python.ui_camera_view import Ui_Form
from Controllers.cam_controller import CamController
from PySide6.QtGui import QIcon, QPixmap, QImage
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from datetime import datetime
from threading import Thread
from pypylon import pylon


class CameraView(QWidget):
    progress_signal = Signal( int, int)
    _orthophoto_done = Signal()
    set_current_action_lbl = Signal(str)

    def __init__(self, drivers):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.drivers: DriverController= drivers

        self.cam: CamController | None= None
        self.cam_2: CamController | None= None
        self._connect_to_cameras()

        self.current_img_1= np.array([])
        self.current_img_2= np.array([])

        self.progress = 0
        self.path = ""
        self.op_quality = 1
        self.quality_dic = {"Vysoká" : 1, "Střední" : 2, "Nízká" : 3}

        self._initial_graphical_changes()
        self._bind_camera_buttons()
        self._bind_emits()

    def _initial_graphical_changes(self):
        self.ui.cam_lbl_1.setPixmap(QPixmap("./App_data/ico.png"))
        self.ui.cam_lbl_1.setScaledContents(True)

        self.ui.cam_lbl_2.setPixmap(QPixmap("./App_data/ico.png"))
        self.ui.cam_lbl_2.setScaledContents(True)

        self.ui.down_btn.setIcon(QIcon("./App_data/down.png"))
        self.ui.up_btn.setIcon(QIcon("./App_data/up.png"))

        self.ui.orthophoto_quality_cb.addItems(["Vysoká", "Střední", "Nízká"])

    def _bind_camera_buttons(self):
        self.ui.cam_1_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cam_1_pg))
        self.ui.cam_2_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cam_2_pg))

        self.ui.up_btn.pressed.connect(lambda: self.drivers.start_jog(True))
        self.ui.up_btn.released.connect(self.stop_moving)

        self.ui.down_btn.pressed.connect(lambda: self.drivers.start_jog(False))
        self.ui.down_btn.released.connect(self.stop_moving)

        self.ui.save_photo_btn.clicked.connect(lambda: self.save_photo(1))
        self.ui.save_photo_btn_2.clicked.connect(lambda: self.save_photo(2))

        self.ui.save_video_btn.clicked.connect(lambda: self.save_video(1))
        self.ui.save_video_btn_2.clicked.connect(lambda: self.save_video(2))

        self.ui.set_pos_btn.clicked.connect(lambda: self.drivers.set_position(int(self.ui.set_pos_le.text())))

        self.ui.reset_camera_connection_btn.clicked.connect(self.connect_clicked)

        self.ui.start_ortophoto_btn.clicked.connect(lambda: self.make_orthophoto_image())

    def _bind_emits(self):
        self.progress_signal.connect(self._update_progressbar)
        self._orthophoto_done.connect(self.orthophoto_ended)
        self.set_current_action_lbl.connect(self._change_action_lbl)

    def connect_clicked(self):
        self._open_camera_connection()

    #todo: odpojit kamery při photogrammetrii
    #todo: je třeba také ošetřit error pokud je jedna z kamer už připojená
    #todo: možná bude stačit jen opět poslet connect na třídě kamery
    def _connect_to_cameras(self):

        self.connecting_cameras = True
        serial_number_1 = "40620956"
        serial_number_2 = "40622574"
        # Enumerate devices
        cam_list = pylon.TlFactory.GetInstance().EnumerateDevices()

        if not cam_list:
            print("No cameras found.")
            return

        # Find devices by serial
        device_1 = next((dev for dev in cam_list if dev.GetSerialNumber() == serial_number_1), None)
        device_2 = next((dev for dev in cam_list if dev.GetSerialNumber() == serial_number_2), None)

        if device_1:
            self.cam = CamController(device_1, 0)
            self.cam.start_capturing()
            time.sleep(1)
            self.cam.set_frame_rate(30)

        if device_2:
            self.cam_2 = CamController(device_2, 1)
            self.cam_2.start_capturing()
            self.cam_2.set_frame_rate(30)

        if self.cam is not None:
            self.cam.CAM_FRAME.connect(lambda image: self._put_image_into_frame(image, 1))
        if self.cam_2 is not None:
            self.cam_2.CAM_FRAME.connect(lambda image: self._put_image_into_frame(image, 2))

        self.connecting_cameras = False

    #todo: toto je nebezpečné pokud kamera již běží a snímá
    def _open_camera_connection(self):
        self.cam.open_connection_and_start_grabbing()
        self.cam_2.open_connection_and_start_grabbing()

    def make_orthophoto_image(self,quality = None, blocking=False):
        self._change_buttons_state(False)
        self.set_current_action_lbl.emit("Pohyb kamer na pozici")
        self.op_quality = quality if quality is not None else self.quality_dic[self.ui.orthophoto_quality_cb.currentText()]

        if blocking:
            self._create_photos()
        else:
            photo_creation_thread = Thread(target=self._create_photos)
            photo_creation_thread.start()

    def _create_photos(self):
        self.drivers.move_to_beginning()
        time.sleep(11)
        self.set_current_action_lbl.emit("Sbírání fotek...")
        self.cam.set_frame_rate(4)

        if self.op_quality == 1:
            photo_number = 122
        elif self.op_quality == 2:
            photo_number = 61
        else:
            photo_number = 20

        for i in range(photo_number):
            self.drivers.move_step(photo_number)

            time.sleep(2)
            cv2.imwrite(f"./App_data/Orthophoto/image_{i}.png", self.current_img_1)
            self.progress_signal.emit(i, photo_number)

        self.cam.set_frame_rate(2)
        self._process_orthophoto_image()

    def save_photo(self, cam_id: int, file="snimek_kamery_"):
        Thread(target=self._save_photo, args=[cam_id, file]).start()

    def _save_photo(self, cam_id: int, file):
        if cam_id == 1:
            current_image = self.current_img_1
        else:
            current_image = self.current_img_2

        name = f"{file}{str(cam_id)}_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        path = f"{self.path}/{name}.png"
        cv2.imwrite(path, current_image)

    def save_video(self, cam_id: int, blocking=False):
        if blocking:
            self._save_video(cam_id)
        else:
            Thread(target=self._save_video, args=[cam_id]).start()

    def _save_video(self, cam_id: int):
        dir_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.set_current_action_lbl.emit("Tvorba videa...")
        os.makedirs(self.path + f"/video_{cam_id}_{dir_time}", exist_ok=True)
        for i in range(90):
            print(i)
            time.sleep(0.5)
            self._save_photo(cam_id, f"video_{cam_id}_{dir_time}/snimek")
            self.progress_signal.emit(i, 90)

    def _process_orthophoto_image(self):
        image_folder = "./App_data/Orthophoto"
        self.set_current_action_lbl.emit("Zpracování fotky...")
        image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(('.png'))], key=self.natural_sort_key)

        strips = []
        for i, img_file in enumerate(image_files[::-1]):
            img_path = os.path.join(image_folder, img_file)
            self.progress_signal.emit(i, len(image_files))
            img = cv2.imread(img_path)

            # Define cropping parameters (adjust height fraction as needed)
            height, width = img.shape[:2]
            self.strip_height = self._get_strip_height()
            cropped_img = img[(height // 2) - (self.strip_height // 2): (height // 2) + (self.strip_height // 2), :]

            strips.append(cropped_img)

        merged_image = np.vstack(strips)

        self._orthophoto_done.emit()

        name = "Orthophoto_" + datetime.now().strftime("%Y-%m-%d_%H_%M")
        cv2.imwrite(f"{self.path}/{name}.png", merged_image)

    def _update_progressbar(self, current: int, total: int):
        if total <= 0:
            percent = 0
        else:
            percent = int((current / (total-1)) * 100)
        percent = max(0, min(100, percent))

        self.ui.orthophoto_pb.setValue(percent)

    def set_path(self, path: str):
        self.path = path

    def orthophoto_ended(self):
        self._change_buttons_state(True)
        self.set_current_action_lbl.emit("Hotovo")
        self.drivers.move_to_beginning()

        folder = "./App_data/Orthophoto"
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):  # only delete files
                os.remove(file_path)

    def _put_image_into_frame(self, image, cam_id):
        height, width, channels = image.shape
        bytes_per_line = channels * width

        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
        q_pixmap = QPixmap.fromImage(q_image)

        if cam_id == 1:
            self.current_img_1 = image
            self.ui.cam_lbl_1.setPixmap(q_pixmap)
        else:
            self.current_img_2 = image
            self.ui.cam_lbl_2.setPixmap(q_pixmap)

    def _get_strip_height(self) -> int:
        toggled = self.ui.objective_chb.isChecked()
        if toggled:
            if self.op_quality == 1:
                strip_height = 88
            elif self.op_quality == 2:
                strip_height = 176
            else:
                strip_height = 800
        else:
            if self.op_quality == 1:
                strip_height = 44
            elif self.op_quality == 2:
                strip_height = 96
            else:
                strip_height= 285
        return strip_height

    def _change_action_lbl(self, lbl):
        self.ui.currnet_action_lbl.setText(lbl)

    def stop_moving(self):
        self.drivers.stop_jog()

    def _change_buttons_state(self, state):
        self.ui.start_ortophoto_btn.setEnabled(state)
        self.ui.up_btn.setEnabled(state)
        self.ui.down_btn.setEnabled(state)
        self.ui.set_pos_btn.setEnabled(state)

    def disconnect(self):
        if self.cam:
            self.cam.disconnect()
        if self.cam_2:
            self.cam_2.disconnect()

    @staticmethod
    def natural_sort_key(filename):
        return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', filename)]
