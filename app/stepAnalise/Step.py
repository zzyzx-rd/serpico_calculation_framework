import sys
import json

sys.path.append("..")
from app.jsonTools import jsonReader as jr

"""
calculated global values 
"""
GLOBAL_KEYS = [
    "averageUsersWeightedResult",
    "averageUsersEqualResult",
    "averageTeamsWeightedResult",
    "averageTeamsEqualResult",
    "averageUsersWeightedRelativeResult",
    "averageUsersEqualRelativeResult",
    "averageTeamsWeightedRelativeResult",
    "averageTeamsEqualRelativeResult",
    "averageUsersWeightedStdDev",
    "averageUsersEqualStdDev",
    "averageTeamsWeightedStdDev",
    "averageTeamsEqualStdDev",
    "maxUsersWeightedStdDev",
    "maxUsersEqualStdDev",
    "maxTeamsWeightedStdDev",
    "maxTeamsEqualStdDev",
    "weightedUserInertia",
    "equalUserInertia",
    "weightedTeamInertia",
    "equalTeamInertia",
    "maxWeightedUserInertia",
    "maxEqualUserInertia",
    "maxWeightedTeamInertia",
    "maxEqualTeamInertia",
    "weightedUserDevRatio",
    "equalUserDevRatio",
    "weightedTeamDevRatio",
    "equalTeamDevRatio",
]
"""
calculated individual values
"""
INDIVIDUAL_KEYS = [
    "weightedResult",
    "equalResult",
    "weightedRelativeResult",
    "equalRelativeResult",
    "weightedStdDev",
    "equalStdDev",
    "weightedDevRatio",
    "equalDevRatio"]
"""
types of entities
"""
ENTITY_TYPES = ["user", "team"]


def averageGlobal(jsonData, key):
    """calculates the average of a value (ex : averageWeightedUserStdDev)

    @param jsonData: dictionary with the json data
    @param key: element on witch the average is calculated (key is in GLOBAL_KEYS)
    @return: the average of the key on all the elements(criterias or stage) in the step (stage or activity)
    """
    average = 0
    sumWeight = 0
    # Loop on the elements (criteria or stage)
    for element_key, element in jsonData.items():
        # if the element is not the dictionary with the user or team's data
        if (not element_key in ENTITY_TYPES) and element_key != "stageId" and element[key] is not None:
            average += element[key] * element["weight"]
            sumWeight += element["weight"]
    if sumWeight:
        return average / sumWeight
    else:
        return None


def averageIndividual(jsonData, entityType, entity_key, key):
    """calculates the average of an individual value (ex: weightedResult)

    @param entity_key: the id of the analysed entity (a user or a team)
    @param entityType: in ENTITY_TYPE
    @param jsonData:dictionary with the json data
    @param key: the value calculated, in INDIVIDUAL_KEYS
    @return: the average of the key on all the elements(criterias or stage) in the step (stage or activity)
    """
    average = 0
    sumWeight = 0
    defined = False
    # loop on the elements (criteria or stage)
    for element_key, element in jsonData.items():
        # if the element is not the dictionary with the user or team's data
        if (not element_key in ENTITY_TYPES) and element_key != "stageId":
            # if the entity has the value for this step
            if entity_key in element[entityType].keys() and key in element[entityType][entity_key].keys() and \
                    element[entityType][entity_key][key] is not None:
                average += element[entityType][entity_key][key] * element["weight"]
                sumWeight += element["weight"]
                defined = True
    # the average can be not defined (for example the weightedResult for a third member)
    if defined:
        return average / sumWeight


def computeResult(jsonData, answerFile=None):
    """calculates all the average for the values in GLOBAL_KEYS and INDIVIDUAL_KEYS on all the elements(criterias or
        stage) in the step (stage or activity)

    @param jsonData: dictionary with the json data
    @param answerFile: string : name on the file where the answer are written (used for tests)
    @return: None if the answer is in a file, the json answer with all the calculated values else
    """
    result = {}
    # compute the global parameters
    for key in GLOBAL_KEYS:
        result[key] = averageGlobal(jsonData, key)
        if result[key] is not None:
            result[key] = round(result[key], 2)
    # compute the individual Parameters
    # loop on user/team type of entities
    for entity_type in ENTITY_TYPES:
        result[entity_type] = {}
        # loop on the entities (user or team)
        for entityKey in jsonData[entity_type]:
            entityKey = str(entityKey)
            result[entity_type][entityKey] = {}
            # Loop on the values to calculate
            for key in INDIVIDUAL_KEYS:
                result[entity_type][entityKey][key] = averageIndividual(jsonData, entity_type, entityKey, key)
                # if the value is defined (ex : weightedResult not defined for a third)
                if result[entity_type][entityKey][key] is not None:
                    result[entity_type][entityKey][key] = round(result[entity_type][entityKey][key], 2)
    result = {"step": result}
    # if the answer must be written in an answer file (for testsà
    if answerFile is not None:
        with open(answerFile, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
    # if the answer must be returned
    else:
        return json.dumps(result, ensure_ascii=False, indent=4)
