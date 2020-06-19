import sys

sys.path.append("..")
from app.criteriaAnalise import GradedUser as gu
from app.jsonTools import jsonReader as jr


def testInitGradable():
    jsonData = jr.readData("Tests/data1.json")
    # Tests without team
    gradedUser = gu.GradedUser("3", jsonData, "1")
    if gradedUser.weight != 300:
        print(1)
        return 1

    if gradedUser.team_id != "1":
        print("team id : ", gradedUser.team_id)
        print(3)
        return 3
    if gradedUser.getGrades() != [(10, 400), (5, 100)]:
        print(gradedUser.getGrades(10 * 400 + 5 * 100) / 500)
        print(2)
        return 1
    if gradedUser.weightedResult != (10 * 400 + 5 * 100) / 500:
        print(5)
    print(0)
    return 0


testInitGradable()
