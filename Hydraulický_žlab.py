import sys

from PySide6.QtWidgets import QApplication
from Gui.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.aboutToQuit.connect(window.on_app_exit)
    window.show()
    sys.exit(app.exec())