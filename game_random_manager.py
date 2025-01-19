import random


class RandomManager(object):

    def addRandomCells(self):
        if self.enableRandomCells:
            for i in range(self.randomFirstGenerationRate.value()):
                x = random.randint(0, self.xFieldSize)
                y = random.randint(0, self.yFieldSize)
                self.calc.setCell(x, y, self.thisRule.generationsCount)
            
            for i in range(self.randomEmptyGenerationRate.value()):
                x = random.randint(0, self.xFieldSize)
                y = random.randint(0, self.yFieldSize)
                self.calc.setCell(x, y, 0)
            
            if self.thisRule.generationsCount > 2:
                for i in range(self.randomIntermediateGenerationRate.value()):
                    x = random.randint(0, self.xFieldSize)
                    y = random.randint(0, self.yFieldSize)
                    self.calc.setCell(x, y, random.randint(1, self.thisRule.generationsCount))
            
        

