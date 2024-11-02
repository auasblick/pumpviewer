import sys
from PyQt6.QtWidgets import QApplication
from source.pvapp import PvApp

app = QApplication(sys.argv)
pvapp = PvApp()
app.exec()

