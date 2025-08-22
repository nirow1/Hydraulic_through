import os
import csv
import time
from threading import Thread

from Controllers.phtgr_cam_controller import PhtgrCamController
from Qt_files.Qt_python.ui_Photogrammetry_view import Ui_Form
from Controllers.driver_controller import DriverController
from Utils.csv_work import change_csv_status
from PySide6.QtWidgets import QWidget


class PhotogrammetryView(QWidget):
    def __init__(self, drivers):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.drivers: DriverController = drivers
        self.cameras: PhtgrCamController = PhtgrCamController()

        # variables
        self.current_working_id = 0
        self.path: str = ""
        self.cams_ready = False

        self._initial_graphical_changes()
        self._bind_buttons()
        self._bind_emits()

    def _initial_graphical_changes(self):
        pass

    def _bind_buttons(self):
        self.ui.start_new_phtgrm_btn.clicked.connect(self.start_photogrammetry)

    def _bind_emits(self):
        self.cameras.CAMS_READY.connect(lambda: self._change_cams_state(True))

    def _change_cams_state(self, state: bool):
        self.cams_ready = state

    def start_photogrammetry(self, blocking=False):
        if blocking:
            self._create_directory()
            self._create_photogrammetry_photos()
        else:
            self._create_directory()
            Thread(target=self._create_photogrammetry_photos).start()

    def _create_directory(self):
        path = f"./App_data/Photogrammetry/Photogrammetry_{self.current_working_id}"
        os.makedirs(path, exist_ok=True)

    def _create_photogrammetry_photos(self):
        self.drivers.move_to_beginning()
        time.sleep(11)
        for i in range(124):
            print(f"foto:{i}")
            self._change_cams_state(False)
            self.cameras.acquire_frames(i)
            while not self.cams_ready:
                time.sleep(0.05)
            self.drivers.move_step()
        change_csv_status("./App_data/Test_plan/photogrammetry.csv", self.current_working_id, 1)

    def _create_photogrammetry_record(self):
        file_path = "./App_data/Test_plan/photogrammetry.csv"

        with open(file_path, mode="r+", newline="") as f:
            reader = list(csv.reader(f))
            records = reader[1:]

            # Extract existing IDs
            existing_ids = [int(row[0]) for row in records if len(row) != 0]

            # Find the smallest missing ID
            last_id = 1
            while last_id in existing_ids:
                last_id += 1

            empty_row_index = next((i for i, row in enumerate(records) if not row or all(cell == '' for cell in row)),
                                   None)

            new_row = [str(last_id), 0, 0, 0]

            if empty_row_index is not None:
                records[empty_row_index] = new_row  # Fill the first empty row
            else:
                records.append(new_row)  # No empty rows, append at the end

            # Rewrite the file with updated data
            f.seek(0)
            writer = csv.writer(f)
            writer.writerow(reader[0])  # Write headers back
            writer.writerows(records)
            f.truncate()  # Ensure old data is removed

        return last_id

    def set_path(self, path):
        self.path = path
