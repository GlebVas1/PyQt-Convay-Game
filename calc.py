import numpy as np
from rule import Rule
    

class Field:
    """ Default game field for convey game"""
    xSize = 10
    ySize = 10
    thisRule = Rule()

    statistics = {}
    statisticsMaxSize = 100
    
    def initializeField(self, x: int = 10, y : int = 10):
        self.field = np.zeros(shape=(x, y), dtype=int)
        self.xSize = x
        self.ySize = y

    def reinitializeFieldWithNewSize(self, xSize : int, ySize : int):
        
        newField = np.zeros(shape=(xSize, ySize), dtype=int)

        xBorders = (max(self.field.shape[0] - xSize, 0) + 1) // 2
        yBorders = (max(self.field.shape[1] - ySize, 0) + 1) // 2

        # Xtop с + 1, Xbottom wo + 1

        truncatedField = self.field[xBorders :  self.xSize - xBorders, yBorders :self.ySize - yBorders]
        print(truncatedField)
        self.xSize = xSize
        self.ySize = ySize

        xPosition = (xSize - truncatedField.shape[0]) // 2
        yPosition = (ySize - truncatedField.shape[1]) // 2

        for i in range(truncatedField.shape[0]):
            for j in range(truncatedField.shape[1]):
                newField[i + xPosition][j + yPosition] = truncatedField[i][j]

        self.field = newField

    def initializeStatistics(self):
        maxStatiSticLength = 0

        keysToDelete = []
        for key, value in self.statistics.items():
            maxStatiSticLength = max(maxStatiSticLength, len(value))
            if key not in range(self.thisRule.generationsCount + 1):
                keysToDelete.append(key)
        
        for key in keysToDelete:
            del self.statistics[key]
        
        for i in range(self.thisRule.generationsCount + 1):
            self.statistics[i] = []

        for key, value in self.statistics.items():
            while len(value) < maxStatiSticLength:
                value.append(0)

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
                if self.field[(x + i + self.xSize) % self.xSize, (y + j + self.ySize) % self.ySize] == self.thisRule.generationsCount:
                    neightborCount += 1
        return neightborCount
    
    def calcualteFieldStep(self):
        newField = np.ndarray(shape=(self.xSize, self.ySize), dtype=int)

        for x in range(self.xSize):
            for y in range(self.ySize):
                neighborCount = self.calcualteNeighborCount(x, y)

                if self.field[x, y] == 0: # empty or dead
                    if self.thisRule.getArrival(neighborCount):
                        newField[x, y] = self.thisRule.generationsCount
                    else:
                        newField[x,y] = 0
                else:
                    if self.field[x, y] == self.thisRule.generationsCount:
                        if self.thisRule.getSurvive(neighborCount):
                            newField[x, y] = self.field[x, y]
                        else:
                            newField[x, y] = self.field[x, y] - 1
                    else:
                        newField[x, y] = self.field[x, y] - 1

        self.field = newField.copy()
    
    def getState(self, x : int, y : int) -> int:
        return int(self.field[x, y])
    
    def setState(self, x : int, y : int, val : int):
        self.field[x, y] = val

    def calcStatistic(self):
        currentStatistic = {}
        for i in range(self.thisRule.generationsCount + 1):
            currentStatistic[i] = 0

        for x in range(self.xSize):
            for y in range(self.ySize):
                currentStatistic[self.getState(x, y)] += 1
                
        for generation, value in currentStatistic.items():
            self.statistics[generation].append(value)
            if len(self.statistics[generation]) > self.statisticsMaxSize:
                self.statistics[generation] = self.statistics[generation][1:]
        

