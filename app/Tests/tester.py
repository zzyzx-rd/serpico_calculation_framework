import sys

sys.path.append("..")
import json
import requests
import os
import os.path as osp
from app import Colors as col

SOURCE_CRITERIA_PATH = "app/Tests/dataToSend/"
RESPONSE_CRITERIA_PATH = "app/Tests/expectedData/"
SERVEUR_PREFIXE = "http://51.15.121.241:5000/"
LOCAL_PREFIXE = "http://localhost:5000/"
URL_CRITERIA = LOCAL_PREFIXE + "main/criteriaComputation"


def getFiles(path):
    sourceFiles = [path + f for f in os.listdir(path) if osp.isfile(osp.join(path, f))]
    res = []
    for file in sourceFiles:
        res.append(file)
    res.sort()
    return res


def setSpace(fileName):
    space = ""
    for _ in range(50 - len(fileName)):
        space += " "
    return space


def testRunner():
    print("call of the test runner", file=sys.stderr)
    sys.stderr.flush()
    sourceFiles = getFiles(SOURCE_CRITERIA_PATH)
    expectedFiles = getFiles(RESPONSE_CRITERIA_PATH)
    response = ""
    for index, source in enumerate(sourceFiles):
        response += col.Colors.BOLD + 'Tested file : "' + col.Colors.ENDC + source + col.Colors.BOLD + '"' + col.Colors.ENDC + \
                    setSpace(source)
        with open(source, 'r') as f:
            dataToSend = json.load(f)
            calculatedRes = requests.post(URL_CRITERIA, json=dataToSend).json()
        with open(expectedFiles[index]) as f:
            expectedRes = json.load(f)
        if calculatedRes != expectedRes:
            print("calculated : ", calculatedRes, "\nexpected : ", expectedRes, file=sys.stderr)
            sys.stderr.flush()
            response += col.Colors.FAIL + "FAILURE" + col.Colors.ENDC
        else:
            response += col.Colors.OKGREEN + "SUCCESSFUL RESULT" + col.Colors.ENDC
        response += "\n"
    print("end of request", file=sys.stderr)
    print(response, file=sys.stderr)
    sys.stderr.flush()
    return response
