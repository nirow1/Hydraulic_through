import numpy
import cv2

from PySide6.QtCore import QObject, Signal
from threading import Thread
from pypylon import pylon


class CamController(QObject):
    CAM_FRAME = Signal(numpy.ndarray)
    FRAME_SAVED = Signal(int)

    def __init__(self, cam, cam_id):
        super().__init__()
        self.camera: pylon.InstantCamera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateDevice(cam))
        self.cam_id = cam_id
        self.camera.Open()
        self.set_frame_rate(2)
        self.camera.AcquisitionFrameRateEnable.SetValue(True)
        self.save_path = "./App_data"

    def start_capturing(self):
        thread = Thread(target=self._camera_capture)
        thread.start()

    def _camera_capture(self):
        try:
            self.camera.StartGrabbing(1)
            self.set_frame_rate(3)

            while self.camera.IsGrabbing():
                grab_result = self.camera.RetrieveResult(2000, pylon.TimeoutHandling_ThrowException)

                if grab_result.GrabSucceeded():
                    image_array = grab_result.Array
                    rgb_image_array = cv2.cvtColor(image_array, cv2.COLOR_BayerRG2RGB)
                    self.CAM_FRAME.emit(rgb_image_array)

                grab_result.Release()

        except Exception as e:
            print(f"cam {self.cam_id}: {e}")

    def grab_frame(self, count: int):
        thread = Thread(target=self._grab_frame, args=[count])
        thread.start()

    def _grab_frame(self, count):
        try:
            self.camera.StartGrabbing(pylon.GrabStrategy_OneByOne)
            image = pylon.PylonImage()

            while self.camera.IsGrabbing():
                grab_result = self.camera.RetrieveResult(2000, pylon.TimeoutHandling_Return)
                if grab_result.GrabSucceeded():
                    image.AttachGrabResultBuffer(grab_result)
                    filename = f"{self.save_path}/cam_{self.cam_id}_{str(count)}.png"
                    image.Save(pylon.ImageFileFormat_Png, filename)
                    self.FRAME_SAVED.emit(self.cam_id)
                    print(f"{self.cam_id} emited")
                    grab_result.Release()
                    break
                else:
                    grab_result.Release()

            self.camera.StopGrabbing()
        except Exception as e:
            print(f"cam {self.cam_id}: {e}")

    def set_path(self, path):
        self.save_path = path

    def set_frame_rate(self, val: float):
        self.camera.AcquisitionFrameRate.SetValue(val)

    def set_exposure(self, val: float):
        self.camera.ExposureTime.SetValue(val)

    def open_connection_and_start_grabbing(self):
        self.camera.Open()
        self.start_capturing()

    def set_gain(self, val: float):
        self.camera.Gain.SetValue(val)

    def disconnect(self):
        self.camera.Close()


if __name__ == '__main__':
    cam_list = pylon.TlFactory.GetInstance().EnumerateDevices()
    cam_list = sorted(cam_list, key=lambda camera: camera.GetFriendlyName())

    for id, camera in enumerate(cam_list):
        test_cam = CamController(camera, id)
        test_cam.grab_frame(1)