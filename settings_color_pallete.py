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
        pallete = self.convertPalleteToSize(colorPallete.copy(), self.calc.thisRule.generationsCount + 1)
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
        pallete = self.convertPalleteToSize(cp.colorPalletesDict[name].copy(), self.calc.thisRule.generationsCount + 1)
        self.initializeSettingsColorPallete(pallete)
        self.initializeColorPallete()
        self.updateFieldColors()
        self.initializeMiniPlot()
        self.initializeMainPlot()


    def convertPalleteToSize(self, pallete : list, size : int) -> list:
        if len(pallete) > size:
            
            pallete_truncated = []
            if size == 2:
                pallete_truncated.append(pallete[0])
                pallete_truncated.append(pallete[-1])
                return pallete_truncated.copy()
            step = (len(pallete) - 2) // (size - 2)
            pallete_truncated.append(pallete[0])
            for i in range(size - 2):
                pallete_truncated.append(pallete[1 + step * i])
            pallete_truncated.append(pallete[-1])
            return pallete_truncated.copy()
        
        if len(pallete) == size: 
            return pallete.copy()
        
        if len(pallete) < size:
            pallete_extended = []
            colorCount = len(pallete)
            needToFillForEachColor = (size - colorCount) // (colorCount - 1)
            # if colorCount + needToFillForEachColor < size:
            #     needToFillForEachColor += 1
            for i in range(colorCount - 2):
                if len(pallete_extended) >= size - 1:
                    break
                pallete_extended.append(pallete[i])
                for j in range(needToFillForEachColor):
                    r = (pallete[i + 1][0] * (j + 1) + pallete[i][0] * (needToFillForEachColor - j)) // (needToFillForEachColor + 1)
                    g = (pallete[i + 1][1] * (j + 1) + pallete[i][1] * (needToFillForEachColor - j)) // (needToFillForEachColor + 1)
                    b = (pallete[i + 1][2] * (j + 1) + pallete[i][2] * (needToFillForEachColor - j)) // (needToFillForEachColor + 1)
                    r = min(255, r)
                    g = min(255, g)
                    b = min(255, b)
                    pallete_extended.append((r, g, b))

            pallete_extended.append(pallete[-2])
            for j in range(size - len(pallete_extended) - 1):
                r = (pallete[-1][0] * (j + 1) + pallete[-2][0] * (needToFillForEachColor - j)) // (needToFillForEachColor + 1)
                g = (pallete[-1][1] * (j + 1) + pallete[-2][1] * (needToFillForEachColor - j)) // (needToFillForEachColor + 1)
                b = (pallete[-1][2] * (j + 1) + pallete[-2][2] * (needToFillForEachColor - j)) // (needToFillForEachColor + 1)
                r = min(255, r)
                g = min(255, g)
                b = min(255, b)
                pallete_extended.append((r, g, b))
            
            pallete_extended.append(pallete[-1])
            print("Requested")
            print(size)
            print("Real")
            print(len(pallete_extended))
            return pallete_extended.copy()
