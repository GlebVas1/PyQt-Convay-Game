from rule import Rule

defaultLife = Rule(surviveIfNeighborCount = [0, 0, 1, 1, 0, 0, 0, 0, 0], arriveIfNeighborCount = [0, 0, 0, 1, 0, 0, 0, 0, 0], genetationsCount = 1)


starWars = Rule(surviveIfNeighborCount = [0, 0, 0, 1, 1, 1, 0, 0, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 0, 0, 0, 0], genetationsCount = 3)
freeStar = Rule(surviveIfNeighborCount = [1, 0, 0, 1, 1, 1, 0, 0, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 0, 0, 0, 0], genetationsCount = 9)
worms = Rule(surviveIfNeighborCount = [0, 0, 0, 1, 1, 0, 1, 1, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 1, 0, 0, 0], genetationsCount = 5)
sticks = Rule(surviveIfNeighborCount = [0, 0, 0, 1, 1, 1, 1, 0, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 0, 0, 0, 0], genetationsCount = 5)
transersI = Rule(surviveIfNeighborCount = [1, 0, 0, 1, 1, 1, 0, 0, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 0, 1, 0, 0], genetationsCount = 5)
transersII = Rule(surviveIfNeighborCount = [0, 0, 0, 1, 1, 1, 0, 0, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 0, 1, 0, 0], genetationsCount = 4)
thrillGrill = Rule(surviveIfNeighborCount = [0, 1, 1, 1, 1, 0, 0, 0, 0], arriveIfNeighborCount = [0, 0, 0, 1, 1, 0, 0, 0, 0], genetationsCount = 47)
fades = Rule(surviveIfNeighborCount = [0, 0, 1, 0, 0, 1, 0, 0, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 0, 1, 0, 0], genetationsCount = 24)

rulesDict = {"Default life" : defaultLife,
             "Star Wars" : starWars,
             "Free star" : freeStar,
             "Worms" : worms,
             "Sticks" : sticks,
             "Transers I" : transersI,
             "Transers II" : transersII,
             "Thrill Grill" : thrillGrill,
             "Fades" : fades}