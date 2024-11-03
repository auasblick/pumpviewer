from PyQt6.QtWidgets import (
    QWidget,
    QLayout,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMainWindow)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from source.QTHelp import Panel

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

        # Drawing panel
        self.graph_placeholder = QLabel("TODO: basic graphs")
        self.graph_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.graph_panel = Panel()
        self.setMinimumWidth(1000)
        ll = QVBoxLayout(self.graph_panel)
        ll.addWidget(self.graph_placeholder)

        # Side panels
        self.tuning_panel = Panel()
        tuning_layout = QVBoxLayout(self.tuning_panel)
        self.tuning_placeholder = QLabel("TODO: pump tuning parameters")
        self.tuning_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tuning_layout.addWidget(self.tuning_placeholder)

        self.pump_panel = Panel()
        pump_layout = QVBoxLayout(self.pump_panel)
        self.tree_placeholder = QLabel("TODO: pump tree")
        self.tree_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pump_layout.addWidget(self.tree_placeholder)

        self.side_layout = QVBoxLayout()
        self.side_layout.addWidget(self.tuning_panel)
        self.side_layout.addWidget(self.pump_panel)

        # Main window widget
        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout(self.central_widget)
        self.central_layout.addWidget(self.graph_panel)
        self.central_layout.addLayout(self.side_layout)
        # Set the stretch factors: 75% to graph panel, 25% to side container
        self.central_layout.setStretch(0, 3)  # Graph panel stretch factor
        self.central_layout.setStretch(1, 1)  # Side panel stretch factor
        self.setCentralWidget(self.central_widget)

        # Show
        self.show()
