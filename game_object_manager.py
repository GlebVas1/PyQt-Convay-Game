from math import sqrt
import random
from PyQt5 import QtWidgets, QtCore
from functools import partial

import gameObjects as ob

GBM_PREVIEW_SIZE = 7
GBM_PREVIEW_TILE_SIZE = 30
GBM_TILE_PADDING = 5

class ObjectManager(object):
    def objectManagerInitializeActions(self):
        self.objectSetRadioButton.clicked.connect(self.setBrushOption)
        self.objectsPresets.currentIndexChanged.connect(self.objectManagerSetToPreview)

    def objectManagerInitializeComboBox(self):
        for name, pallete in ob.objectsDict.items():
            self.objectsPresets.addItem(name)

    def objectManagerInitializePreview(self, object : list):
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
        
        self.objectManagerUpdateObjectToPreview()

    def objectManagerSetToPreview(self):
        self.brushCurrentObject = ob.objectsDict[self.objectsPresets.currentText()].copy()
        print(self.objectsPresets.currentText())
        self.objectManagerUpdateObjectToPreview()

    def objectManagerUpdateObjectToPreview(self):
        for i in range(GBM_PREVIEW_SIZE):
            for j in range(GBM_PREVIEW_SIZE):
                if self.brushCurrentObject[i][j] == 1:
                    self.brushManagerPreviewFrames[i * GBM_PREVIEW_SIZE + j].setStyleSheet("background-color : " + self.gameColorPalleteQt[self.colorPalleteManagerCurrentBrushState])
                else:
                    self.brushManagerPreviewFrames[i * GBM_PREVIEW_SIZE + j].setStyleSheet("background-color : rgb(49, 49, 49)")

