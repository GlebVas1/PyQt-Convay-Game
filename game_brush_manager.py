from math import sqrt
import random
from PyQt5 import QtWidgets, QtCore
from functools import partial

import gameObjects as ob

GBM_PREVIEW_SIZE = 7
GBM_PREVIEW_TILE_SIZE = 30
GBM_TILE_PADDING = 5


class BrushManager(object):

    brushSize = 1
    circleBrush = False

    # 1 - brush
    # 2 - object

    currentBrushOption = 1

    brushManagerPreviewFrames = []

    brushCurrentObject = []


    def BrushManagerInitialize(self):
        self.brushSizeSpinBox.valueChanged.connect(self.BrushManagerSetSize)
        self.fillAllCells.clicked.connect(self.changeAllButtonsStateInGame)
        self.brushSetRadioButton.clicked.connect(self.BrushManagerSetOption)

    def paintInPlace(self, x : int, y : int):
        if self.currentBrushOption == 1:
            size = self.brushSize
            if self.brushRandomSize.isChecked():
                size = random.randint(0, 5)

            for i in range(1 - size, size):
                for j in range(1 - size, size):
                
                    if self.brushSetRound.isChecked():
                        if i ** 2 + j ** 2 >= size:
                            continue
                    x1 = (x + i + self.xFieldSize) % self.xFieldSize
                    y1 = (y + j + self.yFieldSize) % self.yFieldSize

                    if self.brushRandomState.isChecked():
                        self.changeButtonState(x1, y1, random.randint(0, self.calc.thisRule.generationsCount))
                    else:
                        self.changeButtonStateInGame(x1, y1)
        else:
            for i in range(GBM_PREVIEW_SIZE):
                for j in range(GBM_PREVIEW_SIZE):
                    x1 = (x + i - GBM_PREVIEW_SIZE // 2 + self.xFieldSize) % self.xFieldSize
                    y1 = (y + j - GBM_PREVIEW_SIZE // 2 + self.yFieldSize) % self.yFieldSize
                    if self.brushCurrentObject[i][j] == 1:
                        self.changeButtonState(x1, y1, self.colorPalleteManagerCurrentBrushState)

    def BrushManagerSetSize(self):
        self.brushSize = self.brushSizeSpinBox.value()

    def BrushManagerSetOption(self):
        self.currentBrushOption = 1 if self.brushSetRadioButton.isChecked() else 2
        
    