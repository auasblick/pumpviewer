from pyqtgraph import PlotWidget
import numpy as np


class PumpGraph(PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        values_x = np.arange(0, 100, 1, dtype=np.float32)
        values_y = -values_x ** 2 + 10000
        self.plot(values_x, values_y)
        self.setBackground([32, 32, 32])
        self.setXRange(0, 100)
        self.setTitle("Pump Graph")
        self.setLabel("bottom", "Flow Rate [<math>m<sup>3</sup>/s</math>]")
        self.setLabel("left", "Height [m]")
