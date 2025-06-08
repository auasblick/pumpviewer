from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QScrollArea,
    QVBoxLayout
)

from pump_curve_viewer.user_interface.panel import Panel


class PumpScroll(Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.pump_scroll = QScrollArea(self)
        self.pump_widget = QWidget(self.pump_scroll)
        pump_layout = QVBoxLayout(self.pump_widget)
        for i in range(200):
            pump = QLabel(f"Pump number {i}")
            pump.setAlignment(Qt.AlignmentFlag.AlignLeft)
            pump_layout.addWidget(pump)
        self.pump_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.pump_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.pump_scroll.setWidgetResizable(True)
        # TODO: fix scrollable: https://www.pythonguis.com/tutorials/PySide6-qscrollarea/