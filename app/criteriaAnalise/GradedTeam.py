import sys

sys.path.append("..")
from app.criteriaAnalise.Gradable import Gradable
from app.jsonTools import jsonReader as jr


class GradedTeam(Gradable):
    """ team (not person) (as a team entity, not the sum of its member)

        this class calculates the results for a graded team,
        The difference is for the weight recuperation in the json, and for the grade recuperation
    """

    def __init__(self, id, jsonData, criteria_id):
        """Constructor

        @param id : string
        @param jsonData : dictionary, build with jsonReader.readData
        @param criteria_id : a GradedTeam is instanced for any criteria.
        """
        super().__init__(id, jsonData, criteria_id)
        self.weight = self._jsonData['teamWeights'][str(self.id)]
        self.setGrades()
        self.setResult()

    def setGrades(self):
        """ Sets grades attribute with the grades in the json

        should be called only by the constructor
        gets the user grades
        gets the user's team grades
        """
        self.grades = []
        for grader, team_grades in jr.getTeamGrades(self._jsonData, self.criteria_id).items():
            if self.id in team_grades.keys():
                self.grades.append((team_grades[self.id], jr.getUserWeight(self._jsonData, grader)))
                self.totalWeight += jr.getUserWeight(self._jsonData, grader)
                self.numberGrader += 1

    def __eq__(self, other):
        res = True
        res = res and self.id == other.id
        res = res and self.grades == other.grades
        res = res and self.weight == other.weight
        return res

    def __str__(self):
        res = "id : " + str(self.id)
        res += "\nweight : " + str(self.weight)
        res += "\ngrades : " + str(self.grades)
        res += "\nweightedResult : " + str(self.weightedResult)
        res += "\nequalResult : " + str(self.equalResult)
        return res
