import sys

sys.path.append("..")
from app.criteriaAnalise import UserGrader as ug
from app.criteriaAnalise import Criteria as cr
from app.jsonTools import jsonReader as jr
import math as m

def testTeamGrader():
    jsonData = jr.readData("Tests/data1.json")
    criteria = cr.Criteria(jsonData, "1")
    grader = criteria.teamGraders["1"]
    # test instanciation
    if grader.id != "1":
        print(grader.id)
        print("1")
        return 1
    if grader.totalGraderWeight != 700:
        print(1)
        return 1
    if grader.nbTeamMember != 2:
        print(2)
        return 1
    if grader.weightedStdDev != (2.25 * 300 + 1 * 400)/700:
        print(grader.weightedStdDev)
        print((2.25 * 300 + 1 * 400)/700)
        return 1
    if grader.equalStdDev != (4.5 + 2.5)/2:
        print(grader.equalStdDev)
        print((4.5 + 2.5)/2)
        return 1
    print(0)
    return 0

testTeamGrader()