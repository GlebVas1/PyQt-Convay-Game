import copy
from PyQt5 import QtWidgets, QtGui, QtCore

import random
import gameObjects as ob

class RandomManager(object):

    randomManagerCheckBoxes = {}
    
    def randomManagerInitializeStructuresList(self):
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        for key, value in ob.objectsDict.items():
            checkBox = QtWidgets.QCheckBox()
            checkBox.setText(key)
            checkBox.setObjectName("randomManagerCB" + key)
            checkBox.setFont(font)
            self.randomManagerCheckBoxes[key] = checkBox
            item = QtWidgets.QListWidgetItem(self.randomStructuresListWidget) 
            item.setSizeHint(checkBox.sizeHint())
            
            self.randomStructuresListWidget.addItem(item)
            self.randomStructuresListWidget.setItemWidget(item, checkBox)
            


    def randomManagerAddRandomCells(self):
        if self.enableRandomCells.isChecked():
            for i in range(self.randomFirstGenerationRate.value()):
                x = random.randint(0, self.xFieldSize - 1)
                y = random.randint(0, self.yFieldSize - 1)
                self.calc.setCell(x, y, self.thisRule.generationsCount)
            
            for i in range(self.randomEmptyGenerationRate.value()):
                x = random.randint(0, self.xFieldSize - 1)
                y = random.randint(0, self.yFieldSize - 1)
                self.calc.setCell(x, y, 0)
            
            if self.thisRule.generationsCount > 2:
                for i in range(self.randomIntermediateGenerationRate.value()):
                    x = random.randint(0, self.xFieldSize - 1)
                    y = random.randint(0, self.yFieldSize - 1)
                    self.calc.setCell(x, y, random.randint(1, self.thisRule.generationsCount))

        if self.enableRandomStructures.isChecked():
            needToBePlaced = self.randomStructuresPerFrame.value() # how many objects should be placed on this frame in general
            isThereAnySelectedObject = False # if there is even one selected object
            for key, checkBox in self.randomManagerCheckBoxes.items():
                    if checkBox.isChecked():
                        isThereAnySelectedObject = True

            while isThereAnySelectedObject:
                for key, checkBox in self.randomManagerCheckBoxes.items():
                    if checkBox.isChecked():
                        objectToPlace = ob.objectsDict[key]
                        newObjectToPlaceRotateStep = copy.deepcopy(objectToPlace)

                        if self.enableRandomStructuresRotate.isChecked():
                            for r in range(random.randint(0, 3)): # random rotations count
                                newObjectRotateStep = copy.deepcopy(newObjectToPlaceRotateStep)
                                for i in range(ob.OBJ_SIZE):
                                    for j in range(ob.OBJ_SIZE):
                                        newObjectRotateStep[i][j] = newObjectToPlaceRotateStep[j][ob.OBJ_SIZE - 1 - i]
                                newObjectToPlaceRotateStep = copy.deepcopy(newObjectRotateStep)

                        newObjectToPlaceFlipStep = copy.deepcopy(newObjectToPlaceRotateStep)

                        if self.enableRandomStructuresFlip.isChecked():
                            for i in range(ob.OBJ_SIZE):
                                for j in range(ob.OBJ_SIZE):
                                    newObjectToPlaceFlipStep[i][j] = newObjectToPlaceRotateStep[j][ob.OBJ_SIZE - 1 - i]

                        x = random.randint(0, self.xFieldSize)
                        y = random.randint(0, self.yFieldSize)

                        generationToSet = self.thisRule.generationsCount
                        if self.enableRandomStructuresGeneration.isChecked():
                            generationToSet = random.randint(0, generationToSet)

                        for i in range(ob.OBJ_SIZE):
                            for j in range(ob.OBJ_SIZE):
                                x1 = (x + i + self.xFieldSize) % self.xFieldSize
                                y1 = (y + j + self.yFieldSize) % self.yFieldSize
                                if newObjectToPlaceFlipStep[i][j] == 1:
                                    self.calc.setCell(x1, y1, generationToSet)
                        needToBePlaced -= 1

                    if needToBePlaced <= 0:
                        break
                if needToBePlaced <= 0:
                    break
            
        

