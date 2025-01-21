from PyQt5 import QtWidgets, QtCore

import gameObjects as ob

import copy

GBM_PREVIEW_SIZE = 7
GBM_PREVIEW_TILE_SIZE = 30
GBM_TILE_PADDING = 5

class ObjectManager(object):
    """Class that implements the control over object that will be placed"""

    def objectManagerInitializeActions(self):
        self.objectsPresets.currentIndexChanged.connect(self.objectManagerSetToPreview)
        self.objectInvertButton.clicked.connect(self.objectManagerInvertObject)
        self.objectFlipButton.clicked.connect(self.objectManagerFlipObject)
        self.objectRotateButton.clicked.connect(self.objectManagerRotateClockwiseObject)

    def objectManagerInitializeComboBox(self):
        for name, pallete in ob.objectsDict.items():
            self.objectsPresets.addItem(name)

    def objectManagerInitializePreview(self, object : list):
        self.brushManagerCurrentObject = copy.deepcopy(object)
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
        
        self.objectManagerUpdateObjectInPreview()

    def objectManagerSetToPreview(self):
        self.brushManagerCurrentObject = copy.deepcopy(ob.objectsDict[self.objectsPresets.currentText()])
        self.objectManagerUpdateObjectInPreview()

    def objectManagerUpdateObjectInPreview(self):
        for i in range(GBM_PREVIEW_SIZE):
            for j in range(GBM_PREVIEW_SIZE):
                if self.brushManagerCurrentObject[i][j] == 1:
                    self.brushManagerPreviewFrames[i * GBM_PREVIEW_SIZE + j].setStyleSheet("background-color : " + self.gameColorPalleteQt[self.colorPalleteManagerCurrentBrushState])
                else:
                    self.brushManagerPreviewFrames[i * GBM_PREVIEW_SIZE + j].setStyleSheet("background-color : rgb(49, 49, 49)")

    def objectManagerInvertObject(self):
        for i in range(GBM_PREVIEW_SIZE):
            for j in range(GBM_PREVIEW_SIZE):
                self.brushManagerCurrentObject[i][j] = 1 - self.brushManagerCurrentObject[i][j]

        self.objectManagerUpdateObjectInPreview()

    def objectManagerRotateClockwiseObject(self):
        new_object = copy.deepcopy(self.brushManagerCurrentObject)
        for i in range(GBM_PREVIEW_SIZE):
            for j in range(GBM_PREVIEW_SIZE):
                new_object[i][j] = self.brushManagerCurrentObject[j][GBM_PREVIEW_SIZE - 1 - i]

        self.brushManagerCurrentObject = new_object.copy()
        self.objectManagerUpdateObjectInPreview()

    def objectManagerFlipObject(self):
        new_object = copy.deepcopy(self.brushManagerCurrentObject)
        for i in range(GBM_PREVIEW_SIZE):
            for j in range(GBM_PREVIEW_SIZE):
                new_object[i][j] = self.brushManagerCurrentObject[GBM_PREVIEW_SIZE - 1 - i][j]

        self.brushManagerCurrentObject = new_object.copy()
        self.objectManagerUpdateObjectInPreview()



