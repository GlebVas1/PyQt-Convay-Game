
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont

import pyqtgraph as pg

class MainPlotController(object):

    mainPlotCurves = []
    mainPlotPens = []
    mainPlotBrushes = []

    def __init__(self):
        pass

    def mainPlotInitializeActions(self):
        self.mainPlotEnableXGrid.stateChanged.connect(self.mainPlotChangeGridMode)
        self.mainPlotEnableYGrid.stateChanged.connect(self.mainPlotChangeGridMode)
        self.lineThicknessSpinBox.valueChanged.connect(self.mainPlotChangePenThickness)
        self.mainPlotFillUnder.stateChanged.connect(self.mainPlotEnableFill)

    def mainPlotInitialize(self):
        self.mainPlotCurves.clear()
        self.mainPlotPens.clear()
        self.mainPlotBrushes.clear()
        self.mainPlotView.clear()
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
        # self.mainPlotView.hideAxis("bottom") -- cant use that, because also diables vertical x grid

        self.mainPlotView.getAxis("left").setTextPen('w')
        self.mainPlotView.getAxis("left").setTickFont(font)
        self.mainPlotView.getAxis("left").setStyle(tickTextOffset=20)
        self.mainPlotView.getAxis("left").setPen(labelPen)

        self.mainPlotView.addLegend(enableMouse=False)

        for generation, s in self.calc.statistics.items():
            pen = pg.mkPen(self.gameColorPalette[generation], width=3, style=QtCore.Qt.SolidLine)
            brushColor = (self.gameColorPalette[generation][0], self.gameColorPalette[generation][1], self.gameColorPalette[generation][2], 30)
            brush = pg.mkBrush(brushColor, width=3, style=QtCore.Qt.SolidLine)
            self.mainPlotPens.append(pen)
            self.mainPlotBrushes.append(brush)
            plotDataItem = self.mainPlotView.plot(pen=pen, brush=brush)
            self.mainPlotCurves.append(plotDataItem)

        self.mainPlotView.showGrid(x=self.mainPlotEnableXGrid.isChecked(), y=self.mainPlotEnableYGrid.isChecked())
        for curve in self.mainPlotCurves:
            curve.setFillLevel(1.0 if self.mainPlotFillUnder.isChecked() else None)
        

        self.legendAliveFrame.setStyleSheet("background-color : " + self.gameColorPalleteQt[self.thisRule.generationsCount])
        self.legendEmptyFrame.setStyleSheet("background-color : " + self.gameColorPalleteQt[0])

        self.mainPlotDrawStatistic()

    def mainPlotDrawStatistic(self):
        """In the nutshell a function that makes the main plot to update after changing the color pallete, rules changing etc"""
        for i in range(len(self.calc.statistics)):
            self.mainPlotCurves[i].setData(self.calc.statistics[i][0 : self.plotsFrameWindow.value()])
    
    def mainPlotChangeGridMode(self):
        self.mainPlotView.showGrid(x=self.mainPlotEnableXGrid.isChecked(), y=self.mainPlotEnableYGrid.isChecked())
        self.mainPlotDrawStatistic()

    def mainPlotChangePenThickness(self):
        for pen in self.mainPlotPens:
            pen.setWidth(self.lineThicknessSpinBox.value())
        self.mainPlotDrawStatistic()

    def mainPlotEnableFill(self):
        for curve in self.mainPlotCurves:
            curve.setFillLevel(1.0 if self.mainPlotFillUnder.isChecked() else None)
        self.mainPlotDrawStatistic()