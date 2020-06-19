import sys

sys.path.append("..")
from app.criteriaAnalise import GradedTeam as gu
from app.jsonTools import jsonReader as jr


def testInitGradable():
    jsonData = jr.readData("Tests/data1.json")
    gradedTeam = gu.GradedTeam("1", jsonData, "1")
    if gradedTeam.weight != 700:
        print(1)
        return 1
    if gradedTeam.getGrades() != [(5, 100)]:
        print(gradedTeam.getGrades())
        print(2)
        return 1
    print(0)
    return 0


testInitGradable()
