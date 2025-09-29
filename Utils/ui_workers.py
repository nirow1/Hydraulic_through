from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QTableWidgetItem, QProgressBar, QWidget


def show_status_message(message: QWidget, duration: float):
    message.setVisible(True)
    QTimer.singleShot(int(duration * 1000), lambda: message.setVisible(False))

def populate_table(table, data):
    table.setRowCount(0)  # Clear existing rows
    for row_data in data:
        row_position = table.rowCount()
        table.insertRow(row_position)
        for column, value in enumerate(row_data):
            item = QTableWidgetItem(str(value))
            table.setItem(row_position, column, item)

def update_progressbar(progressbar: QProgressBar, current: int, total: int):
    if total <= 0:
        percent = 0
    else:
        percent = int((current / (total - 1)) * 100)
    percent = max(0, min(100, percent))

    progressbar.setValue(percent)