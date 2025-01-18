from rule import Rule

defaultLife = Rule(surviveIfNeighborCount = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0], arriveIfNeighborCount = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], genetationsCount = 1)
starWars = Rule(surviveIfNeighborCount = [0, 0, 0, 1, 1, 1, 0, 0, 0, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], genetationsCount = 3)

rulesDict = {"Default life" : defaultLife,
             "Star Wars" : starWars}