
from PyQt5 import QtCore
from PyQt5.QtGui import QFont

import pyqtgraph as pg

class MiniPlotManager(object):
    def __init__(self):
        pass
    
    def miniPlotInitialize(self):
        self.miniPlotView.setBackground((89, 89, 89))
        self.miniPlotView.setMouseEnabled(x=False, y=False)  # Disable mouse panning & zooming
        self.miniPlotView.hideButtons()  # Disable corner auto-scale button
        self.miniPlotView.getPlotItem().setMenuEnabled(False)

        font = QFont()
        font.setPixelSize(20)

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
        print("Plot initialized")
        print(self.thisRule.generationsCount)
        x = range(self.thisRule.generationsCount + 1)
 

        # create pyqt5graph bar graph item

        self.bargraph = pg.BarGraphItem(x=x, height=y, width = 1, brushes=brushes, pens=pens)
 
        # add item to plot window
        # adding bargraph item to the plot window
        self.miniPlotView.clear()
        self.miniPlotView.addItem(self.bargraph)

        self.miniPlotView.showGrid(x=False, y=False)

        self.miniPlotDrawStatistic()

    def miniPlotDrawStatistic(self):
        if len(self.calc.statistics[0]) < 2:
            return
        
        y = []
        for generation, s in self.calc.statistics.items():
            y.append(s[-1])

        self.bargraph.setOpts(x=range(self.calc.thisRule.generationsCount + 1), height=y)