from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout

from pump_curve_viewer.user_interface.panel import Panel


class TracingWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Drawing panel
        self.graph_placeholder = QLabel("TODO: display media content")
        self.graph_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.graph_panel = Panel()
        self.setMinimumWidth(1000)
        ll = QVBoxLayout(self.graph_panel)
        ll.addWidget(self.graph_placeholder)

        # Side panels
        self.tuning_panel = Panel()
        tuning_layout = QVBoxLayout(self.tuning_panel)
        self.tuning_placeholder = QLabel("TODO: tracing settings")
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

        # define central widget
        self.central_layout = QHBoxLayout(self)
        self.central_layout.addWidget(self.graph_panel)
        self.central_layout.addLayout(self.side_layout)
        # Set the stretch factors: 75% to graph panel, 25% to side container
        self.central_layout.setStretch(0, 3)  # Graph panel stretch factor
        self.central_layout.setStretch(1, 1)  # Side panel stretch factor
