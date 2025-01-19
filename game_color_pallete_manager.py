from PyQt5 import QtWidgets, QtCore
from functools import partial

CPM_COLUMN_SIZE = 5
CPM_TILE_SIZE = 60
CPM_PADDING_SIZE = 10

class ColorPalleteManager(object):
    
    colorPalleteManagerPalleteButtons = []
    colorPalleteManagerCurrentBrushState = 0

    def colorPalleteManagerInitialize(self):

        for button in self.colorPalleteManagerPalleteButtons:
            button.setParent(None)
        
        self.colorPalleteManagerPalleteButtons.clear()

        currentColumns = 0

        for i in range(self.thisRule.generationsCount + 1):
            if i > 0 and i % CPM_COLUMN_SIZE == 0:
                currentColumns += 1
            xCoord = CPM_PADDING_SIZE * (currentColumns + 1) + CPM_TILE_SIZE * currentColumns
            yCoord = CPM_PADDING_SIZE + (CPM_TILE_SIZE + CPM_PADDING_SIZE) * (i % CPM_COLUMN_SIZE)
            button = QtWidgets.QPushButton(self.colorPallete)
            button.setGeometry(QtCore.QRect(xCoord, yCoord, CPM_TILE_SIZE, CPM_TILE_SIZE))
            button.setObjectName("game_pallete_button_" + str(i))
            button.setStyleSheet("background-color : " + self.gameColorPalleteQt[i])

            button.clicked.connect(partial(self.colorPalleteManagerSetState, i))
            button.show()
            self.colorPalleteManagerPalleteButtons.append(button)

        realYCellsCount = min(CPM_COLUMN_SIZE, self.thisRule.generationsCount + 1)

        self.colorPallete.setMaximumSize(QtCore.QSize(CPM_PADDING_SIZE * (currentColumns + 2)  + CPM_TILE_SIZE * (currentColumns + 1), (realYCellsCount + 1) * CPM_PADDING_SIZE + (realYCellsCount) * CPM_TILE_SIZE))
        self.colorPallete.setMinimumSize(QtCore.QSize(CPM_PADDING_SIZE * (currentColumns + 2)  + CPM_TILE_SIZE * (currentColumns + 1), (realYCellsCount + 1) * CPM_PADDING_SIZE + (realYCellsCount) * CPM_TILE_SIZE))

        self.currentBrushState = min(self.currentBrushState,self.thisRule.generationsCount)
        self.selectedColorPanel.setStyleSheet("background-color : " + self.gameColorPalleteQt[self.currentBrushState])
    
    def colorPalleteManagerSetState(self, val : int):
        self.currentBrushState = val
        self.objectManagerUpdateObjectToPreview()
        self.selectedColorPanel.setStyleSheet("background-color : " + self.gameColorPalleteQt[val])

    

        

        