import sys

from PySide6.QtWidgets import QApplication

from user_interface.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
