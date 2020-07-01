import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask
)
from app.jsonTools import jsonReader as jr
from app.criteriaAnalise import Criteria as cr
from app.stepAnalise import Step as s
import sys
import json

# Define a blueprint for all function in this module
bp = Blueprint('main', __name__, url_prefix='/main')


@bp.route('/criteriaComputation', methods=['POST', 'GET'])
def postJsonCriteria():
    """send back the json answer with calculated values for a criteria

    call Criteria for all criteria in criterias, and concatenate the answers
    @warning doesn't check if the json has the right structure
    @return: a json, with all calculated values
    """
    print("request json : ", request.get_json(), file=sys.stdout)
    print("request json : ", request.get_json(), file=sys.stderr)
    # check the request has the correct format
    if not request.is_json:
        error = 'a json file is required'
        return error
    # get the json content (get_json send a dictionary)
    content = request.get_json()
    # # write the json answer
    strResult = "{"
    # Loop on the criteria
    for criteriaId in jr.getCriteriasId(content):
        criteria = cr.Criteria(content, criteriaId)
        strResult += '"' + criteriaId + '"' + ': ' + criteria.jsonResponse
    strResult += "}"
    result = {}
    # Loop on the criteria
    for criteriaId in jr.getCriteriasId(content):
        criteria = cr.Criteria(content, criteriaId)
        result[criteria.criteria_id] = criteria.result
    print("result : ", strResult, file=sys.stderr)
    return json.dumps(result, indent=True)


@bp.route('/stageComputation', methods=['POST'])
def postJsonStep():
    """send back the json answer with calculated values for a step (stage or activity)

    @warning doesn't check if the json has the right structure
    @return: a json, with all calculated values
    """
    # check the request has the correct format
    if not request.is_json:
        error = 'a json file is required'
        print(error, file=sys.stderr)
        return error
    # get the json content
    content = request.get_json()
    print("content : ", content, file=sys.stderr)
    # compute the results
    result = s.computeResult(content)
    print("stepResult : ", result, file=sys.stderr)
    return result


@bp.route('/hello', methods=['GET', 'POST'])
def hello_world():
    print("Appel de hello : ", file=sys.stdout)
    return "Welcome on the first version of the framework of result calculation, powered by Serpico"
