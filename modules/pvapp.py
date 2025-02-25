from PyQt6.QtWidgets import (
    QTabWidget,
    QMainWindow)
from PyQt6.QtGui import QIcon
from modules.fitting.fitting import FittingWidget
from modules.tracing.tracing import TracingWidget
from modules.qt.QTHelp import is_dark_mode


class PvApp(QMainWindow):
    """
    This is the main window, and holds all the submenus
    """
    def __init__(self):
        # inherit from
        super().__init__()

        # determine color based on whether dark mode is active
        print(f"Is dark mode: {is_dark_mode()}")
        if is_dark_mode():
            background_color = "rgb(32, 32, 32)"
            active_background_color = "rgb(64, 0, 0)"
            foreground_color = "rgb(240, 240, 240)"
        else:
            background_color = "rgb(240, 240, 240)"
            active_background_color = "rgb(250, 250, 250)"
            foreground_color = "rgb(0, 0, 0)"
        # Apply the background and foreground colors
        self.background_color = background_color
        self.foreground_color = foreground_color
        self.setStyleSheet(f"background-color: {background_color}; color: {foreground_color};")

        # visual identifiers
        ujams_icon = QIcon(r"source/media/ujams_icon.ico")
        self.setWindowIcon(ujams_icon)
        self.setWindowTitle("UJAMS Pump Curve Modification Tool")
        self.setMinimumSize(200, 200)
        self.resize(1080, 720)

        stylesheet = f"""
            QTabBar::tab:selected {{background: {active_background_color}; foreground: {foreground_color};}}
            QTabBar::tab::unselected {{background: {background_color};}}
            """

        # Tabs
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setStyleSheet(stylesheet)
        self.fit = FittingWidget()
        self.tab_widget.addTab(self.fit, "Fitting")
        self.trace = TracingWidget()
        self.tab_widget.addTab(self.trace, "Tracing")

        self.setCentralWidget(self.tab_widget)

        # Show
        self.show()
