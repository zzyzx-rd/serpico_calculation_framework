import sys

sys.path.append("..")
from app.criteriaAnalise import Criteria as cr
from app.jsonTools import jsonReader as jr
from app.stepAnalise import Step as s


def testCriteria():
    jsonData = jr.readData("Tests/fullDataCriteria.json")
    criteria = cr.Criteria(jsonData, "1")
    criteria.setAnswer("Tests/calculatedFullDataCriteria.json")
    jsonData = jr.readData("Tests/fullDataStep.json")
    s.computeResult(jsonData, "Tests/calculatedFullDataStep.json")


testCriteria()
