from rule import Rule

defaultLife = Rule(surviveIfNeighborCount = [0, 0, 1, 1, 0, 0, 0, 0, 0], arriveIfNeighborCount = [0, 0, 0, 1, 0, 0, 0, 0, 0], genetationsCount = 1)
labirinth = Rule(surviveIfNeighborCount = [0, 1, 1, 1, 1, 1, 0, 0, 0], arriveIfNeighborCount = [0, 0, 0, 1, 0, 0, 0, 0, 0], genetationsCount = 1)
mazectric = Rule(surviveIfNeighborCount = [0, 1, 1, 1, 1, 0, 0, 0, 0], arriveIfNeighborCount = [0, 0, 0, 1, 0, 0, 0, 0, 0], genetationsCount = 1)
mouseMaze = Rule(surviveIfNeighborCount = [0, 1, 1, 1, 1, 1, 0, 0, 0], arriveIfNeighborCount = [0, 0, 0, 1, 0, 0, 0, 1, 0], genetationsCount = 1)
mazectricMouse = Rule(surviveIfNeighborCount = [0, 1, 1, 1, 1, 0, 0, 0, 0], arriveIfNeighborCount = [0, 0, 0, 1, 0, 0, 0, 1, 0], genetationsCount = 1)
HTree = Rule(surviveIfNeighborCount = [1, 1, 1, 1, 1, 1, 1, 1, 1], arriveIfNeighborCount = [0, 1, 0, 0, 0, 0, 0, 0, 0], genetationsCount = 1)

starWars = Rule(surviveIfNeighborCount = [0, 0, 0, 1, 1, 1, 0, 0, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 0, 0, 0, 0], genetationsCount = 3)
freeStar = Rule(surviveIfNeighborCount = [1, 0, 0, 1, 1, 1, 0, 0, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 0, 0, 0, 0], genetationsCount = 9)
worms = Rule(surviveIfNeighborCount = [0, 0, 0, 1, 1, 0, 1, 1, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 1, 0, 0, 0], genetationsCount = 5)
sticks = Rule(surviveIfNeighborCount = [0, 0, 0, 1, 1, 1, 1, 0, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 0, 0, 0, 0], genetationsCount = 5)
transersI = Rule(surviveIfNeighborCount = [1, 0, 0, 1, 1, 1, 0, 0, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 0, 1, 0, 0], genetationsCount = 5)
transersII = Rule(surviveIfNeighborCount = [0, 0, 0, 1, 1, 1, 0, 0, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 0, 1, 0, 0], genetationsCount = 4)
thrillGrill = Rule(surviveIfNeighborCount = [0, 1, 1, 1, 1, 0, 0, 0, 0], arriveIfNeighborCount = [0, 0, 0, 1, 1, 0, 0, 0, 0], genetationsCount = 47)
fades = Rule(surviveIfNeighborCount = [0, 0, 1, 0, 0, 1, 0, 0, 0], arriveIfNeighborCount = [0, 0, 1, 0, 0, 0, 1, 0, 0], genetationsCount = 24)

rulesDict = {"Default life" : defaultLife,
             "Maze" : labirinth,
             "Mazectric" : mazectric,
             "Mouse maze" : mouseMaze,
             "Mazectric with mice" : mazectricMouse,
             "H-Tree" : HTree,
             "Star Wars" : starWars,
             "Free star" : freeStar,
             "Worms" : worms,
             "Sticks" : sticks,
             "Transers I" : transersI,
             "Transers II" : transersII,
             "Thrill Grill" : thrillGrill,
             "Fades" : fades}

def loadRulesFromFile():
    file = open("rulesPresets.txt", "r")

    def strToList(values : str) -> list:
        l = []
        for i in range(9):
            l.append(0)
        for c in list(values):
            if not c.isdigit():
                continue
            l[int(c)] = 1
        return l
    
    for line in file:
        parsed = line.split('/')
        name = parsed[0]
        generationsCount = int(parsed[3]) if len(parsed) == 4 else 1
        listArrive = strToList(parsed[1])
        listSurvive = strToList(parsed[2])
        rulesDict[name] = Rule(listSurvive, listArrive, generationsCount)
        

def strFromRule(name : str, rule : Rule) -> str:
    res = name
    res += "/B"

    for i in range(9):
        if rule.arriveIfNeighborCount[i] == 1:
            res += str(i)

    res += "/S"

    for i in range(9):
        if rule.surviveIfNeighborCount[i] == 1:
            res += str(i)
            
    if rule.generationsCount != 1:
        res += "/"
        res += str(rule.generationsCount)

    return res

def saveToFile():
    file = open("rulesPresets.txt", "w")
    for key, rule in rulesDict.items():
        file.write(strFromRule(key, rule) + '\n')
