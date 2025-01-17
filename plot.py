from PyQt5 import QtWidgets, QtCore

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class QTMultiPlot(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.figure = plt.figure(figsize=(5, 5))
        self.figureCanvas = FigureCanvas(self.figure)
        self.navigationToolbar = NavigationToolbar(self.figureCanvas, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.navigationToolbar)
        layout.addWidget(self.figureCanvas)
        self.setLayout(layout)

    def draw(self, x : list, values):
        ax = self.figure.add_subplot(111)
