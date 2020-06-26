import sys

sys.path.append("..")
from app.criteriaAnalise import Criteria as cr
from app.jsonTools import jsonReader as jr
from app.stepAnalise import Step as s


def testCriteria():
    jsonData = jr.readData("Tests/fullDataCriteria2.json")
    criteria = cr.Criteria(jsonData, "1")
    criteria.setAnswer("Tests/calculatedFullDataCriteria2.json")
    jsonData = jr.readData("Tests/fullDataStep.json")
    s.computeResult(jsonData, "Tests/calculatedFullDataStep.json")


testCriteria()
