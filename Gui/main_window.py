import time

from threading import Thread
from datetime import datetime
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow
from Gui.Views.camera_view import CameraView
from Gui.Views.test_plan_view import TestPlanView
from Gui.Views.setting_page_view import SettingsView
from Controllers.logo_controller import LogoController
from Controllers.driver_controller import DriverController
from Gui.Views.photogrammetry_view import PhotogrammetryView
from PySide6.QtCore import QPropertyAnimation, QByteArray, Signal
from Qt_files.Qt_python.ui_Hydraulic_through import Ui_MainWindow
from Utils.csv_work import extract_data_from_csv, change_csv_status


class MainWindow(QMainWindow):
    change_next_flow = Signal(list)
    update_tabs = Signal()
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.drivers = DriverController()
        self.drivers.start()
        self.logo = LogoController()
        self.logo.start()

        self.settings_view = SettingsView(self.logo)
        self.camera_view = CameraView(self.drivers)
        self.photogrammetry_view = PhotogrammetryView(self.drivers)
        self.test_plan_view = TestPlanView(self.logo)
        self.setup_views()

        self.stop = False

        self._init_graphical_changes()
        self._bind_menu_buttons()
        self._bind_emits()
        self._set_save_path("./")

    def setup_views(self):
        self.ui.stackedWidget.addWidget(self.settings_view)
        self.ui.stackedWidget.addWidget(self.camera_view)
        self.ui.stackedWidget.addWidget(self.photogrammetry_view)
        self.ui.stackedWidget.addWidget(self.test_plan_view)

    def _init_graphical_changes(self):
        self.ui.expand_menu_btn.setIcon(QIcon("./App_data/ico.png"))
        self.setWindowIcon(QIcon("./App_data/ico.png"))
        self.ui.logo_4j_btn.setIcon(QIcon('./App_data/4j_logo_150x50.png'))
        self.ui.expand_wgt.setHidden(True)

        self.side_panel_animation = QPropertyAnimation(self.ui.widget, QByteArray(b"maximumWidth"))

        self.ui.stackedWidget.setCurrentWidget(self.settings_view)
        self.setFixedSize(1400, 900)

    def _bind_menu_buttons(self):
        self.ui.logo_4j_btn.clicked.connect(lambda: self._menu_animation(True))
        self.ui.expand_menu_btn.clicked.connect(lambda: self._menu_animation(False))

        self.ui.settings_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.settings_view))
        self.ui.process_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.test_plan_view))
        self.ui.photo_pg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.photogrammetry_view))
        self.ui.cam_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.camera_view))

        self.ui.stop_btn.clicked.connect(self._stop_through)

    def _bind_emits(self):
        self.update_tabs.connect(self._generate_test_plan)

        self.settings_view.GENERATE_TEST_PLAN.connect(self._generate_test_plan)
        self.settings_view.SAVE_PATH.connect(self._set_save_path)

        self.test_plan_view.START_PLAN.connect(self._start_plans)
        self.photogrammetry_view.PHTGR_RUNNING.connect(self._show_photogrammetry_lbl)

        self.change_next_flow.connect(lambda flow: self.test_plan_view.update_next_planed_change(flow[0], flow[1], flow[2]))
        self.update_tabs.connect(self.test_plan_view.update_tabs)

    def _set_save_path(self, path):
        self.camera_view.set_path(path)
        self.photogrammetry_view.set_path(path)
        self.test_plan_view.set_path(path)

    def _generate_test_plan(self):
        self.test_plan_view.update_tabs()

    def _start_plans(self):
        self._change_button_state(False)
        Thread(target=self._iterate_flow_plans, daemon=True).start()
        Thread(target=self._iterate_cam_plans).start()

    def _iterate_cam_plans(self):
        path = "./App_data/Test_plan/cam_plans.csv"
        flow_plans = extract_data_from_csv(path)
        for i, row in enumerate(flow_plans):
            if not self.stop:
                target_time = datetime.strptime(row[0], "%d.%m.%Y %H:%M:%S")
                if row[3] == "0":
                    self._wait_until(target_time)
                    print(f"setting drivers to: {row[1]}")
                    self.drivers.set_position(int(row[1]))
                    time.sleep(12)
                    if row[2] == "foto 1":
                        self.camera_view.save_photo(1)
                        time.sleep(1)
                    if row[2] == "foto 2":
                        self.camera_view.save_photo(2)
                        time.sleep(1)
                    if row[2] == "video 1":
                        self.camera_view.save_video(1, blocking=True)
                    if row[2] == "video 2":
                        self.camera_view.save_video(2, blocking=True)
                    if row[2] == "orthophoto":
                        self.camera_view.make_orthophoto_image(quality=row[1],blocking=True)
                    if row[2] == "photogrm":
                        self.photogrammetry_view.start_photogrammetry(quality=row[1], blocking=True)
                    change_csv_status(path, i, 3)
                    self.update_tabs.emit()

    def _iterate_flow_plans(self):
        path = "./App_data/Test_plan/planned_flow.csv"
        flow_plans = extract_data_from_csv(path)
        self.test_plan_view.start_saving()

        for i, row in enumerate(flow_plans):
            if not self.stop:
                target_time = datetime.strptime(row[0], "%d.%m.%Y %H:%M:%S")
                flow_value = float(row[1])
                self.change_next_flow.emit([i / (len(flow_plans)) * 100, row[0], row[1]])
                if row[2] == "0":
                    self._wait_until(target_time)
                    self._change_flow(flow_value)
                    change_csv_status(path, i, 2)
                    self.update_tabs.emit()

        self.test_plan_view.stop_saving()
        self.test_plan_view.show_testplan_lbl(False)
        self._change_button_state(True)
        self.stop = False

    def _wait_until(self, target_time):
        while datetime.now() < target_time and not self.stop:
            time.sleep(1)

    def _change_flow(self, flow: float):
        flow_voltage = int(flow * 10)
        self.logo.write_logo_ushort(1, flow_voltage)

    def _menu_animation(self, state: bool):
        start = 180 if state else 0
        end = 0 if state else 180
        self.side_panel_animation.setDuration(200)
        self.side_panel_animation.setStartValue(start)
        self.side_panel_animation.setEndValue(end)
        self.side_panel_animation.finished.connect(lambda: self.ui.widget.setMaximumWidth(end))
        self.side_panel_animation.start()
        self.ui.expand_wgt.setHidden(not state)

    def _change_button_state(self, state):
        self.test_plan_view.change_button_state(state)
        self.settings_view.change_button_status(state)

    def _show_photogrammetry_lbl(self, state):
        self.test_plan_view.show_photogrammetry_lbl(state)

    def _stop_through(self):
        self.logo.write_logo_ushort(1, 0)
        self.stop = True

    def on_app_exit(self):
        self.camera_view.disconnect()
        self.photogrammetry_view.disconnect()
        self.logo.disconnect()