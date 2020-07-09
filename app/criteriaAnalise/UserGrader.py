import sys

sys.path.append("..")
from app.jsonTools import jsonReader as jr
import math as m


class UserGrader:
    """user grader

        id : string id of the user in the json
        criteriaID : this class is instantiated for any criteria
        criteria : instance of Criteria, the results must have been calculated
        userGrade : grades given to users
        team grades : grades given to team
        totalGradedWeight : sum of the weight of the entity(team + user) self grades
        nbGraded : number of entity self grades
        team_id : string id of self team (None if he has no team)
    """

    def __init__(self, id, criteria):
        """

        @param id: string id in the json
        @param criteria: instance of Criteria, the results must have been calculated
        """
        self.id = id
        self._jsonData = criteria._jsonData
        self.criteriaID = criteria.criteria_id
        self.criteria = criteria
        self.userGrades = {}
        self.teamGrades = {}
        self.totalGradedWeight = 0
        self.nbGraded = 0
        self.team_id = None
        self.weightedStdDev = 0
        self.equalStdDev = 0
        self.weightedDevRatio = 0
        self.equalDevRatio = 0
        self.setGrades()
        self.calculStdDev()
        self.setTeamId()

    def setTeamId(self):
        """gets the team id in the json

        should be called only by the constructor
        """
        self.team_id = jr.getTeamId(self._jsonData, self.id)
        print("team id : ", self.team_id, file=sys.stderr)

    def setGrades(self):
        """gets the grades self gives in the json

        - build userGrades and teamGrades {graded_id, Gradable}
        - calculate totalGradedWeight, nbGraded
        """
        # user grades
        if self.id in jr.getUserGrades(self._jsonData, self.criteriaID).keys():
            for graded, user_grade in jr.getUserGrades(self._jsonData, self.criteriaID)[self.id].items():
                self.userGrades[graded] = user_grade
                self.totalGradedWeight += jr.getUserWeight(self._jsonData, graded)
                self.nbGraded += 1
        if self.totalGradedWeight == 0:
            self.totalGradedWeight += 1
        # team grades
        if self.team_id is not None and self.id in jr.getTeamGrades(self._jsonData, self.criteriaID).keys():
            for graded, team_grade in jr.getTeamGrades(self._jsonData, self.criteriaID)[self.id].items():
                self.teamGrades[graded] = team_grade
                self.totalGradedWeight += jr.getTeamWeights(self._jsonData)[graded]
                self.nbGraded += 1

    def calculStdDev(self):
        """calculates the both stdDev

        - weightedStdDev
        - equalStdDev
        """
        userWeights = jr.getUserWeights(self._jsonData)
        teamWeights = jr.getTeamWeights(self._jsonData)
        # Sum on the user grades
        for gradedId in self.userGrades.keys():
            gradedWeightedResult = self.criteria.GradedUser[str(gradedId)].weightedResult
            gradedEqualResult = self.criteria.GradedUser[str(gradedId)].equalResult
            self.weightedStdDev += (gradedWeightedResult - self.userGrades[str(gradedId)]) ** 2 * userWeights[
                str(gradedId)]
            self.equalStdDev += (gradedEqualResult - self.userGrades[str(gradedId)]) ** 2
        # Sum on the teams grades
        for gradedId in self.teamGrades.keys():
            gradedWeightedResult = self.criteria.GradedTeam[gradedId].weightedResult
            gradedEqualResult = self.criteria.GradedTeam[gradedId].equalResult
            self.weightedStdDev += (gradedWeightedResult - self.teamGrades[gradedId]) ** 2 * teamWeights[gradedId]
            self.equalStdDev += (gradedEqualResult - self.teamGrades[gradedId]) ** 2
        self.weightedStdDev /= self.totalGradedWeight
        self.equalStdDev /= self.nbGraded
        self.weightedStdDev = m.sqrt(self.weightedStdDev)
        self.equalStdDev = m.sqrt(self.equalStdDev)

    def calculateRatios(self):
        """ calculates the both ratios

        - weightedDevRatio
        - equalDevRatio
        """
        if self.criteria.maxWeightedUserStdDev:
            self.weightedDevRatio = self.weightedStdDev / self.criteria.maxWeightedUserStdDev
        if self.criteria.maxEqualUserStdDev:
            self.equalDevRatio = self.equalStdDev / self.criteria.maxEqualUserStdDev
