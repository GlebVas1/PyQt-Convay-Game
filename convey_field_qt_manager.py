from PyQt5 import QtWidgets, QtCore

from functools import partial

import calc as cl
import colorPalletes as cp
import gameObjects as ob
import rules as ru

from game_brush_manager import BrushManager
from game_color_pallete_manager import ColorPalleteManager
from game_object_manager import ObjectManager
from game_random_manager import RandomManager

from main_plot_qt_manager import MainPlotController
from mini_plot_manager import MiniPlotManager

from stop_start_manager import StopStartManager
from settings_color_pallete import SettingsColorPalleteManager
from settings_field_size import SettingsFieldSize
from settings_rule import SettingsRuleManager

# CFMButtonStyleSheet = "border-radius : 6px;\nborder-width: 2px; \nborder-style : solid;\nborder-color : rgb(255 79, 79);\nborder-bottom: 2px solid rgb(89, 89, 89);\n"
CFMButtonStyleSheet = ""
CFMGameFramePadding = 5 

class ConveyFieldQtManager(BrushManager,
                           ColorPalleteManager,
                           MainPlotController,
                           MiniPlotManager,
                           ObjectManager,
                           RandomManager,
                           SettingsColorPalleteManager, 
                           SettingsFieldSize,
                           SettingsRuleManager,
                           StopStartManager):

    xFieldSize = 10
    yFieldSize = 10

    gameButtons = []
    
    gameButtonsStates = []

    framesTotalCounter = 0
    alliveCellsCounter = 0

    def ConveyFieldQtManagerInitializeActions(self):
        """Initializes some QT events, like timer, basic buttons actions etc"""
        self.updateTimer = QtCore.QTimer(self)
        self.updateTimer.setInterval(500)
        self.updateTimer.timeout.connect(self.conveyFieldQtManagerUpdateField)
        self.updateTimer.start()

        self.fpsSetter.currentIndexChanged.connect(self.conveyFieldQtManagerSetFPS)
        self.settingsWindowFixedSize.clicked.connect(self.windowFixedSizeMode)
        

    def ConveyFieldQtManagerInitializeManager(
            self, xSize: int = 10,
            ySize : int = 10, 
            rule : ru.Rule = ru.defaultLife, 
            colorPallete : list = cp.defaultBinary, 
            brushObject : list = ob.glider
            ):
        """
        Initialize game field, sizes and calc platform, and other actions\n
        Contains so many lines because of dependanses between initializations of different objects"""
        self.xFieldSize = xSize
        self.yFieldSize = ySize

        self.calc = cl.Field()  

        self.settingsRuleInitializeActions()
        self.settingsRuleInitializeFrame()
        self.settingsRuleInitializeComboBox()
        self.settingsRuleInitializeManager(rule)
        self.settingsRuleMakePreview(rule)

        # must be initialized after to make correct intialization after intializing rules
        self.calc.initializeField(xSize, ySize)
        self.calc.initializeStatistics()


        self.settingsFieldSizeInititalizeActions()

        self.settingsColorInitializeActions()
        self.settingsColorPalleteInitializeComboBox()
        self.settingsColorPalleteInitialize(colorPallete)
        self.settingsColorPalleteInitializePreview(colorPallete)

        self.mainPlotInitializeActions()
        self.mainPlotInitialize()
        self.miniPlotInitialize()

        self.colorPalleteManagerInitialize()

        self.brushManagerInitializeActions()

        self.objectManagerInitializeActions()
        self.objectManagerInitializeComboBox()
        self.objectManagerInitializePreview(brushObject)

        self.randomManagerInitializeStructuresList()

        self.stopStartManagerInitializeActions()

        self.conveyFieldQtManageInitializeButtons()

    def conveyFieldQtManageInitializeButtons(self):
        """initial filiing main field with buttons, also is used to reinitilize field"""

        for button in self.gameButtons:
            button.setParent(None)

        self.gameButtonsStates.clear()
        self.gameButtons.clear()

        xSize = int((self.mainField.size().width() - (1 + self.xFieldSize) * CFMGameFramePadding) / self.xFieldSize)
        ySize = int((self.mainField.size().height() - (1 + self.yFieldSize) * CFMGameFramePadding) / self.yFieldSize)

        # Need to resize the main game field to have appropriate borders 
        
        newFieldFrameWidgetXSize = xSize * self.xFieldSize + CFMGameFramePadding * (1 + self.xFieldSize)
        newFieldFrameWidgetYSize = ySize * self.yFieldSize + CFMGameFramePadding * (1 + self.yFieldSize)

        self.mainField.setMinimumSize(QtCore.QSize(newFieldFrameWidgetXSize, newFieldFrameWidgetYSize))
        self.mainField.setMaximumSize(QtCore.QSize(newFieldFrameWidgetXSize, newFieldFrameWidgetYSize))
        
        for i in range(0, self.xFieldSize):
            for j in range(0, self.yFieldSize):
                button = QtWidgets.QPushButton(self.mainField)
                button.setGeometry(QtCore.QRect(CFMGameFramePadding + (xSize + CFMGameFramePadding) * i, CFMGameFramePadding + (ySize + CFMGameFramePadding) * j, xSize, ySize))
                button.setObjectName("game_button_" + str(i * self.xFieldSize + j))

                button.clicked.connect(partial(self.paintInPlace, i, j))

                self.gameButtons.append(button)
                self.gameButtonsStates.append(0)

        self.conveyFieldQtManagerUpdateFieldColors()
        
    
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

    def conveyFieldQtManagerUpdateFieldColors(self):
        """Called on pallete/rule change in order to update appropriate colors"""
        for x in range(self.xFieldSize):
            for y in range(self.yFieldSize):
                state = self.calc.getState(x, y)
                self.changeButtonState(x, y, state)

    def conveyFieldQtManagerUpdateField(self):
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
        self.conveyFieldQtManagerUpdateLCD()

        if self.framesTotalCounter % self.plotsUpdateFramesRate.value() == 0:
            self.mainPlotDrawStatistic()
            self.miniPlotDrawStatistic()

    def conveyFieldQtManagerSetFPS(self, value):
        msToRender = int(1000 / int(self.fpsSetter.itemText(value)))
        self.updateTimer.setInterval(msToRender)
    
    def conveyFieldQtManagerUpdateLCD(self):
        self.totalFramesLCD.display(self.framesTotalCounter)
        self.AliveCellsLCD.display(self.alliveCellsCounter)        

    def conveyFieldQtManagerSyncChanges(self):
        self.settingsColorPalleteApplyPreview()
        self.colorPalleteManagerInitialize()
        self.objectManagerUpdateObjectInPreview()
        self.conveyFieldQtManagerUpdateFieldColors()
        self.miniPlotInitialize()
        self.mainPlotInitialize()
    
    def windowFixedSizeMode(self):
        pass

        
                               


    