from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMainWindow)
from PyQt6.QtGui import QIcon


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

        # Side panels
        self.config_placeholder = QLabel("TODO: modifiable pump metrics")
        self.tree_placeholder = QLabel("TODO: pump tree")
        self.button = QPushButton("Hello")
        self.side_layout = QVBoxLayout()
        self.side_layout.addWidget(self.config_placeholder)
        self.side_layout.addWidget(self.tree_placeholder)

        # Main window widget
        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout(self.central_widget)
        self.central_layout.addWidget(self.graph_placeholder)
        self.central_layout.addLayout(self.side_layout)
        self.setCentralWidget(self.central_widget)

        # Show
        self.show()
