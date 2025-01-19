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

    currentBrushState = 0

    # 1 - brush
    # 2 - object

    currentBrushOption = 1

    brushManagerPreviewFrames = []

    brushCurrentObject = []


    def initializeBrushManager(self):
        self.brushSizeSpinBox.valueChanged.connect(self.changeBrushSize)
        self.fillAllCells.clicked.connect(self.changeAllButtonsStateInGame)
        self.brushSetRadioButton.clicked.connect(self.setBrushOption)
        self.objectSetRadioButton.clicked.connect(self.setBrushOption)
        self.objectsPresets.currentIndexChanged.connect(self.setNewObjectToPreview)

    def initializeObjectComboBox(self):
        for name, pallete in ob.objectsDict.items():
            self.objectsPresets.addItem(name)

    def initializeObjectPreview(self, object : list):
        self.brushCurrentObject = object.copy()

        for frame in self.brushManagerPreviewFrames:
            frame.setParent(None)

        for i in range(GBM_PREVIEW_SIZE):
            for j in range(GBM_PREVIEW_SIZE):
                frame = QtWidgets.QFrame(self.objectPreview)
                frame.setObjectName(str("objectPrewiewSet") + str(i * GBM_PREVIEW_SIZE + j))
                frame.setGeometry(QtCore.QRect(GBM_TILE_PADDING + (GBM_PREVIEW_TILE_SIZE + GBM_TILE_PADDING) * i, GBM_TILE_PADDING + (GBM_PREVIEW_TILE_SIZE + GBM_TILE_PADDING) * j, GBM_PREVIEW_TILE_SIZE, GBM_PREVIEW_TILE_SIZE))
                frame.setStyleSheet("background-color : " + self.gameColorPalleteQt[0])
                self.brushManagerPreviewFrames.append(frame)
                frame.show()
        
        self.updateObjectPreview()

    def setNewObjectToPreview(self):
        self.brushCurrentObject = ob.objectsDict[self.objectsPresets.currentText()].copy()
        print(self.objectsPresets.currentText())
        self.updateObjectPreview()

    def updateObjectPreview(self):
        print(self.brushCurrentObject)
        for i in range(GBM_PREVIEW_SIZE):
            for j in range(GBM_PREVIEW_SIZE):
                if self.brushCurrentObject[i][j] == 1:
                    self.brushManagerPreviewFrames[i * GBM_PREVIEW_SIZE + j].setStyleSheet("background-color : " + self.gameColorPalleteQt[self.currentBrushState])
                else:
                    self.brushManagerPreviewFrames[i * GBM_PREVIEW_SIZE + j].setStyleSheet("background-color : rgb(49, 49, 49)")



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
            for i in range(5):
                for j in range(5):
                    x1 = (x + i - GBM_PREVIEW_SIZE // 2 + self.xFieldSize) % self.xFieldSize
                    y1 = (y + j - GBM_PREVIEW_SIZE // 2 + self.yFieldSize) % self.yFieldSize
                    if self.brushCurrentObject[i][j] == 1:
                        self.changeButtonState(x1, y1, self.currentBrushState)
                
                    

    def changeBrushSize(self):
        self.brushSize = self.brushSizeSpinBox.value()

    def setBrushOption(self):
        self.currentBrushOption = 1 if self.brushSetRadioButton.isChecked() else 2
        
    