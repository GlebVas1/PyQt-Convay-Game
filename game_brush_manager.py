from math import sqrt
from PyQt5 import QtWidgets, QtCore
from functools import partial

class BrushManager(object):

    brushSize = 1
    circleBrush = False

    currentBrushState = 0

    def initializeBrushManager(self):
        self.brushSizeSpinBox.valueChanged.connect(self.changeBrushSize)

    def paintInPlace(self, x : int, y : int):
        for i in range(1 - self.brushSize, self.brushSize):
            for j in range(1 - self.brushSize, self.brushSize):
                if self.circleBrush:
                    if sqrt(i * i + j * j) > self.brushSize:
                        continue
                x1 = (x + i + self.xFieldSize) % self.xFieldSize
                y1 = (y + j + self.yFieldSize) % self.yFieldSize
                self.changeButtonStateInGame(x1, y1)

    def changeBrushSize(self):
        self.brushSize = self.brushSizeSpinBox.value()
    