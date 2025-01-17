
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont

import pyqtgraph as pg

class MainPlotController(object):

    mainPlotCurves = []
    
    def __init__(self):
        pass

    def initializeMainPlot(self):

        self.mainPlotCurves.clear()
        self.mainPlotView.setBackground((69, 69, 69))

        self.mainPlotView.setMouseEnabled(x=False, y=False)  # Disable mouse panning & zooming
        self.mainPlotView.hideButtons()  # Disable corner auto-scale button
        self.mainPlotView.getPlotItem().setMenuEnabled(False)

        my_font = QFont("MS Shell Dlg 2", 10, QFont.Bold)

        font = QFont()
        font.setPixelSize(20)
        
        labelPen = pg.mkPen('w', width=2, style=QtCore.Qt.SolidLine) 

        self.mainPlotView.getAxis("bottom").setStyle(showValues=False)
        self.mainPlotView.getAxis("bottom").setPen(labelPen)
        self.mainPlotView.hideAxis("bottom")

        self.mainPlotView.getAxis("left").setTextPen('w')
        self.mainPlotView.getAxis("left").setTickFont(font)
        self.mainPlotView.getAxis("left").setStyle(tickTextOffset=20)
        self.mainPlotView.getAxis("left").setPen(labelPen)

        self.mainPlotView.addLegend(enableMouse=False)
        for generation, s in self.calc.statistics.items():
            pen = pg.mkPen(self.gameColorPalette[generation], width=3, style=QtCore.Qt.SolidLine) 
            plotDataItem = self.mainPlotView.plot(pen=pen)
            self.mainPlotCurves.append(plotDataItem)

        self.mainPlotView.showGrid(x=False, y=True)

    def drawMainPlotStatistic(self):
        for i in range(len(self.calc.statistics)):
            self.mainPlotCurves[i].setData(self.calc.statistics[i])