from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QSlider,
    QVBoxLayout,
    QHBoxLayout
)

from pump_curve_viewer.user_interface.panel import Panel


class TuningPanel(Panel):
    def __init__(self, parent):
        super().__init__(parent)
        tuning_layout = QVBoxLayout(self)
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

    def update_rotation(self):
        self.n_value.setText(f"{self.n_slider.value()}")

    def update_diameter(self):
        self.d_value.setText(f"{self.d_slider.value()}")