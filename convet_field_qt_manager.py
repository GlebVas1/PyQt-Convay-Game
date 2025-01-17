from PyQt5 import QtWidgets, QtCore

from functools import partial

import calc as cl
import colorPalletes as cp
import rules as r

from main_plot_qt_mamger import MainPlotController
from color_pallete_manager import ColorPalleteManager

import pyqtgraph as pg

# CFMButtonStyleSheet = "border-radius : 6px;\nborder-width: 2px; \nborder-style : solid;\nborder-color : rgb(255 79, 79);\nborder-bottom: 2px solid rgb(89, 89, 89);\n"
CFMButtonStyleSheet = ""
CFMGameFramePadding = 5

class ConveyFieldQtManager(MainPlotController, ColorPalleteManager):

    xFieldSize = 10
    yFieldSize = 10
    gameButtons = []
    gameColorPalette = ["rgb(49, 49, 49)", "rgb(255, 249, 207)"]
    gameColorPalleteQt = []
    gameButtonsStates = []

    gameStatePlayed = True
    gameStateFPS = 30

    framesTotalCounter = 0
    alliveCellsCounter = 0

    gameCurrentState = 0
    gamePalleteButtons = []

    mainPlotCurves = []

    def initializeManger(self):
        """Initializes some QT events, like timer, basic buttons actions etc"""
        self.updateTimer = QtCore.QTimer(self)
        self.updateTimer.setInterval(500)
        self.updateTimer.timeout.connect(self.updateField)
        self.updateTimer.start()

        self.gameStartStopButton.clicked.connect(self.gameStartStopButtonAction)
        self.fpsSetter.currentIndexChanged.connect(self.setFPS)

        self.fillAllCells.clicked.connect(self.changeAllButtonsStateInGame)

        

    def initializeField(self, x: int = 10, y : int = 10):
        """Initialize game field, sizes and calc platform"""
        self.xFieldSize = x
        self.yFieldSize = y
        self.calc = cl.Field()
        self.gameColorPalette = cp.greenHexa

        for c in self.gameColorPalette:
            self.gameColorPalleteQt.append(cp.convertColorToQTString(c))

        self.calc.initializeField(x, y, r.starWars)
        self.calc.initializeStatistics()

        self.initializeMainPlot()

        self.initializeColorPallete()

        
        
    def fillButtons(self):
        """initial filiing main field with buttons"""
        xSize = int((self.mainField.size().width() - (1 + self.xFieldSize) * CFMGameFramePadding) / self.xFieldSize)
        ySize = int((self.mainField.size().height() - (1 + self.yFieldSize) * CFMGameFramePadding) / self.yFieldSize)

        newFieldXSize = xSize * self.xFieldSize + CFMGameFramePadding * (1 + self.xFieldSize)
        newFieldYSize = ySize * self.yFieldSize + CFMGameFramePadding * (1 + self.yFieldSize)

        self.mainField.setMinimumSize(QtCore.QSize(newFieldXSize, newFieldYSize))
        self.mainField.setMaximumSize(QtCore.QSize(newFieldXSize, newFieldYSize))
        
        for i in range(0, self.xFieldSize):
            for j in range(0, self.yFieldSize):
                button = QtWidgets.QPushButton(self.mainField)
                button.setGeometry(QtCore.QRect(CFMGameFramePadding + (xSize + CFMGameFramePadding) * i, CFMGameFramePadding + (ySize + CFMGameFramePadding) * j, xSize, ySize))
                button.setObjectName("game_button_" + str(i * self.xFieldSize + j))
                button.setStyleSheet(CFMButtonStyleSheet + "background-color : " + self.gameColorPalleteQt[0])

                button.clicked.connect(partial(self.changeButtonStateInGame, i, j))

                self.gameButtons.append(button)
                self.gameButtonsStates.append(0)

    def changeAllButtons(self, val : int):
        """change all buttons to a specific state"""
        for button in self.gameButtons:
            button.setStyleSheet(CFMButtonStyleSheet + "background-color : " + self.gameColorPalleteQt[val])
           
        for v in self.gameButtonsStates:
            v = val

        self.calc.field.fill(val)
    
    def changeButtonState(self, x : int, y : int, val : int):
        """change one button state"""
        # print(val)
        self.gameButtons[x * self.yFieldSize + y].setStyleSheet(CFMButtonStyleSheet + "background-color : " + self.gameColorPalleteQt[val])
        self.gameButtonsStates[x * self.yFieldSize + y] = val
        self.calc.setCell(x, y, val)

    def changeButtonStateInGame(self, x : int, y : int):
        """change one button state by game parametrs"""
        val = self.gameCurrentState
        self.gameButtons[x * self.yFieldSize + y].setStyleSheet(CFMButtonStyleSheet + "background-color : " + self.gameColorPalleteQt[val])
        self.gameButtonsStates[x * self.yFieldSize + y] = val
        self.calc.setCell(x, y, val)

    def changeAllButtonsStateInGame(self):
        """change all buttons to a specific state by game paramters"""
        val = self.gameCurrentState

        for button in self.gameButtons:
            button.setStyleSheet(CFMButtonStyleSheet + "background-color : " + self.gameColorPalleteQt[val])
           
        for v in self.gameButtonsStates:
            v = val

        self.calc.field.fill(val)

    def updateField(self):
        """recalculate field and update buttons"""
        self.framesTotalCounter += 1
        self.alliveCellsCounter = 0
        self.calc.calcualteFieldStep()
        for x in range(self.xFieldSize):
            for y in range(self.yFieldSize):
                state = self.calc.getState(x, y)
                self.changeButtonState(x, y, state)
                if state == self.calc.thisRule.generationsCount:
                    self.alliveCellsCounter += 1
        
        self.calc.calcStatistic()
        self.alliveCellsCounter = self.calc.statistics[self.calc.thisRule.generationsCount][-1]
        self.updateLCD()

        #if self.framesTotalCounter % 1 == 0:
            #if len(self.calc.statistics[0]) > 6:
                #self.dataPlot.updatePlot(range(len(self.calc.statistics[0])), self.calc.statistics)
        #self.mainPlotView.cla()
        #self.mainPlotView.plot(range(len(self.calc.statistics[0])), self.calc.statistics[0])
        #self.mainPlotView.show()
        self.drawStatistic()

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
        msToRender = int(1000 / int(self.fpsSetter.itemText(value)))
        self.updateTimer.setInterval(msToRender)
    
    def updateLCD(self):
        self.totalFramesLCD.display(self.framesTotalCounter)
        self.AliveCellsLCD.display(self.alliveCellsCounter)        


        
                               


    