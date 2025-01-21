class Rule:
    """
    Rule that returns new cellState by neighbors count
    State 0 - dead / empty
    State generationsCount -- new born
    
    """
    surviveIfNeighborCount = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
    arriveIfNeighborCount = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    generationsCount = 1
    
    def getSurvive(self, neighborCount : int) -> bool:
        return self.surviveIfNeighborCount[neighborCount] == 1
    
    def getArrival(self, neighborCount : int) -> bool:
        return self.arriveIfNeighborCount[neighborCount] == 1

    def __init__(self, surviveIfNeighborCount : list = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0], arriveIfNeighborCount : list = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], genetationsCount = 1):
        self.surviveIfNeighborCount = surviveIfNeighborCount
        self.arriveIfNeighborCount = arriveIfNeighborCount
        self.generationsCount = genetationsCount