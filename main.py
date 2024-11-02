from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys
import numpy as np
# import positioning as pos
# import generationing as gen

# important globals:
# app; screen_width; screen_height; w_width; w_height; color; task;
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("UJAMS Pump Curve Modification Tool")
window.setMinimumSize(200, 200)
ujams_icon = QIcon(r"media\ujams_icon.ico")
window.setWindowIcon(ujams_icon)
window.show()
app.exec()
