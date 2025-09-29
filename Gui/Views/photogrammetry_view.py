import Metashape
import time
import csv
import os

from Controllers.phtgr_cam_controller import PhtgrCamController
from Utils.ui_workers import populate_table, update_progressbar
from Qt_files.Qt_python.ui_Photogrammetry_view import Ui_Form
from Controllers.driver_controller import DriverController
from Utils.csv_work import extract_data_from_csv
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from threading import Thread


class PhotogrammetryView(QWidget):
    PHTGR_RUNNING = Signal(bool)
    CAMS_WORKING = Signal(bool)

    # calss signals
    aligning_photos = Signal()
    creating_point_cloud = Signal()
    creating_model = Signal()
    building_texture = Signal()
    progress_signal = Signal(object, int, int)

    def __init__(self, drivers):

        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.drivers: DriverController = drivers
        self.cameras: PhtgrCamController = PhtgrCamController()

        # variables
        self.current_project_id = 0
        self.result_path: str = ""
        self.cams_ready = False
        self.doc = Metashape.Document()
        self.chunk = self.doc.addChunk()
        self.quality = None

        self.photo_align_settings = {"downscale": 0, "keypoint": 0, "tiepoint": 0}
        self.point_cloud_setting = {"downscale": 0, "filter": 0}
        self.texture_settings = {"blending": 0, "size": 0}
        self.mesh_face_count = 0

        self._update_photogrammetry_table()
        self._initial_graphical_changes()
        self._bind_buttons()
        self._bind_emits()

    def _initial_graphical_changes(self):
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.widget_28.setVisible(False)
        self.ui.photogrammetry_running_lbl.setVisible(False)

    #todo: přidat přehled o časové náročnosti
    #todo: pridat chb na mazání filů po skončení phtotogrammetrie
    #todo: poprvé se kamery nepohnou
    #todo: přidat popisky k aktuálnímu stavu kamer a nastavit vzhled progressbaru
    def _bind_buttons(self):
        self.ui.start_new_phtgrm_btn.clicked.connect(lambda: self.start_photogrammetry())

    def _bind_emits(self):
        self.cameras.CAMS_READY.connect(lambda: self._change_cams_state(True))
        self.aligning_photos.connect(lambda: self.ui.progress_lbl.setText("Aligning photos"))
        self.creating_point_cloud.connect(lambda: self.ui.progress_lbl.setText("Creating point could"))
        self.creating_model.connect(lambda: self.ui.progress_lbl.setText("Creating model"))
        self.building_texture.connect(lambda: self.ui.progress_lbl.setText("Building texture"))
        self.progress_signal.connect(update_progressbar)

    def _change_cams_state(self, state: bool):
        self.cams_ready = state

    #todo: možnost vypnout photogrammetrii
    def start_photogrammetry(self,quality=None, blocking=False):
        self._create_directory()
        self._photogrammetry_running(True)
        self._update_photogrammetry_table()
        self.quality = quality
        self._set_quality(quality)

        if blocking:
            self._create_photogrammetry_photos()
            Thread(target=self._create_photogrammetry_model).start()
        else:
            Thread(target=self._start_photogrammetry_process).start()

    def _create_directory(self):
        self._create_photogrammetry_record()
        path = f"./App_data/Photogrammetry/Photogrammetry_{self.current_project_id}/Photos"
        os.makedirs(path, exist_ok=True)

    def _start_photogrammetry_process(self):
        self._create_photogrammetry_photos()
        self._create_photogrammetry_model()

    def _create_photogrammetry_photos(self):
        self.change_button_states(False)
        self.drivers.move_to_beginning()
        self.CAMS_WORKING.emit(True)
        self.cameras.set_path(f"./App_data/Photogrammetry/Photogrammetry_{self.current_project_id}/Photos")
        time.sleep(12)
        for i in range(80):
            print(f"foto:{i}")
            self._change_cams_state(False)
            self.cameras.acquire_frames(i)
            while not self.cams_ready:
                time.sleep(0.05)
            self.drivers.move_step(80)
            self.progress_signal.emit(self.ui.progressBar, i, 80)

        self.CAMS_WORKING.emit(False)
        self.change_button_states(True)

    def _create_photogrammetry_model(self):
        result_folder_path = f"./App_data/Photogrammetry/Photogrammetry_{self.current_project_id}"
        self._align_photos(result_folder_path)
        self._create_point_cloud(result_folder_path)
        self._create_model(result_folder_path)
        if self.quality is None and self.ui.texture_chb.isChecked():
            self.build_texture(result_folder_path)
        self.export_results()
        self.doc.remove(self.chunk)
        self._photogrammetry_running(False)
        self.chunk = None

    def _align_photos(self, result_folder_path):
        self.aligning_photos.emit()
        photo_folder_path = result_folder_path+"/photos"
        photos = [os.path.join(photo_folder_path, p) for p in os.listdir(photo_folder_path) if p.endswith(".png")]
        self.chunk.addPhotos(photos)

        self.chunk.matchPhotos(downscale=self.photo_align_settings["downscale"],
                               keypoint_limit=self.photo_align_settings["keypoint"],
                               tiepoint_limit=self.photo_align_settings["tiepoint"],
                               progress=self.progress_callback)
        self.chunk.alignCameras()
        self.doc.save(os.path.join(result_folder_path, "project_after_alignment.psx"))

    def _create_point_cloud(self, result_file_path):
        self.creating_point_cloud.emit()
        self.chunk.buildDepthMaps(downscale=2, filter_mode=Metashape.MildFiltering)
        self.chunk.buildPointCloud(progress=self.progress_callback)
        self.doc.save(os.path.join(result_file_path, "project_after_pointcloud.psx"))

    def _create_model(self, result_folder_path):
        self.creating_model.emit()
        self.chunk.buildModel(surface_type=Metashape.Arbitrary,
                              interpolation=Metashape.EnabledInterpolation,
                              face_count=Metashape.MediumFaceCount,
                              progress=self.progress_callback)
        self.doc.save(os.path.join(result_folder_path, "project_after_model.psx"))

    def build_texture(self, result_folder_path):
        self.building_texture.emit()
        self.chunk.buildUV(mapping_mode=Metashape.GenericMapping)
        self.chunk.buildTexture(blending_mode=Metashape.MosaicBlending,
                                texture_size=4096,
                                progress=self.progress_callback)
        self.doc.save(os.path.join(result_folder_path, "project_after_texture.psx"))

    def export_results(self):
        os.makedirs(self.result_path, exist_ok=True)

        # Export to STL
        self.chunk.exportModel(
            path=os.path.join(self.result_path, "model.stl"),
            binary=True,  # True = binary STL (smaller file size), False = ASCII STL
            format=Metashape.ModelFormatSTL
        )

    def progress_callback(self, info):
        self.progress_signal.emit(self.ui.progressBar, info, 80000)

    def _create_photogrammetry_record(self):
        file_path = "./App_data/Test_plan/planned_photogrammetry.csv"

        with open(file_path, mode="r+", newline="") as f:
            reader = list(csv.reader(f))
            records = reader

            # Extract existing IDs
            existing_ids = [int(row[0]) for row in records if len(row) != 0]

            # Find the smallest missing ID
            last_id = 1
            while last_id in existing_ids:
                last_id += 1

            empty_row_index = next((i for i, row in enumerate(records) if not row or all(cell == '' for cell in row)), None)

            new_row = [str(last_id), 0, 0, 0, 0]

            if empty_row_index is not None:
                records[empty_row_index] = new_row  # Fill the first empty row
            else:
                records.append(new_row)  # No empty rows, append at the end

            # Rewrite the file with updated data
            f.seek(0)
            writer = csv.writer(f)
            writer.writerows(records)
            f.truncate()  # Ensure old data is removed

            self.current_project_id = last_id

    def _set_quality(self, quality=None):
        if quality == 1:  # High
            self._set_alignment_settings(1, 80000, 20000)
            self._set_point_cloud_settings(1, "Bez filtru")
            self._set_model_settings("Vysoký")
        elif quality == 2:  # Medium
            self._set_alignment_settings(2, 40000, 10000)
            self._set_point_cloud_settings(2, "Střední filtr")
            self._set_model_settings("Střední")
        elif quality == 3:  # Low
            self._set_alignment_settings(4, 20000, 2000)
            self._set_point_cloud_settings(4, "Střední filtr")
            self._set_model_settings("Nízký")
        else:  # Custom from UI
            self._set_alignment_settings(
                int(self.ui.alignment_downscale_cb.currentText()),
                int(self.ui.keypoint_le.text()),
                int(self.ui.tiepoint_le.text())
            )
            self._set_point_cloud_settings(
                int(self.ui.cloud_downscale_cb.currentText()),
                self.ui.filter_cb.currentText()
            )
            self._set_model_settings(self.ui.face_count_cb.currentText())
            if self.ui.texture_chb.isChecked():
                self._set_texture_settings()

    def _set_alignment_settings(self, downscale, keypoint, tiepoint):
        self.photo_align_settings["downscale"] = downscale
        self.photo_align_settings["keypoint"] = keypoint
        self.photo_align_settings["tiepoint"] = tiepoint

    def _set_point_cloud_settings(self, downscale, filter: str):
        self.point_cloud_setting["downscale"] = downscale
        if filter == "Bez filtru":
            self.point_cloud_setting["filter"] = Metashape.NoFiltering
        elif filter == "Střední filtr":
            self.point_cloud_setting["filter"] = Metashape.MildFiltering
        elif filter == "Agresivní filtr":
            self.point_cloud_setting["filter"] = Metashape.AggressiveFiltering

    def _set_model_settings(self, face_count: str):
        if face_count == "Vysoký":
            self.mesh_face_count = Metashape.HighFaceCount
        elif face_count == "Střední":
            self.mesh_face_count = Metashape.MediumFaceCount
        elif face_count == "Nízký":
            self.mesh_face_count = Metashape.LowFaceCount

    def _set_texture_settings(self):
        blending_mode = self.ui.blending_mode_cb.currentText()
        if blending_mode == "Mosaic":
            self.texture_settings["blending"] = Metashape.MosaicBlending
        elif blending_mode == "Average":
            self.texture_settings["blending"] = Metashape.AverageBlending

        self.texture_settings["size"] = int(self.ui.texture_size.currentText())

    def change_button_states(self, state):
        self.ui.start_new_phtgrm_btn.setEnabled(state)
        self.ui.continue_phtgrm_btn.setEnabled(state)

    def _update_photogrammetry_table(self):
        photogrammetry_plans = extract_data_from_csv("./App_data/Test_plan/planned_photogrammetry.csv")
        populate_table(self.ui.tableWidget, photogrammetry_plans)

    def set_path(self, path):
        self.result_path = os.path.join(path, "fotogrammetrie")

    def _photogrammetry_running(self, state):
        self.PHTGR_RUNNING.emit(False)
        self.ui.photogrammetry_running_lbl.setVisible(False)

    def disconnect(self):
        self.cameras.stop_recording()
