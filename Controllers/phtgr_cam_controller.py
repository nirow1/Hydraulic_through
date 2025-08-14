import time
from functools import partial
from threading import Thread
from typing import List

from Controllers.cam_controller import CamController
from PySide6.QtCore import QObject, Signal
from pypylon import pylon


class PhtgrCamController(QObject):
    CAMS_READY = Signal()

    def __init__(self):
        super().__init__()
        self.cam_list: List[CamController] = []
        self.cams_ready = [True, True, True, True]
        self._initialize_cameras()

    def bind_emits(self):
        for cam in self.cam_list:
            cam.FRAME_SAVED.connect(partial(self._change_cam_status, cam.cam_id))

    def _initialize_cameras(self):
        cam_list = pylon.TlFactory.GetInstance().EnumerateDevices()
        cam_list = sorted(cam_list, key=lambda camera: camera.GetFriendlyName())
        count = 0

        for camera in cam_list:
            if camera.GetSerialNumber() != "40620956":
                cam = CamController(camera, count)
                count += 1
                self.cam_list.append(cam)

    def acquire_frames(self, count):
        thread = Thread(target=self._acquire_frames, args=[count])
        thread.start()

    def _acquire_frames(self, count):
        self.cams_ready = [False, False, False, False]
        for cam in self.cam_list:
            cam.grab_frame(count)
        while not all(self.cams_ready):
            time.sleep(.05)
        self.CAMS_READY.emit()

    def _change_cam_status(self, cam_id):
        self.cams_ready[cam_id] = True

    def set_path(self, path):
        for cam in self.cam_list:
            cam.set_path(path)

    def start_recording(self):
        for cam in self.cam_list:
            cam.start_capturing()

    def stop_recording(self):
        for cam in self.cam_list:
            cam.disconnect()