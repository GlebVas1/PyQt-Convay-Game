import numpy as np
from rule import Rule
    

class Field:
    """ Default game field for convey game"""
    xSize = 10
    ySize = 10
    thisRule = Rule()

    def setRule(self, rule : Rule):
        self.thisRule = rule
    
    def InitializeField(self, x: int = 10, y : int = 10, rule : Rule = Rule()):
        self.field = np.ndarray(shape=(x, y), dtype=int)
        self.xSize = x
        self.ySize = y
        self.thisRule = rule
    
    def setCell(self, x : int, y : int, val : int):
        self.field[x, y] = val
    
    def fillField(self, val : int):
        self.field.fill(val)
    
    def calcualteNeighborCount(self, x : int, y : int) -> int:
        neightborCount = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.field[(x + i + self.xSize) % self.xSize, (y + j + self.ySize) % self.ySize] == self.thisRule.genetationsCount:
                    neightborCount += 1
        return neightborCount
    
    def calcualteFieldStep(self):
        newField = np.ndarray(shape=(self.xSize, self.ySize), dtype=int)

        for x in range(self.xSize):
            for y in range(self.ySize):
                neighborCount = self.calcualteNeighborCount(x, y)

                if self.field[x, y] == 0: # empty or dead
                    if self.thisRule.getArrival(neighborCount):
                        newField[x, y] = self.thisRule.genetationsCount
                    else:
                        newField[x,y] = 0
                else:
                    if self.field[x, y] == self.thisRule.genetationsCount:
                        if self.thisRule.getSurvive(neighborCount):
                            newField[x, y] = self.field[x, y]
                        else:
                            newField[x, y] = self.field[x, y] - 1
                    else:
                        newField[x, y] = self.field[x, y] - 1
        # print(self.field)
        # print(newField)
        self.field = newField.copy()
    
    def getState(self, x : int, y : int) -> int:
        return int(self.field[x, y])
    
    def setState(self, x : int, y : int, val : int):
        self.field[x, y] = val