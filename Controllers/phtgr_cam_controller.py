import time
from threading import Thread
from typing import List

from Controllers.cam_controller import CamController
from PySide6.QtCore import QObject
from pypylon import pylon


class PhtgrCamController(QObject):
    def __init__(self):
        super().__init__()
        self.cam_list: List[CamController] = []
        self._initialize_cameras()

    def _initialize_cameras(self):
        cam_list = pylon.TlFactory.GetInstance().EnumerateDevices()
        cam_list = sorted(cam_list, key=lambda camera: camera.GetFriendlyName())

        for cam_id, camera in enumerate(cam_list):
            if cam_id < 5 and camera.GetSerialNumber() != "40620956":
                cam = CamController(camera, cam_id)
                self.cam_list.append(cam)

    def acquire_frames(self, count):
        thread = Thread(target=self._acquire_frames, args=[count])
        thread.start()

    def _acquire_frames(self, count):
        for cam in self.cam_list:
            time.sleep(2.5)
            cam.grab_frame(count)

    def set_path(self, path):
        for cam in self.cam_list:
            cam.set_path(path)

    def start_recording(self):
        for cam in self.cam_list:
            cam.start_capturing()

    def stop_recording(self):
        for cam in self.cam_list:
            cam.disconnect()