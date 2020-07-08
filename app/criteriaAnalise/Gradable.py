import sys

sys.path.append("..")
from app.jsonTools import jsonReader as jr


class Gradable:
    """Abstract class, represents a gradable entity

    id : string (in the json file)
    jsonData : dictionary, built with the json reader
    criteria_id : criteria id in the json file
    lower and upper bound: bound of the grade for the criteria
    grades : [(grade, weight)], grades given to the gradable
    totalWeight : sum of the weights of his graders
    number grader : number of grades received (can change because of the jockerisation)
    """

    def __init__(self, id, jsonData, criteria_id):
        self.id = id
        self._jsonData = jsonData
        self.criteria_id = criteria_id
        self.lowerBound = jr.getLowerBound(self._jsonData, self.criteria_id)
        self.upperBound = jr.getUpperBound(self._jsonData, self.criteria_id)
        self.grades = None
        # results
        self.weightedResult = 0
        self.equalResult = 0
        self.relativeWeightedResult = 0
        self.relativeEqualResult = 0
        self.equalRelativeResult = 0
        self.totalWeight = 0
        self.numberGrader = 0

    def getGrades(self):
        """ getter

        @deprecated: used with an old implementation, but not problematic (and remains in the actual code)
        """
        return self.grades

    @property
    def __str__(self):
        res = "id : " + str(self.id)
        res += "\nweight : " + str(self.weight)
        res += "\ngrades : " + str(self.grades)
        return res

    def setResult(self):
        """Calculate all the results (Results and RelativeResult)

        should be called only by the subclasses constructors
        """
        for (grade, weight) in self.grades:
            self.weighdResult += grade * weight
            self.equalResult += grade
        self.weightedResult /= self.totalWeight
        self.equalResult /= self.numberGrader
        self.relativeWeightedResult = (self.weightedResult - self.lowerBound) / (self.upperBound - self.lowerBound)
        self.relativeEqualResult = (self.equalResult - self.lowerBound) / (self.upperBound - self.lowerBound)
