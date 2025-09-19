from PySide6.QtWidgets import QTableWidgetItem


def populate_table(table, data):
    table.setRowCount(0)  # Clear existing rows
    for row_data in data:
        row_position = table.rowCount()
        table.insertRow(row_position)
        for column, value in enumerate(row_data):
            item = QTableWidgetItem(str(value))
            table.setItem(row_position, column, item)