
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont

import pyqtgraph as pg

class MiniPlotManager(object):
    def __init__(self):
        pass
    

    def initializeMiniPlot(self):
        self.miniPlotView.setBackground((89, 89, 89))

        self.miniPlotView.setMouseEnabled(x=False, y=False)  # Disable mouse panning & zooming
        self.miniPlotView.hideButtons()  # Disable corner auto-scale button
        self.miniPlotView.getPlotItem().setMenuEnabled(False)

        my_font = QFont("MS Shell Dlg 2", 10, QFont.Bold)

        font = QFont()
        font.setPixelSize(20)
        
        labelPen = pg.mkPen('w', width=2, style=QtCore.Qt.SolidLine) 

        self.miniPlotView.hideAxis("bottom")

        self.miniPlotView.hideAxis("left")

        self.miniPlotView.addLegend(enableMouse=False)

        
        # for generation, s in self.calc.statistics.items():
        #     pen = pg.mkPen(self.gameColorPalette[generation], width=3, style=QtCore.Qt.SolidLine) 
        #     plotDataItem = self.miniPlotView.BarGraphItem(pen=pen)
        #     self.miniPlotBars.append(plotDataItem)

        y = []
        brushes = [pg.mkBrush(self.gameColorPalette[generation], width=3, style=QtCore.Qt.SolidLine) for generation, s in self.calc.statistics.items()]
        pens = [None for generation, s in self.calc.statistics.items() ]
        for generation, s in self.calc.statistics.items():
            y.append(0)
 
        # create horizontal list i.e x-axis
        x = range(self.calc.thisRule.generationsCount + 1)
 

        # create pyqt5graph bar graph item
        # with width = 0.6
        # with bar colors = green
        self.bargraph = pg.BarGraphItem(x=x, height=y, width = 1, brushes=brushes, pens=pens)
 
        # add item to plot window
        # adding bargraph item to the plot window
        self.miniPlotView.clear()
        self.miniPlotView.addItem(self.bargraph)

        self.miniPlotView.showGrid(x=False, y=False)

        self.drawMiniPlotStatistic()

    def drawMiniPlotStatistic(self):
        if len(self.calc.statistics[0]) < 2:
            return
        
        y = []
        for generation, s in self.calc.statistics.items():
            y.append(s[-1])

        self.bargraph.setOpts(x=range(self.calc.thisRule.generationsCount + 1), height=y)