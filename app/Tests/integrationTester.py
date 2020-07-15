import os
import os.path as osp
from typing import Dict, Any

import app.Colors as col
import sys
import app.Tests.tester as test
import json
import requests

""" activity ids available if < 318"""
ACT_ID = "1"
URL = "http://localhost:8888/fr/activity/" + ACT_ID
SOURCE_PATH = "app/Tests/dataIntegration/"
ID = {"_username": "rmurray@yopmail.com",
      "_passWord": "Serpico2019",
      "_csrf_token": "6Hb1T56Uow1iWvr2MFWEax26FG61kMq3NZczKg_QUl4",
      "_remember_me": "on",
      "_target_path": "home"}
COOKIES_REQ: Dict[Any, str] = {"PHPSESSID": "9l90v88dne80kbvid7cvdlj90k"}


class Criterion:
    def __init__(self,
                 weight: int,
                 cName: str,
                 type: int,
                 lowerBound: int,
                 upperBound: int,
                 step: int,
                 targetValue="",
                 comment="",
                 forceCommentSign="",
                 forceCommentValue=""):
        self.weight = weight
        self.name = cName
        self.type = type
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.step = step
        self.targetValue = targetValue
        self.comment = comment
        self.forceCommentSign = forceCommentSign
        self.forceCommentValue = forceCommentValue

    def toHashTable(self):
        return {"weight": self.weight,
                "cName": self.name,
                "type": self.type,
                "forceCommentSign": self.forceCommentSign,
                "forceCommentValue": self.forceCommentValue,
                "lowerbound": self.lowerBound,
                "upperbound": self.upperBound,
                "step": self.step,
                "targetValue": self.targetValue,
                "comment": self.comment
                }


class Stage:

    def __init__(self,
                 weight: int,
                 name: str,
                 starddate: str,
                 enddate: str,
                 mode: int,
                 criteria,
                 visibility=3):
        self.weight = weight
        self.name = name
        self.startdate = starddate
        self.endDate = enddate
        self.mode = mode
        self.visibility = visibility
        self.criteria = criteria

    def toHashTable(self):
        criteriaTable = toHashTable(self.criteria)
        return {"activeWeight": self.weight,
                "name": self.name,
                "startdate": self.startdate,
                'gstartdate': self.startdate,
                "enddate": self.startdate,
                "genddate": self.endDate,
                "mode": self.mode,
                "visibility": self.visibility,
                "criteria": criteriaTable}


class Activity:
    def __init__(self, name: str, stages):
        self.name = name
        self.stages = stages

    def toHashTable(self):
        stageTable = toHashTable(self.stages)
        return {"name": self.name,
                "activeModifiableStages": stageTable}


def toHashTable(list):
    table = {}
    for index, element in enumerate(list):
        table[index] = element.toHashTable()
    return table


def runTest():
    print(col.Colors.BOLD + "call of the test runner for integration" + col.Colors.ENDC, file=sys.stderr)
    print(col.Colors.BOLD + "source path : " + col.Colors.ENDC, SOURCE_PATH, file=sys.stderr)
    sys.stderr.flush()
    sourceFiles = [SOURCE_PATH + f for f in os.listdir(SOURCE_PATH) if osp.isfile(osp.join(SOURCE_PATH, f))]
    sourceFiles.sort()
    response = ""
    for source in sourceFiles:
        response += addActivityDataBase(source)
    print("end of request", file=sys.stderr)
    sys.stderr.flush()
    return response


def addActivityDataBase(jsonTested=None):
    print(col.Colors.BOLD + 'Tested file : "' + col.Colors.ENDC + jsonTested + col.Colors.BOLD + '"' + col.Colors.ENDC + \
          test.setSpace(jsonTested), file=sys.stderr)
    if jsonTested is not None:
        response = ""
        response += col.Colors.BOLD + 'Tested file : "' + col.Colors.ENDC + jsonTested + col.Colors.BOLD + '"' + col.Colors.ENDC + \
                    test.setSpace(jsonTested)
        with open(jsonTested, 'r') as f:
            dataToSend = json.load(f)
        x = requests.get("http://localhost:8888/fr/")
        print("success ! !", file=sys.stderr)
        print(x.cookies, file=sys.stderr)
        # with requests.Session() as session:
        #     session.auth = ('rmurray@yopmail.com', "Serpico2019")
        #     session.post("http://localhost:8888/fr/")
        #     print(session.cookies, file=sys.stderr)
        #     session.post("http://localhost:8888/admin/login_check", cookies=session.cookies, json=json.dumps(ID))
        #     session.post(URL, json=dataToSend).json()
        response += "\n"
        print(response, file=sys.stderr)
        sys.stderr.flush()
        return response
    return None
