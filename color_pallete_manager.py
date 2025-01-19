from PyQt5 import QtWidgets, QtCore
from functools import partial

CPM_COLUMN_SIZE = 6
class ColorPalleteManager(object):
    
    gamePalleteButtons = []

    def initializeColorPallete(self):

        for button in self.gamePalleteButtons:
            button.setParent(None)
        
        self.gamePalleteButtons.clear()

        currentColumns = 0

        for i in range(self.thisRule.generationsCount + 1):
            if i > 0 and i % 6 == 0:
                currentColumns += 1
            xCoord = 10 * (currentColumns + 1) + 60 * currentColumns
            yCoord = 10 + (60 + 10) * (i % 5)
            button = QtWidgets.QPushButton(self.colorPallete)
            button.setGeometry(QtCore.QRect(xCoord, yCoord, 60, 60))
            button.setObjectName("game_pallete_button_" + str(i))
            button.setStyleSheet("background-color : " + self.gameColorPalleteQt[i])

            button.clicked.connect(partial(self.palleteButtonSetState, i))
            button.show()
            self.gamePalleteButtons.append(button)

        realYCellsCount = min(CPM_COLUMN_SIZE, self.thisRule.generationsCount + 1)
        self.colorPallete.setMaximumSize(QtCore.QSize(10 * (currentColumns + 2)  + 60 * (currentColumns + 1), (CPM_COLUMN_SIZE + 2) * 10 + (CPM_COLUMN_SIZE + 1) * 60))
        self.colorPallete.setMinimumSize(QtCore.QSize(10 * (currentColumns + 2)  + 60 * (currentColumns + 1), (realYCellsCount + 2) * 10 + (realYCellsCount + 1) * 60))

        self.currentBrushState = min(self.currentBrushState,self.thisRule.generationsCount)
        self.selectedColorPanel.setStyleSheet("background-color : " + self.gameColorPalleteQt[self.currentBrushState])
    
    def palleteButtonSetState(self, val : int):
        self.currentBrushState = val
        self.updateObjectPreview()
        self.selectedColorPanel.setStyleSheet("background-color : " + self.gameColorPalleteQt[val])

    

        

        