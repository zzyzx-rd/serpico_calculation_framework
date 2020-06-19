import sys

sys.path.append("..")
from app.criteriaAnalise import UserGrader as ug
from app.criteriaAnalise import Criteria as cr
from app.jsonTools import jsonReader as jr
import math as m

def testUserGrader():
    jsonData = jr.readData("Tests/data1.json")
    criteria = cr.Criteria(jsonData, "1")
    grader = criteria.userGraders["1"]
    # test instanciation
    if grader.userGrades != {"2": 15}:
        print(1)
        print("err : userGrades ")
        print(grader.userGrades)
        return 1
    if grader.teamGrades != {"1": 5, "2": 10}:
        print(1)
        print("err : teamsGrades")
        return 1
    if grader.nbGraded != 3:
        print(1)
        return 1
    if grader.totalGradedWeight != 1700:
        print(1)
        return 1
    if grader.team_id is not None:
        print(1)
    # test stdDev
    if grader.weightedStdDev - m.sqrt(((15 - 15) + (5 - 5) + (10 - 16.66666666666)**2 * 800)/1700) > 10**-5:
        print(2)
        print(grader.weightedStdDev)
        print(m.sqrt(((15 - 15) + (5 - 5) + (10 - 16.66666666666)**2 * 800)/1700))
        return 1
    if grader.equalStdDev - m.sqrt(((15 - 15) + (5 - 5) + (10 - 15)**2) / 3) > 10**-5:
        print(3)
        print(grader.equalStdDev)
        print( m.sqrt(((15 - 15) + (5 - 5) + (10 - 15)**2) / 3))
        return 1

    # test team setting
    grader = ug.UserGrader("3", criteria)
    if grader.team_id != "1":
        print("11")
    print(0)
    return 0

testUserGrader()