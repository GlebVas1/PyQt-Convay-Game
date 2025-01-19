from PyQt5 import QtWidgets, QtCore
from functools import partial


class ColorPalleteManager(object):
    
    gamePalleteButtons = []

    def initializeColorPallete(self):

        for button in self.gamePalleteButtons:
            button.setParent(None)
        
        self.gamePalleteButtons.clear()

        currentColumns = 0

        for i in range(self.calc.thisRule.generationsCount + 1):
            if i > 0 and i % 8 == 0:
                currentColumns += 1
            xCoord = 10 * (currentColumns + 1) + 60 * currentColumns
            yCoord = 10 + (60 + 10) * (i % 8)
            button = QtWidgets.QPushButton(self.colorPallete)
            button.setGeometry(QtCore.QRect(xCoord, yCoord, 60, 60))
            button.setObjectName("game_pallete_button_" + str(i))
            button.setStyleSheet("background-color : " + self.gameColorPalleteQt[i])

            button.clicked.connect(partial(self.palleteButtonSetState, i))
            button.show()
            self.gamePalleteButtons.append(button)

        self.colorPallete.setMaximumSize(QtCore.QSize(10 * (currentColumns + 2)  + 60 * (currentColumns + 1), (self.thisRule.generationsCount + 2) * 10 + (self.thisRule.generationsCount + 1) * 60))
        self.colorPallete.setMinimumSize(QtCore.QSize(10 * (currentColumns + 2)  + 60 * (currentColumns + 1), (self.thisRule.generationsCount + 2) * 10 + (self.thisRule.generationsCount + 1) * 60))

        self.currentBrushState = min(self.currentBrushState,self.thisRule.generationsCount)
        self.selectedColorPanel.setStyleSheet("background-color : " + self.gameColorPalleteQt[self.currentBrushState])
    
    def palleteButtonSetState(self, val : int):
        self.currentBrushState = val
        self.updateObjectPreview()
        self.selectedColorPanel.setStyleSheet("background-color : " + self.gameColorPalleteQt[val])

    

        

        