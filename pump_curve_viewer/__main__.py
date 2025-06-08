import sys

from PySide6.QtWidgets import QApplication

from pump_curve_viewer.tiles.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
