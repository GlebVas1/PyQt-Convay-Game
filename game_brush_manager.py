from math import sqrt
import random
from PyQt5 import QtWidgets, QtCore
from functools import partial

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

    def initializeObjectPreview(self, object : list):
        self.brushCurrentObject = object.copy()

        for frame in self.brushManagerPreviewFrames:
            frame.setParent(None)

        for i in range(5):
            for j in range(5):
                frame = QtWidgets.QFrame(self.objectPreview)
                frame.setObjectName(str("objectPrewiewSet") + str(i * 5 + j))
                frame.setGeometry(QtCore.QRect(5 + (22 + 5) * i, 5 + (22 + 5) * j, 22, 22))
                frame.setStyleSheet("background-color : " + self.gameColorPalleteQt[0])
                self.brushManagerPreviewFrames.append(frame)
                frame.show()
        
        self.updateObjectPreview()

    def updateObjectPreview(self):
        for i in range(5):
            for j in range(5):
                if self.brushCurrentObject[i][j] == 1:
                    self.brushManagerPreviewFrames[i * 5 + j].setStyleSheet("background-color : " + self.gameColorPalleteQt[self.currentBrushState])



    def paintInPlace(self, x : int, y : int):
        if self.currentBrushOption == 1:
            size = self.brushSize
            if self.brushRandomSize.isChecked():
                size = random.randint(0, 5)

            for i in range(1 - size, size):
                for j in range(1 - size, size):
                
                    if self.brushSetRound.isChecked():
                        if i ** 2 + j ** 2 >= size ** 2:
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
                    x1 = (x + i - 2 + self.xFieldSize) % self.xFieldSize
                    y1 = (y + j - 2 + self.yFieldSize) % self.yFieldSize
                    if self.brushCurrentObject[i][j] == 1:
                        self.changeButtonState(x1, y1, self.currentBrushState)
                
                    

    def changeBrushSize(self):
        self.brushSize = self.brushSizeSpinBox.value()

    def setBrushOption(self):
        self.currentBrushOption = 1 if self.brushSetRadioButton.isChecked() else 2
        
    