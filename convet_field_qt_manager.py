from PyQt5 import QtWidgets, QtCore
from functools import partial
import calc as cl


# CFMButtonStyleSheet = "border-radius : 6px;\nborder-width: 2px; \nborder-style : solid;\nborder-color : rgb(255 79, 79);\nborder-bottom: 2px solid rgb(89, 89, 89);\n"
CFMButtonStyleSheet = ""
CFMGameFramePadding = 5
class ConveyFieldQtManager(object):

    xFieldSize = 10
    yFieldSize = 10
    gameButtons = []
    gameButtonsColorsState = ["rgb(49, 49, 49)", "rgb(255, 249, 207)"]
    gameButtonsStates = []

    gameStatePlayed = True
    gameStateFPS = 30

    framesTotalCounter = 0
    alliveCellsCounter = 0

    def initializeManger(self):
        """Initializes some QT events, like timer, basic buttons actions etc"""
        self.updateTimer = QtCore.QTimer(self)
        self.updateTimer.setInterval(500)
        self.updateTimer.timeout.connect(self.updateField)
        self.updateTimer.start()

        self.gameStartStopButton.clicked.connect(self.gameStartStopButtonAction)
        self.comboBox.currentIndexChanged.connect(self.setFPS)

    def InitializeField(self, x: int = 10, y : int = 10):
        """Initialize game field, sizes and calc platform"""
        self.xFieldSize = x
        self.yFieldSize = y
        self.calc = cl.Field()
        self.calc.InitializeField(x, y)
        
    def fillButtons(self):
        """initial filiing main field with buttons"""
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
        """change all buttons to a specific state"""
        for button in self.gameButtons:
            button.setStyleSheet(CFMButtonStyleSheet + "background-color : " + self.gameButtonsColorsState[val]) 
           
        for v in self.gameButtonsStates:
            v = val

        self.calc.field.fill(val)
    
    def changeButtonState(self, x : int, y : int, val : int):
        self.gameButtons[x * self.yFieldSize + y].setStyleSheet(CFMButtonStyleSheet + "background-color : " + self.gameButtonsColorsState[val])
        self.gameButtonsStates[x * self.yFieldSize + y] = val
        self.calc.setCell(x, y, val)

    def updateField(self):
        self.framesTotalCounter += 1
        self.alliveCellsCounter = 0
        self.calc.calcualteFieldStep()
        for x in range(self.xFieldSize):
            for y in range(self.yFieldSize):
                state = self.calc.getState(x, y)
                self.changeButtonState(x, y, state)
                if state == 1:
                    self.alliveCellsCounter += 1
        self.updateLCD()

    def getButtonState(self, x : int, y : int) -> int:
        return self.gameButtonsStates[x * self.yFieldSize + y]
    
    def gameStartStopButtonAction(self):
        if self.gameStatePlayed:
            self.gameStatePlayed = False
            self.updateTimer.stop()
        else:
            self.gameStatePlayed = True
            self.updateTimer.start()

    def setFPS(self, value):
        msToRender = int(1000 / int(self.comboBox.itemText(value)))
        self.updateTimer.setInterval(msToRender)
    
    def updateLCD(self):
        self.totalFramesLCD.display(self.framesTotalCounter)
        self.AliveCellsLCD.display(self.alliveCellsCounter)