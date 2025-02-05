from rule import Rule

"""
This file contains some hardcoded rules
All rules presets will be saved in file rulesPresets.txt after clicking save im settings preview button
To restore original rules and delete added in game rules either modify rulesPresets.txt of delete that file
Data should be pasted as rule_name/B{digitals}/S{digitals} and optionally /generationscount (wo it will be setted to 2)
Ex.
Default life/B3/S23
Star Wars/B2/S345/4

The rules are from https://habr.com/ru/articles/718620/ and the next article
"""

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
        generationsCount = int(parsed[3]) - 1 if len(parsed) == 4 else 1
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
        res += str(rule.generationsCount + 1)

    return res

def saveToFile():
    file = open("rulesPresets.txt", "w")
    for key, rule in rulesDict.items():
        file.write(strFromRule(key, rule) + '\n')
