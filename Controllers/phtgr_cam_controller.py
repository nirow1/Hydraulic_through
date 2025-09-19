import time
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
        Thread(target=self._initialize_cameras).start()

    def _bind_emits(self):
        if len(self.cam_list) != 0:
            self.cam_list[0].FRAME_SAVED.connect(self._change_cam_status)
            self.cam_list[1].FRAME_SAVED.connect(self._change_cam_status)
            self.cam_list[2].FRAME_SAVED.connect(self._change_cam_status)
            self.cam_list[3].FRAME_SAVED.connect(self._change_cam_status)

    def _initialize_cameras(self):
        cam_list = pylon.TlFactory.GetInstance().EnumerateDevices()
        cam_list = sorted(cam_list, key=lambda camera: camera.GetFriendlyName())
        count = 0

        for camera in cam_list:
            try:
                cam = CamController(camera, count)
                count += 1
                self.cam_list.append(cam)
            except Exception as e:
                print(e)

        self._bind_emits()

    def acquire_frames(self, count):
        thread = Thread(target=self._acquire_frames, args=[count])
        thread.start()

    def _acquire_frames(self, count):
        self.cams_ready = [False, False, False, False]
        for cam in self.cam_list:
            cam.grab_frame(count)
            time.sleep(1.0)
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