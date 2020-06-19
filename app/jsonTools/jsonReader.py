import json

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
    return jsonData["teams"]


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
    return jsonData['teamWeights']


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


def isUserGraded(jsonData, criteriaId, userId):
    """boolean, weather the user is graded(an active or a passive

    @param jsonData:  the dictionary with the data
    @param criteriaId: string, id of the analysed criteria
    @param userId: string, id of the user
    @return: boolean : true if the user is active or passive
    """
    for grader, grades in getUserGrades(jsonData, criteriaId).items():
        if userId in grades.keys():
            return True
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