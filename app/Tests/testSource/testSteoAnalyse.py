import sys
sys.path.append("..")
from app.stepAnalise import Step as s
from app.jsonTools import jsonReader as jr
jsonData = jr.readData("Tests/2.json")
s.computeResult(jsonData, "Tests/resultData2.json")
