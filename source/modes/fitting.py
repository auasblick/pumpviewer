import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QSlider,
    QScrollArea,
    QVBoxLayout,
    QHBoxLayout
)

from source.QTHelp import Panel


class FittingWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ## Drawing panel
        self.graph_panel = Panel()
        self.setMinimumWidth(1000)
        ll = QVBoxLayout(self.graph_panel)
        self.plot_graph = pg.PlotWidget()
        self.plot_graph.setBackground([32, 32, 32])
        ll.addWidget(self.plot_graph)
        values_x = np.arange(0, 100, 1, dtype=np.float32)
        values_y = -values_x**2 + 10000
        self.plot_graph.plot(values_x, values_y)
        self.plot_graph.setXRange(0,100)
        self.plot_graph.setTitle("Pump Graph")
        self.plot_graph.setLabel("bottom", "Flow Rate [<math>m<sup>3</sup>/s</math>]")
        self.plot_graph.setLabel("left", "Height [m]")

        ## Side panels
        # Tuning parameters
        self.tuning_panel = Panel()
        tuning_layout = QVBoxLayout(self.tuning_panel)
        tuning_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        n_layout = QHBoxLayout()
        self.n_label = QLabel("Rotations [n]")
        self.n_value = QLabel(f"{0}")
        self.n_slider = QSlider(Qt.Orientation.Horizontal)
        self.n_slider.sliderMoved.connect(self.update_rotation)
        n_layout.addWidget(self.n_label)
        n_layout.addWidget(self.n_value)
        n_layout.addWidget(self.n_slider)
        d_layout = QHBoxLayout()
        self.d_label = QLabel("Diameter [mm]")
        self.d_value = QLabel(f"{0}")
        self.d_slider = QSlider(Qt.Orientation.Horizontal)
        self.d_slider.sliderMoved.connect(self.update_diameter)
        d_layout.addWidget(self.d_label)
        d_layout.addWidget(self.d_value)
        d_layout.addWidget(self.d_slider)
        tuning_layout.addLayout(n_layout)
        tuning_layout.addLayout(d_layout)

        # Pump panel
        self.pump_panel = Panel()
        self.pump_scroll = QScrollArea(self.pump_panel)
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

        self.side_layout = QVBoxLayout()
        self.side_layout.addWidget(self.tuning_panel)
        self.side_layout.addWidget(self.pump_scroll)
        self.side_layout.setStretch(0,1)
        self.side_layout.setStretch(1,1)

        # define central widget
        self.central_layout = QHBoxLayout(self)
        self.central_layout.addWidget(self.graph_panel)
        self.central_layout.addLayout(self.side_layout)
        # Set the stretch factors: 75% to graph panel, 25% to side container
        self.central_layout.setStretch(0, 3)  # Graph panel stretch factor
        self.central_layout.setStretch(1, 1)  # Side panel stretch factor


    def update_rotation(self):
        self.n_value.setText(f"{self.n_slider.value()}")


    def update_diameter(self):
        self.d_value.setText(f"{self.d_slider.value()}")
