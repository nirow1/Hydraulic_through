import math
from datetime import datetime

import numpy as np
import time
import cv2
import os
import re

from PySide6.QtGui import QIcon, QPixmap, QImage
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from threading import Thread
from pypylon import pylon

from Controllers.driver_controller import DriverController
from Qt_files.Qt_python.ui_camera_view import Ui_Form
from Controllers.cam_controller import CamController


class CameraView(QWidget):
    progress_signal = Signal(int)
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
        self.strip_height = 88

        self._initial_graphical_changes()
        self._bind_camera_buttons()
        self._bind_emits()

    #todo: přidat indikaci dělaání videa
    #todo: přidat kvalitu orthophoto a s tím propočítat velikost pásu
    def _initial_graphical_changes(self):
        self.ui.cam_lbl_1.setPixmap(QPixmap("./App_data/ico.png"))
        self.ui.cam_lbl_1.setScaledContents(True)

        self.ui.cam_lbl_2.setPixmap(QPixmap("./App_data/ico.png"))
        self.ui.cam_lbl_2.setScaledContents(True)

        self.ui.left_btn.setIcon(QIcon("./App_data/down.png"))
        self.ui.right_btn.setIcon(QIcon("./App_data/up.png"))

        self.ui.orthophoto_quality_cb.addItem("Vysoká")
        self.ui.orthophoto_quality_cb.addItem("Střední")
        self.ui.orthophoto_quality_cb.addItem("Nízká")

    def _bind_camera_buttons(self):
        self.ui.cam_1_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cam_1_pg))
        self.ui.cam_2_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cam_2_pg))

        self.ui.left_btn.pressed.connect(lambda: self.drivers.start_jog(True))
        self.ui.left_btn.released.connect(self.stop_moving)

        self.ui.right_btn.pressed.connect(lambda: self.drivers.start_jog(False))
        self.ui.right_btn.released.connect(self.stop_moving)

        self.ui.save_photo_btn.clicked.connect(lambda: self.save_photo(1))
        self.ui.save_photo_btn_2.clicked.connect(lambda: self.save_photo(2))

        self.ui.save_video_btn.clicked.connect(lambda: self.save_video(1))
        self.ui.save_video_btn_2.clicked.connect(lambda: self.save_video(2))

        self.ui.objective_chb.stateChanged.connect(self._changed_objective)

        self.ui.set_pos_btn.clicked.connect(lambda: self.drivers.set_position(int(self.ui.set_pos_le.text())))

        self.ui.reset_camera_connection_btn.clicked.connect(self.connect_clicked)

        self.ui.start_ortophoto_btn.clicked.connect(self.make_orthophoto_image)

    def _bind_emits(self):
        self.progress_signal.connect(self._update_progressbar)
        self._orthophoto_done.connect(self._orthophoto_done)
        self.set_current_action_lbl.connect(self._change_action_lbl)

    def connect_clicked(self):
        if not self.connecting_cameras:
            self._connect_to_cameras()

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

        if device_2:
            self.cam_2 = CamController(device_2, 1)
            self.cam_2.start_capturing()

        if self.cam is not None:
            self.cam.CAM_FRAME.connect(lambda image: self._put_image_into_frame(image, 1))
        if self.cam_2 is not None:
            self.cam_2.CAM_FRAME.connect(lambda image: self._put_image_into_frame(image, 2))

        self.connecting_cameras = False

    def make_orthophoto_image(self, blocking=False):
        self._change_buttons_state(False)
        self.set_current_action_lbl.emit("Pohyb kamer na pozici")

        if blocking:
            self._create_photos()
        else:
            photo_creation_thread = Thread(target=self._process_orthophoto_image)#self._create_photos)
            photo_creation_thread.start()

    def _create_photos(self):
        self.drivers.move_to_beginning()
        time.sleep(11)
        self.set_current_action_lbl.emit("Sbírání fotek...")
        self.cam.set_frame_rate(4)
        for i in range(124):
            self.drivers.move_step()
            time.sleep(2)
            cv2.imwrite(f"./App_data/Orthophoto/image_{i}.png", self.current_img_1)
            self.progress_signal.emit(i)

        self.drivers.move_to_beginning()
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
        os.makedirs(self.path + f"/video_{cam_id}_{dir_time}", exist_ok=True)
        for i in range(90):
            print(i)
            time.sleep(0.5)
            self._save_photo(cam_id, f"video_{cam_id}_{dir_time}/snimek")

    def _process_orthophoto_image(self):
        image_folder = "./App_data/Orthophoto"
        self.set_current_action_lbl.emit("Zpracování fotky...")
        image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(('.png'))], key=self.natural_sort_key)

        strips = []
        for i, img_file in enumerate(image_files[::-1]):
            img_path = os.path.join(image_folder, img_file)
            self.progress_signal.emit(i)
            img = cv2.imread(img_path)

            # Define cropping parameters (adjust height fraction as needed)
            height, width = img.shape[:2]
            self.strip_height = 44 # 88 for 12x camera
            cropped_img = img[(height // 2) - (self.strip_height // 2): (height // 2) + (self.strip_height // 2), :]

            strips.append(cropped_img)

        merged_image = np.vstack(strips)

        self._orthophoto_done.emit()

        name = "Orthophoto_" + datetime.now().strftime("%Y-%m-%d_%H_%M")
        cv2.imwrite(f"{self.path}/{name}.png", merged_image)

    def _update_progressbar(self, value):
        self.ui.orthophoto_pb.setValue(math.ceil(value / 1.25))

    def set_path(self, path: str):
        self.path = path

    def orthophoto_ended(self):
        self._change_buttons_state(True)
        self.set_current_action_lbl.emit("Hotovo")

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

    def _changed_objective(self):
        if self.ui.objective_chb.toggled:
            self.strip_height = 88
        else:
            self.strip_height = 44

    def _change_action_lbl(self, lbl):
        self.ui.currnet_action_lbl.setText(lbl)

    def stop_moving(self):
        self.drivers.stop_jog()

    def _change_buttons_state(self, state):
        self.ui.start_ortophoto_btn.setEnabled(state)
        self.ui.left_btn.setEnabled(state)
        self.ui.right_btn.setEnabled(state)
        self.ui.set_pos_btn.setEnabled(state)

    def disconnect(self):
        if self.cam:
            self.cam.disconnect()
        if self.cam_2:
            self.cam_2.disconnect()

    @staticmethod
    def natural_sort_key(filename):
        return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', filename)]
