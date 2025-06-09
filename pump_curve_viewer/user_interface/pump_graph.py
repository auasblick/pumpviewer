from PySide6.QtWidgets import QWidget
from pyqtgraph import PlotWidget
import numpy as np
from pump_curve_viewer.user_interface.color import ColorManager


class PumpGraph(PlotWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        __color_manager = ColorManager()
        self.setBackground([__color_manager.background]*3)
        self.setXRange(0, 100)
        self.setYRange(-100, 100)
        self.setTitle("Pump Graph")
        self.setLabel("bottom", "Flow Rate [<math>m<sup>3</sup>/s</math>]")
        self.setLabel("left", "Height [m]")

    def add_curve(self, x: np.ndarray, y: np.ndarray):
        self.plot(x, y)
