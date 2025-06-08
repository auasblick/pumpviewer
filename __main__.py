import sys

from PySide6.QtWidgets import QApplication

from source.pvapp import PvApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pvapp = PvApp()
    app.exec()
