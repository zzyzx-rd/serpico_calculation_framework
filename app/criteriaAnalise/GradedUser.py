import sys

sys.path.append("..")
from app.criteriaAnalise.Gradable import Gradable
from app.jsonTools import jsonReader as jr


class GradedUser(Gradable):
    """ user (person, not team) GRADED(active or passive

        this class calculates the results for a graded user
        The difference is for the weight recuperation in the json, and for the grade recuperation
    """

    def __init__(self, id, jsonData, criteria_id):
        """Constructor

        @param id : string
        @param jsonData : dictionary, build with jsonTools/jsonReader readData
        @param criteria_id : a GradedUser is instanced for any criteria.
        """
        super().__init__(id, jsonData, criteria_id)
        self.weight = self._jsonData["userWeights"][self.id]
        self.setTeamId()
        self.setGrades()
        self.setResult()

    def setTeamId(self):
        """get the team id in the jsonData

        should be called only by the constructor
        """
        self.team_id = jr.getTeamId(self._jsonData, self.id)

    def setGrades(self):
        """ Sets grades attribute with the grades in the json

        get the user grades
        get the user's team grades
        should be called only by the constructor
        """
        self.grades = []
        # Loop on the user grades
        for grader, user_grades in jr.getUserGrades(self._jsonData, self.criteria_id).items():
            # if the grader has graded this graded (jockerisation)
            if self.id in user_grades.keys():
                self.grades.append((user_grades[self.id], jr.getUserWeight(self._jsonData, grader)))
                self.totalWeight += jr.getUserWeight(self._jsonData, grader)
                self.numberGrader += 1
        # Loop on the team results (if necessary)
        if self.team_id is not None:
            for grader, team_grades in jr.getTeamGrades(self._jsonData, self.criteria_id).items():
                if self.team_id in team_grades.keys() and jr.getTeamId(self._jsonData, grader) != self.team_id:
                    self.grades.append((team_grades[self.team_id], jr.getUserWeight(self._jsonData, grader)))
                    self.totalWeight += jr.getUserWeight(self._jsonData, grader)
                    self.numberGrader += 1
        if self.totalWeight == 0:
            self.totalWeight += 1

    def __eq__(self, other):
        res = True
        res = res and self.id == other.id
        res = res and self.team_id == other.team_id
        res = res and self.grades == other.grades
        res = res and self.weight == other.weight
        return res

    def __str__(self):
        res = "id : " + str(self.id)
        res += "\nweight : " + str(self.weight)
        res += "\nteam_id : " + str(self.team_id)
        res += "\ngrades : " + str(self.grades)
        res += "\nweightedResult : " + str(self.weightedResult)
        res += "\nequalResult : " + str(self.equalResult)
        return res
