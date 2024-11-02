from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtGui import QIcon

class PvApp(QMainWindow):
    """
    This is the main window, and holds all the submenus
    """
    def __init__(self):
        # inherit from
        super().__init__()

        # visual identifiers
        ujams_icon = QIcon(r"source/media\ujams_icon.ico")
        self.setWindowIcon(ujams_icon)
        self.setWindowTitle("UJAMS Pump Curve Modification Tool")
        self.setMinimumSize(200, 200)

        # start position
        self.size()

        # show
        self.show()