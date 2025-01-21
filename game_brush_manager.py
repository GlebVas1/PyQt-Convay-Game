from math import sqrt
import random
from PyQt5 import QtWidgets, QtCore
from functools import partial

import gameObjects as ob

GBM_PREVIEW_SIZE = ob.OBJ_SIZE

GBM_PREVIEW_TILE_SIZE = 30
GBM_TILE_PADDING = 5


class BrushManager(object):
    """Brush manager implements functions of 
       paint/place selected color/object controlled
        by game_color_manager and game_object_manager"""

    # 1 - brush
    # 2 - object

    brushManagerPreviewFrames = []

    brushManagerCurrentObject = []

    def brushManagerInitializeActions(self):
        self.fillAllCells.clicked.connect(self.changeAllButtonsStateInGame)

    def paintInPlace(self, x : int, y : int):
        """Each button on main field activates this function in an appropriate place of the game field"""

        if self.brushSetRadioButton.isChecked():

            size = self.brushSizeSpinBox.value()

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

                    if self.brushManagerCurrentObject[i][j] == 1:
                        self.changeButtonState(x1, y1, self.colorPalleteManagerCurrentBrushState)

    