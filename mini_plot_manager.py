
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont

import pyqtgraph as pg

class MiniPlotManager(object):
    def __init__(self):
        pass
    
    miniPlotBars = []

    def initializeMiniPlot(self):
        self.miniPlotView.setBackground((69, 69, 69))

        self.miniPlotView.setMouseEnabled(x=False, y=False)  # Disable mouse panning & zooming
        self.miniPlotView.hideButtons()  # Disable corner auto-scale button
        self.miniPlotView.getPlotItem().setMenuEnabled(False)

        my_font = QFont("MS Shell Dlg 2", 10, QFont.Bold)

        font = QFont()
        font.setPixelSize(20)
        
        labelPen = pg.mkPen('w', width=2, style=QtCore.Qt.SolidLine) 

        self.miniPlotView.getAxis("bottom").setStyle(showValues=False)
        self.miniPlotView.getAxis("bottom").setPen(labelPen)
        self.miniPlotView.hideAxis("bottom")

        self.miniPlotView.getAxis("left").setTextPen('w')
        self.miniPlotView.getAxis("left").setTickFont(font)
        self.miniPlotView.getAxis("left").setStyle(tickTextOffset=20)
        self.miniPlotView.getAxis("left").setPen(labelPen)

        self.miniPlotView.addLegend(enableMouse=False)

        
        # for generation, s in self.calc.statistics.items():
        #     pen = pg.mkPen(self.gameColorPalette[generation], width=3, style=QtCore.Qt.SolidLine) 
        #     plotDataItem = self.miniPlotView.BarGraphItem(pen=pen)
        #     self.miniPlotBars.append(plotDataItem)

        y = []

        for generation, s in self.calc.statistics.items():
            # pen = pg.mkPen(self.gameColorPalette[generation], width=3, style=QtCore.Qt.SolidLine) 
            # plotDataItem = self.miniPlotView.BarGraphItem(pen=pen)
            # self.miniPlotBars.append(plotDataItem)
            y.append(0)
 
        # create horizontal list i.e x-axis
        x = range(self.calc.thisRule.generationsCount + 1)
 
        # create pyqt5graph bar graph item
        # with width = 0.6
        # with bar colors = green
        self.bargraph = pg.BarGraphItem(x, width = 0.6, brush ='g')
 
        # add item to plot window
        # adding bargraph item to the plot window
        self.miniPlotView.addItem(self.bargraph)

        self.miniPlotView.showGrid(x=False, y=False)

    def drawMiniPlotStatistic(self):
        if len(self.calc.statistics[0]) < 2:
            return
        y = []

        for generation, s in self.calc.statistics.items():
            # pen = pg.mkPen(self.gameColorPalette[generation], width=3, style=QtCore.Qt.SolidLine) 
            # plotDataItem = self.miniPlotView.BarGraphItem(pen=pen)
            # self.miniPlotBars.append(plotDataItem)
            y.append(s[-1])

        self.bargraph.setData(y)
        for i in range(len(self.calc.statistics)):
            # self.miniPlotBars[i].setData(self.calc.statistics[i][-1])
            pass