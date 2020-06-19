import sys
sys.path.append("..")
from app.criteriaAnalise.Gradable import Gradable
from app.jsonTools import jsonReader as jr

def testInitGradable():
    jsonData = jr.readData("Tests/data1.json")
    gradable = Gradable(3, jsonData, "1")
    gradable.grades = [(10, 100), (15, 200)]
    gradable.totalWeight = 300
    gradable.numberGrader = 2
    gradable.setResult()
    if gradable.weightedResult != (1000 + 3000) / 300:
        print(1)
    if gradable.equalResult != 12.5:
        print(2)
    if gradable.relativeWeightedResult - (1000 + 3000) / (300 * 20) > 10**-5:
        print(3)
    if gradable.relativeEqualResult - 12.5 / 20 > 10**-5:
        print(4)
    print(0)
    return 0
testInitGradable()