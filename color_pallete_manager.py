from PyQt5 import QtWidgets, QtCore
from functools import partial


class ColorPalleteManager(object):
    
    gamePalleteButtons = []

    def initializeColorPallete(self):

        for button in self.gamePalleteButtons:
            button.setParent(None)
        
        self.gamePalleteButtons.clear()

        for i in range(self.calc.thisRule.generationsCount + 1):
            button = QtWidgets.QPushButton(self.colorPallete)
            button.setGeometry(QtCore.QRect(10, 10 + (60 + 10) * i, 60, 60))
            button.setObjectName("game_pallete_button_" + str(i))
            button.setStyleSheet("background-color : " + self.gameColorPalleteQt[i])

            button.clicked.connect(partial(self.palleteButtonSetState, i))
            button.show()
            self.gamePalleteButtons.append(button)
            self.colorPallete.setMaximumSize(QtCore.QSize(80, (self.calc.thisRule.generationsCount + 2) * 10 + (self.calc.thisRule.generationsCount + 1) * 60))

        self.selectedColorPanel.setStyleSheet("background-color : " + self.gameColorPalleteQt[self.currentBrushState])
    
    def palleteButtonSetState(self, val : int):
        self.currentBrushState = val
        self.selectedColorPanel.setStyleSheet("background-color : " + self.gameColorPalleteQt[val])

    

        

        