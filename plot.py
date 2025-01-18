from PyQt5 import QtWidgets, QtCore

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from scipy.interpolate import make_interp_spline, BSpline
import numpy as np

# https://stackoverflow.com/questions/72568050/plotting-a-chart-inside-a-pyqt-gui
# https://www.pythonguis.com/tutorials/plotting-matplotlib/
# https://stackoverflow.com/questions/8955869/why-is-plotting-with-matplotlib-so-slow
# https://pyqtgraph.readthedocs.io/en/latest/getting_started/how_to_use.html

class QTMultiPlot(QtWidgets.QWidget):

    colorPalette = []
    def __init__(self, parent):
        super().__init__(parent)

        self.figure = plt.figure(figsize=(8, 6))
        self.figureCanvas = FigureCanvas(self.figure)

        layout = QtWidgets.QGridLayout(parent)
        layout.addWidget(self.figureCanvas)

        self.setLayout(layout)
        self.ax = self.figure.add_subplot(111)
        self.figure.set_facecolor((0.27, 0.27, 0.27))

        self.ax.set_facecolor((0.27, 0.27, 0.27))
        
        self.ax.spines['bottom'].set_color('#ffffff')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['left'].set_color('#ffffff')
        
        self.figure.show()  
        self.figureCanvas.show()

        
        

    def updatePlot(self, x : list, values):
        self.ax.cla()

        # NpX = np.array(x)
        # NpXinterp = np.linspace(NpX.min(), NpX.max(), 200) 
        # for generation, val in values.items():
        #     NpY = np.array(val)
        #     spl = make_interp_spline(NpX, NpY, k=2)  # type: BSpline
        #     NpYinterp = spl(NpXinterp)
        #     self.ax.plot(NpXinterp, NpYinterp, color=[self.colorPalette[generation][0] / 255, self.colorPalette[generation][1] / 255, self.colorPalette[generation][2] / 255])
        
        
        for generation, val in values.items():
            self.ax.plot(x, val, color=[self.colorPalette[generation][0] / 255, self.colorPalette[generation][1] / 255, self.colorPalette[generation][2] / 255])
        
        for item in ([self.ax.title, self.ax.xaxis.label, self.ax.yaxis.label] + self.ax.get_xticklabels() + self.ax.get_yticklabels()):
            item.set_fontsize(11)
            item.set_color('#ffffff')

        self.figureCanvas.draw()

