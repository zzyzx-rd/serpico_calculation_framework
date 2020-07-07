import json
import sys
"""
should always be used to get data from the jsonData, if the structure of the json changes
"""


def readData(jsonFile):
    """

    @deprecated (used for the tests, the Serpico app won't use a file, but send the data directly
    @param jsonFile: name of the file
    @return: a dictionary with the data in the json
    """
    with open(jsonFile) as json_data:
        data_dict = json.load(json_data)
    return data_dict


def getCriteriasId(jsonData):
    """ returns an iterator of the criteria ids"""
    return jsonData["criterias"].keys()


def getTeams(jsonData):
    """returns the dictionary with the composition of the teams {team id: [user_id]}"""
    if "teams" in jsonData.keys() and jsonData["teams"] != []:
        return jsonData["teams"]
    else:
        return None


def getLowerBound(jsonData, criteria_id):
    """returns the lower bound of the criteria"""
    return jsonData["criterias"][criteria_id]["lowerBound"]


def getUpperBound(jsonData, criteria_id):
    """returns the upper bound of the criteria"""
    return jsonData["criterias"][criteria_id]["upperBound"]


def getUserWeights(jsonData):
    """ returns the weights of the users

    @param jsonData : the dictionary with the data
    @return a dictionary with the weights {user_id : user_weight}
    """
    return jsonData['userWeights']


def getUserWeight(jsonData, useId):
    """returns the weight of the user"""
    return jsonData["userWeights"][useId]


def getTeamWeights(jsonData):
    """ returns the weights of the teams

    is used, if the formula of the team weights changes
    @param jsonData : the dictionary with the data
    @return a dictionary with the weights {team_id : user_weight}
    """
    if 'teamWeights' in jsonData.keys():
        return jsonData['teamWeights']
    else:
        return None


def getUserGrades(jsonData, criteriaId):
    """ returns the dictionary with the user's grades

    @param jsonData: the dictionary with the data
    @param criteriaId: string, id of the analysed criteria
    @return: dictionary with the grades of the user {grader_id:{graded_id}}, graded is a user
    """
    return jsonData["criterias"][criteriaId]["userGrades"]


def getTeamGrades(jsonData, criteriaId):
    """ returns the dictionary with the team's grades

    @param jsonData: the dictionary with the data
    @param criteriaId: string, id of the analysed criteria
    @return: dictionary with the grades of the team {grader_id:{graded_id}}, graded is a team, grader a user (team can't
            give grades)
    """
    return jsonData["criterias"][criteriaId]["teamGrades"]


def getStageId(jsonData):
    return jsonData["stageId"]


def getTeamId(jsonData, userId):
    """get the team id in the jsonData

            should be called only by the constructor
            """
    team_Id = None
    print("user id : ", userId, file=sys.stderr)
    if getTeams(jsonData) is not None:
        for teamId, teamMember in getTeams(jsonData).items():
            print("teamID : ", teamId, file=sys.stderr)
            print("teamMember : ", teamMember, file=sys.stderr)
            if str(userId) in teamMember:
                team_Id = teamId
                break
    print("teamId : ", team_Id, file=sys.stderr)
    return team_Id


def isUserGraded(jsonData, criteriaId, userId, teamId=None):
    """boolean, weather the user is graded(an active or a passive

    @param jsonData:  the dictionary with the data
    @param criteriaId: string, id of the analysed criteria
    @param userId: string, id of the user
    @param teamId
    @return: boolean : true if the user is active or passive
    """
    print("user id : ", userId, " teamId : ", teamId, file=sys.stderr)
    # if the user is graded as a user
    for grader, grades in getUserGrades(jsonData, criteriaId).items():
        if userId in grades.keys():
            return True
    # if the user's team is graded
    if teamId is not None:
        return isTeamGraded(jsonData, criteriaId, teamId)
    return False


def isTeamGraded(jsonData, criteriaId, teamId):
    """ indicates if the team as en entity (not the sum of its participants), is graded

    @param jsonData: the dictionary with the data
    @param criteriaId: string, id of the analysed criteria
    @param teamId: string, id of the team
    @return: boolean : true if the team is graded (could not be because of the jockerisation or if the team contains
            only third
    """
    for grader, grades in getTeamGrades(jsonData, criteriaId).items():
        if teamId in grades.keys():
            return True
    return False
