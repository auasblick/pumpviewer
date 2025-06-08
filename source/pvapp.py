from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QTabWidget,
    QMainWindow)

from source.modes.fitting import FittingWidget
from source.modes.tracing import TracingWidget


class PvApp(QMainWindow):
    """
    This is the main window, and holds all the submenus
    """
    def __init__(self):
        # inherit from
        super().__init__()

        # visual identifiers
        ujams_icon = QIcon(r"source/media/ujams_icon.ico")
        self.setWindowIcon(ujams_icon)
        self.setWindowTitle("UJAMS Pump Curve Modification Tool")
        self.setMinimumSize(200, 200)
        self.resize(1080, 720)

        # Tabs
        self.tab_widget = QTabWidget(self)
        self.fit = FittingWidget()
        self.tab_widget.addTab(self.fit, "Fitting")
        self.trace = TracingWidget()
        self.tab_widget.addTab(self.trace, "Tracing")

        self.setCentralWidget(self.tab_widget)

        # Show
        self.show()
