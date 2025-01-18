from math import sqrt
import random
from PyQt5 import QtWidgets, QtCore
from functools import partial

class BrushManager(object):

    brushSize = 1
    circleBrush = False

    currentBrushState = 0

    def initializeBrushManager(self):
        self.brushSizeSpinBox.valueChanged.connect(self.changeBrushSize)
        self.fillAllCells.clicked.connect(self.changeAllButtonsStateInGame)

    def paintInPlace(self, x : int, y : int):
        size = self.brushSize
        if self.brushRandomSize.isChecked():
            size = random.randint(0, 5)

        for i in range(1 - self.brushSize, self.brushSize):
            for j in range(1 - self.brushSize, self.brushSize):
            
                if self.brushSetRound.isChecked():
                    if i ** 2 + j ** 2 >= size ** 2:
                        continue
                x1 = (x + i + self.xFieldSize) % self.xFieldSize
                y1 = (y + j + self.yFieldSize) % self.yFieldSize

                if self.brushRandomState.isChecked():
                    self.changeButtonState(x1, y1, random.randint(0, self.calc.thisRule.generationsCount))
                else:
                    self.changeButtonStateInGame(x1, y1)

    def changeBrushSize(self):
        self.brushSize = self.brushSizeSpinBox.value()
    