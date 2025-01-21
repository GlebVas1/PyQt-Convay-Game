from PyQt5 import QtWidgets, QtCore

from functools import partial

import calc as cl
import colorPalletes as cp
import rules as ru
import gameObjects as ob

from main_plot_qt_manager import MainPlotController
from game_color_pallete_manager import ColorPalleteManager
from mini_plot_manager import MiniPlotManager
from game_brush_manager import BrushManager
from stop_start_manager import StopStartManager
from settings_color_pallete import SettingsColorPalleteManager
from settings_rule import settingsRuleManager
from settings_field_size import SettingsFieldSize
from game_object_manager import ObjectManager
from game_random_manager import RandomManager

import pyqtgraph as pg

# CFMButtonStyleSheet = "border-radius : 6px;\nborder-width: 2px; \nborder-style : solid;\nborder-color : rgb(255 79, 79);\nborder-bottom: 2px solid rgb(89, 89, 89);\n"
CFMButtonStyleSheet = ""
CFMGameFramePadding = 5

class ConveyFieldQtManager(MainPlotController, 
                           ColorPalleteManager, 
                           MiniPlotManager, 
                           BrushManager, 
                           StopStartManager, 
                           SettingsColorPalleteManager, 
                           settingsRuleManager,
                           ObjectManager,
                           RandomManager,
                           SettingsFieldSize):

    xFieldSize = 10
    yFieldSize = 10

    gameButtons = []
    
    gameButtonsStates = []

    gameStateFPS = 30

    framesTotalCounter = 0
    alliveCellsCounter = 0

    def initializeManger(self):
        """Initializes some QT events, like timer, basic buttons actions etc"""
        self.updateTimer = QtCore.QTimer(self)
        self.updateTimer.setInterval(500)
        self.updateTimer.timeout.connect(self.updateField)
        self.updateTimer.start()

        self.fpsSetter.currentIndexChanged.connect(self.setFPS)
        self.settingsWindowFixedSize.clicked.connect(self.windowFixedSizeMode)
        

    def initializeField(self, x: int = 10, y : int = 10):
        """Initialize game field, sizes and calc platform"""
        self.xFieldSize = x
        self.yFieldSize = y

        self.calc = cl.Field()

        self.settingsRuleInitializeActions()
        self.settingsRuleInitializeFrame()
        self.settingsRuleInitializeComboBox()
        self.settingsRuleInitializeManager(ru.defaultLife)
        self.settingsRuleMakePreview(ru.defaultLife)

        self.calc.initializeField(x, y)
        self.calc.initializeStatistics()

        self.SettingsFieldSizeInititalizeActions()

        self.settingsColorInitializeActions()
        self.settingsColorPalleteInitializeComboBox()
        self.settingsColorPalleteInitialize(cp.defaultBinary)
        self.settingsColorPalleteInitializePreview(cp.defaultBinary)

        self.mainPlotInitializeActions()
        self.mainPlotInitialize()
        self.miniPlotInitialize()

        self.colorPalleteManagerInitialize()

        self.BrushManagerInitialize()

        self.objectManagerInitializeActions()
        self.objectManagerInitializeComboBox()
        self.objectManagerInitializePreview(ob.glider)

        self.randomManagerInitializeStructuresList()

        self.stopStartManagerInitializeActions()

        
        
    def initializeGameFieldFillButtons(self):
        """initial filiing main field with buttons"""

        for button in self.gameButtons:
            button.setParent(None)

        self.gameButtonsStates.clear()
        self.gameButtons.clear()


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

                button.clicked.connect(partial(self.paintInPlace, i, j))

                self.gameButtons.append(button)
                self.gameButtonsStates.append(0)

        self.updateFieldColors()
        
    
    def changeAllButtons(self, val : int):
        """change all buttons to a specific state"""
        for button in self.gameButtons:
            button.setStyleSheet(CFMButtonStyleSheet + "background-color : " + self.gameColorPalleteQt[val])
           
        for v in self.gameButtonsStates:
            v = val

        self.calc.field.fill(val)
    
    def changeButtonState(self, x : int, y : int, val : int):
        """change one button state"""
        self.gameButtons[x * self.yFieldSize + y].setStyleSheet(CFMButtonStyleSheet + "background-color : " + self.gameColorPalleteQt[val])
        self.gameButtonsStates[x * self.yFieldSize + y] = val
        self.calc.setCell(x, y, val)

    def changeButtonStateInGame(self, x : int, y : int):
        """change one button state by game parametrs"""
        self.changeButtonState(x, y, self.colorPalleteManagerCurrentBrushState)

    def changeAllButtonsStateInGame(self):
        """change all buttons to a specific state by game paramters"""
        self.changeAllButtons(self.colorPalleteManagerCurrentBrushState)

    def updateFieldColors(self):
        for x in range(self.xFieldSize):
            for y in range(self.yFieldSize):
                state = self.calc.getState(x, y)
                self.changeButtonState(x, y, state)
    


    def updateField(self):
        """recalculate field and update buttons"""
        self.framesTotalCounter += 1
        self.alliveCellsCounter = 0

        self.calc.calcualteFieldStep()

        if self.framesTotalCounter % self.randomOnEachFrameRate.value() == 0:
            self.randomManagerAddRandomCells()
        
        if self.framesTotalCounter % (int(self.skipFrameSetter.currentText()) + 1) == 0:
            for x in range(self.xFieldSize):
                for y in range(self.yFieldSize):
                    state = self.calc.getState(x, y)
                    self.changeButtonState(x, y, state)
                    if state == self.calc.thisRule.generationsCount:
                        self.alliveCellsCounter += 1
        
        self.calc.calcStatistic()
        self.alliveCellsCounter = self.calc.statistics[self.calc.thisRule.generationsCount][-1]
        self.updateLCD()

        if self.framesTotalCounter % self.plotsUpdateFramesRate.value() == 0:
            self.mainPlotDrawStatistic()
            self.miniPlotDrawStatistic()

    def getButtonState(self, x : int, y : int) -> int:
        return self.gameButtonsStates[x * self.yFieldSize + y]

    def setFPS(self, value):
        msToRender = int(1000 / int(self.fpsSetter.itemText(value)))
        self.updateTimer.setInterval(msToRender)
    
    def updateLCD(self):
        self.totalFramesLCD.display(self.framesTotalCounter)
        self.AliveCellsLCD.display(self.alliveCellsCounter)        

    def gameManagerSyncChanges(self):
        self.settingsColorPalleteApplyPreview()
        self.colorPalleteManagerInitialize()
        self.objectManagerUpdateObjectToPreview()
        self.updateFieldColors()
        self.miniPlotInitialize()
        self.mainPlotInitialize()
    
    def windowFixedSizeMode(self):
        pass

        
                               


    