from importlib.resources import files as ui_files
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QTabWidget,
    QMainWindow,
)

from pump_curve_viewer.tiles.fitting import FittingWidget
from pump_curve_viewer.tiles.tracing import TracingWidget


class MainWindow(QMainWindow):
    """
    This is the main window of the pump curve viewer, and holds all the submenus
    """
    def __init__(self):
        # inherit from
        super().__init__()

        # visual identifiers
        icon_path = Path(ui_files("user_interface").joinpath("resources").joinpath("ujams_icon.ico"))
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowTitle("Auasblick Pump Curve Viewer")
        self.setMinimumSize(200, 200)
        self.resize(1080, 720)

        # Tabs
        self.tab_widget = QTabWidget(self)
        self.fit = FittingWidget(self)
        self.tab_widget.addTab(self.fit, "Fitting")
        self.trace = TracingWidget()
        self.tab_widget.addTab(self.trace, "Tracing")

        # layout
        self.setCentralWidget(self.tab_widget)

        # Show
        self.show()
