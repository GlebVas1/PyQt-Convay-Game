import numpy as np

class Rule:
    """Rule that returns new cellState by neighbors count"""
    surviveIfNeighborCount = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
    arriveIfNeighborCount = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    
    def getSurvive(self, neighborCount : int):
        return self.surviveIfNeighborCount[neighborCount]
    
    def getArrival(self, neighborCount : int):
        return self.arriveIfNeighborCount[neighborCount]
    

class Field:
    """ Default game field for convey game"""
    xSize = 10
    ySize = 10
    thisRule = Rule()

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
                
                if self.field[(x + i + self.xSize) % self.xSize, (y + j + self.ySize) % self.ySize] != 0:
                    neightborCount += 1
        return neightborCount
    
    def calcualteFieldStep(self):
        newFiled = np.ndarray(shape=(self.xSize, self.ySize))

        for x in range(self.xSize):
            for y in range(self.ySize):
                neighborCount = self.calcualteNeighborCount(x, y)
                if self.field[x, y] == 0:
                    newFiled[x, y] = self.thisRule.getArrival(neighborCount)
                else:
                    newFiled[x, y] = self.thisRule.getSurvive(neighborCount)
        self.field = newFiled.copy()
    
    def getState(self, x : int, y : int) -> int:
        return int(self.field[x, y])
    
    def setState(self, x : int, y : int, val : int):
        self.field[x, y] = val