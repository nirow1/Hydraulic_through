import os
import csv
import time

from datetime import datetime
from threading import Thread

from PySide6.QtCore import Signal
from Utils.csv_work import extract_data_from_csv
from Utils.number_validator import FloatValidator
from Controllers.logo_controller import LogoController
from Qt_files.Qt_python.ui_test_plan_view import Ui_Form
from PySide6.QtWidgets import QWidget, QTableWidgetItem


class TestPlanView(QWidget):
    LOAD_PLAN = Signal()
    START_PLAN = Signal()

    def __init__(self, logo: LogoController):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.logo = logo

        self.path: str = ""
        self.saving = False
        self.flow: float= 0.0

        self._initial_graphical_changes()
        self._bind_buttons()
        self._bind_emits()

    #todo: přidat sekundy do tabulky
    def _initial_graphical_changes(self):
        self.ui.load_btn.hide()
        self.ui.send_through_le.setValidator(FloatValidator(2, 1))
        self.ui.flow_tw.verticalHeader().setVisible(False)
        self.ui.cam_plans_tw.verticalHeader().setVisible(False)
        self.ui.continue_plan_btn.setVisible(False)
        self._set_columns()

    def _bind_emits(self):
        self.logo.LOGO_DATA.connect(self._logo_data_to_lbl)

    def _bind_buttons(self):
        self.ui.send_through_btn.clicked.connect(lambda: self._change_flow(float(self.ui.send_through_le.text())))
        self.ui.continue_plan_btn.clicked.connect(lambda: self.LOAD_PLAN.emit())
        self.ui.start_plan_btn.clicked.connect(self.START_PLAN.emit)

    def _change_flow(self, flow: float):
        flow_voltage = int(flow * 10)
        self.logo.write_logo_ushort(1, flow_voltage)

    def _logo_data_to_lbl(self, flow):
        self.ui.current_flow_lbl.setText(str(flow))
        self.flow = flow

    def start_saving(self):
        self.saving = True
        Thread(target=self._saving_thread).start()

    def _saving_thread(self):
        save_path = f"{self.path}/zaznam_prutoku{datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"

        while self.saving:
            file_exists = os.path.exists(self.path)
            write_header = not file_exists or os.stat(self.path).st_size == 0

            with open(save_path, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=";")
                if write_header:
                    writer.writerow(["Čas", "Průtok"])
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([current_time, self.flow])

            time.sleep(5)

    def stop_saving(self):
        self.saving = False

    def update_next_planed_change(self, value, next_date: str, next_flow: float ):
        self.ui.date_lbl.setText(next_date)
        self.ui.through_lbl.setText(str(next_flow))
        self.ui.progressBar.setValue(value)

    def update_tabs(self):
        flow_plans = extract_data_from_csv("./App_data/Test_plan/planed_flow.csv")
        cam_plans = extract_data_from_csv("./App_data/Test_plan/cam_plans.csv")
        self.populate_table(self.ui.flow_tw, flow_plans)
        self.populate_table(self.ui.cam_plans_tw, cam_plans)

    def set_path(self, path: str):
        self.path = path

    def change_button_state(self, state):
        self.ui.send_through_btn.setEnabled(state)
        self.ui.start_plan_btn.setEnabled(state)
        self.ui.continue_plan_btn.setEnabled(state)

    def populate_table(self,table, data):
        table.setRowCount(0)  # Clear existing rows
        for row_data in data:
            row_position = table.rowCount()
            table.insertRow(row_position)
            for column, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                table.setItem(row_position, column, item)

    def _set_columns(self):
        self.ui.flow_tw.setColumnWidth(0, 170)
        self.ui.flow_tw.setColumnWidth(1, 47)
        self.ui.flow_tw.setColumnWidth(2, 47)
        self.ui.cam_plans_tw.setColumnWidth(0, 170)
