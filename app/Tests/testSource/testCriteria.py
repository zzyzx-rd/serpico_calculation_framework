import sys
sys.path.append("..")
from app.criteriaAnalise import Criteria as cr
from app.criteriaAnalise import GradedUser as gu
from app.criteriaAnalise import GradedTeam as gt
from app.jsonTools import jsonReader as jr

def testCriteria():
    jsonData = jr.readData("Tests/data1.json")
    criteria = cr.Criteria(jsonData, "1")
    # Test of criteria instantiation
    if criteria.GradedUser["2"] != gu.GradedUser("2", jsonData, "1"):
        print(1)
        return 1
    if criteria.GradedUser["3"] != gu.GradedUser("3", jsonData, "1"):
        print(2)
        return 1
    if criteria.GradedUser["4"] != gu.GradedUser("4", jsonData, "1"):
        print(3)
        return 1
    if criteria.GradedTeam["1"] != gt.GradedTeam("1", jsonData, "1"):
        print(4)
        return 1
    if criteria.totalUserGradersWeight != 800:
        print(criteria.totalGradersWeight)
        print(5)
        return 1
    if criteria.totalGradedTeamWeight != 1500:
        print(10)
        return 1
    if criteria.totalGradedWeight != 900:
        print(11)
        return 0
    if criteria.nbGradedTeams != 2:
        print(criteria.nbGradedTeams)
        print(12)
        return 1
    if criteria.nbGraded != 3:
        print(12)
        return 2
    if criteria.nbGraders != 3:
        print(13)
        return 1
    if criteria.nbGradersTeam != 1:
        print(14)
        return 1
    # Test of the result calculation
    if criteria.averageUsersWeightedResult != (15 * 200 + 9 * 300 + 11.75 * 400)/900:
        print(criteria.averageUsersWeightedResult)
        print(6)
        return 2
    if criteria.averageUsersEqualResult != (15 + 7.5 + 9.5)/3:
        print((15 + 7.5 + 9.5)/3)
        print(criteria.averageUsersEqualResult)
        print(7)
        return 2
    if criteria.averageTeamsWeightedResult - (700 * 5 + 800 * 16.66666666)/1500 > 10**-5:
        print((700 * 5 + 800 * 16.66666666)/1500)
        print(criteria.averageUsersWeightedResult)
        print(8)
        return 1
    if criteria.averageTeamsEqualResult - (5 + 15)/2:
        print(9)
        return 1
    # Test of the relativeResultCalculation
    if criteria.averageUsersWeightedRelativeResult != (15 * 200 + 9 * 300 + 11.75 * 400)/(900 * 20):
        print(13)
        return 1
    if criteria.averageUsersEqualRelativeResult != (15 + 7.5 + 9.5)/(3 * 20):
        print(14)
        return 1
    if criteria.averageTeamsWeightedRelativeResult - (700 * 5 + 800 * 16.66666666)/(1500 * 20) > 10**-6:
        print(15)
        return 1
    if criteria.averageTeamsEqualRelativeResult != (5 + 15)/(2 * 20):
        print(16)
        return 0

    # Test of the json exit
    criteria.setAnswer("Tests/resultData1.json")
    print(0)
    return 0
testCriteria()