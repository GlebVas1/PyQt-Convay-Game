from PyQt5 import QtWidgets, QtCore
from functools import partial
import calc as cl


CFMButtonStyleSheet = "border-radius : 10px;\nborder-width: 3px; \nborder-style : solid;\nborder-color  : rgb(89, 89, 89);\nborder-bottom: 4px solid black;\n"
CFMGameFramePadding = 5
class ConveyFieldQtManager(object):

    xFieldSize = 10
    yFieldSize = 10
    gameButtons = []
    gameButtonsColorsState = ["rgb(49, 49, 49)", "rgb(255, 249, 207)"]
    gameButtonsStates = []

    def update(self):
        print("updated")

    def InitializeField(self, x: int = 10, y : int = 10):
        self.xFieldSize = x
        self.yFieldSize = y
        self.calc = cl.Field()
        self.calc.InitializeField(x, y)
        self.updateButton.clicked.connect(partial(self.update))

    def fillButtons(self):
        xSize = int((self.mainField.size().width() - (1 + self.xFieldSize) * CFMGameFramePadding) / self.xFieldSize)
        ySize = int((self.mainField.size().height() - (1 + self.yFieldSize) * CFMGameFramePadding) / self.yFieldSize)

        for i in range(0, self.xFieldSize):
            for j in range(0, self.yFieldSize):
                button = QtWidgets.QPushButton(self.mainField)
                button.setGeometry(QtCore.QRect(CFMGameFramePadding + (xSize + CFMGameFramePadding) * i, CFMGameFramePadding + (ySize + CFMGameFramePadding) * j, xSize, ySize))
                button.setObjectName("game_button_" + str(i * self.xFieldSize + j))
                button.setStyleSheet(CFMButtonStyleSheet + "background-color : " + self.gameButtonsColorsState[0])

                button.clicked.connect(partial(self.changeButtonState, i, j, 1))

                self.gameButtons.append(button)
                self.gameButtonsStates.append(0)

    def changeAllButtons(self, val : int):
        # for button in self.gameButtons:
        #     button.setStyleSheet("background-color : " + self.gameButtonsColorsState[val]) 
        for i in range(0, self.xFieldSize):
            for j in range(0, self.yFieldSize):
                print(i * self.xFieldSize + j)
                print(self.gameButtonsColorsState[val])
                self.gameButtons[i * self.yFieldSize + j].setStyleSheet(CFMButtonStyleSheet + "background-color : " + self.gameButtonsColorsState[val])
                
        for v in self.gameButtonsStates:
            v = val
    
    def changeButtonState(self, x : int, y : int, val : int):
        print(str(x) + "  " + str(y) + " changed to " + str(val))
        self.gameButtons[x * self.yFieldSize + y].setStyleSheet(CFMButtonStyleSheet + "background-color : " + self.gameButtonsColorsState[val])
        self.gameButtonsStates[x * self.yFieldSize + y] = val
        self.calc.setCell(x, y, val)

    
        # self.calc.calcualteFieldStep()
        
        # for x in range(self.xFieldSize):
        #     for y in range(self.yFieldSize):
        #         self.changeButtonState(self.calc.getState(x, y))

    def getButtonState(self, x : int, y : int) -> int:
        return self.gameButtonsStates[x * self.yFieldSize + y]
    
