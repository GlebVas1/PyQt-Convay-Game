def formulateRule(ruleName : str, surviveIfNeighborCount : list, arriveIfNeighborCount : list, genetationsCount : int):
    ruleStr = "{} = Rule(surviveIfNeighborCount = {}, arriveIfNeighborCount = {}, genetationsCount = {})"
    return ruleStr.format(ruleName, surviveIfNeighborCount, arriveIfNeighborCount, genetationsCount)

def strToList(values : str) -> list:
    l = []
    for i in range(9):
        l.append(0)
    for c in list(values):
        l[int(c)] = 1
    return l

strToParse = input()

parsed = strToParse.split('/')
print(parsed)
name = parsed[0]
listArrive = strToList(parsed[2])
listSurvive = strToList(parsed[4])

generationsCount = int(parsed[5]) - 1 if len(parsed) == 6 else 1
    
print(formulateRule(name, listSurvive, listArrive, generationsCount))