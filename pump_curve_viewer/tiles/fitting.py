from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from pump_curve_viewer.user_interface.pump_graph import PumpGraph
from pump_curve_viewer.user_interface.pump_scroll import PumpScroll
from pump_curve_viewer.user_interface.tuning_panel import TuningPanel


class FittingWidget(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        # drawing panel
        self.__pump_graph: PumpGraph = PumpGraph(self)

        # side panels
        self.__tuning_panel: TuningPanel = TuningPanel(self)
        self.__pump_scrolling_panel: PumpScroll = PumpScroll(self)
        self.__side_layout = QVBoxLayout()
        self.__side_layout.addWidget(self.__tuning_panel, stretch=1)
        self.__side_layout.addWidget(self.__pump_scrolling_panel, stretch=1)

        # layout
        self.central_layout = QHBoxLayout(self)
        self.central_layout.addWidget(self.__pump_graph, stretch=3)
        self.central_layout.addLayout(self.__side_layout, stretch=1)

        # sizing
        self.setMinimumSize(800, 200)
