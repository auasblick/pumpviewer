import sys
from PyQt6.QtWidgets import QApplication
from modules.pvapp import PvApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('dark')
    pvapp = PvApp()
    app.exec()
