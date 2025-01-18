from PyQt5 import QtWidgets, QtCore
import colorPalletes as cp

class SettingsColorPalleteManager(object):

    gameColorPalette = []
    gameColorPalleteQt = []

    settingsColorPalletePreviewFrames = []

    def initializeSettingsColorActions(self):
        self.colorPalleteComboBox.currentIndexChanged.connect(self.changeGamePalletePreview)
        self.colorPalleteApply.clicked.connect(self.applyPreview)

    def initializeSettingsColorPallete(self, colorPallete : list):
        pallete = colorPallete.copy()
        while len(pallete) < self.calc.thisRule.generationsCount + 1:
            pallete.append(pallete[-1])
        self.gameColorPalette = pallete
        self.gameColorPalleteQt = cp.convertPalleteToQT(self.gameColorPalette)

    def initializeSettingsColorPalleteComboBox(self):
        for name, pallete in cp.colorPalletesDict.items():
            self.colorPalleteComboBox.addItem(name)

    def changeGamePalletePreview(self, value):
        name = self.colorPalleteComboBox.itemText(value)
        self.initializeSettingsColorPreview(cp.colorPalletesDict[name])
        
    def initializeSettingsColorPreview(self, colorPallete : list):
        
        colorPalleteQt = cp.convertPalleteToQT(colorPallete)
        for frame in self.settingsColorPalletePreviewFrames:
            frame.setParent(None)
        self.settingsColorPalletePreviewFrames.clear()

        frameXSize = int((self.colorPalletePreview.size().width() - 5 * (len(colorPallete) + 1)) / (len(colorPallete)))
        
        for i in range(len(colorPallete)):
            frame = QtWidgets.QFrame(self.colorPalletePreview)
            frame.setObjectName(str(colorPallete) + str(i))
            frame.setGeometry(QtCore.QRect(5 + (frameXSize + 5) * i, 5, frameXSize, 55))
            frame.setStyleSheet("background-color : " + colorPalleteQt[i])
            frame.show()
            self.settingsColorPalletePreviewFrames.append(frame)
        
        self.colorPalletePreview.show()

    def applyPreview(self):
        name = self.colorPalleteComboBox.currentText()
        pallete = cp.colorPalletesDict[name].copy()
        while len(pallete) < self.calc.thisRule.generationsCount + 1:
            pallete.append(pallete[-1])
        self.initializeSettingsColorPallete(pallete)
        self.initializeColorPallete()
        self.updateFieldColors()
        self.initializeMiniPlot()
        self.initializeMainPlot()



        

    
