import sys

sys.path.append("..")
from app.jsonTools import jsonReader as jr


class TeamGrader:
    """Team with at least one grader (active or third)

    id : string id of the team in the json
    criteriaID : this class is instantiated for any criteria
    criteria : instance of Criteria, the results must have been calculated
    totalGraderWeight : sum of the weights of the teams members (the graders only)
    nbTeamMember : number of grader in the team
    """

    def __init__(self, id, criteria):
        self.id = id
        self._jsonData = criteria._jsonData
        self.criteriaID = criteria.criteria_id
        self.criteria = criteria
        self.totalGraderWeight = 0
        self.nbTeamMember = 0
        self.weightedDevRatio = 0
        self.equalDevRatio = 0
        self.teamMember = {}
        self.setTeamMembers()
        # std dev
        self.weightedStdDev = 0
        self.equalStdDev = 0
        self.calculStdDev()

    def setTeamMembers(self):
        """gets the team member in the json

        teamMember : {grader_id, UserGrader}
        """
        for grader in self.criteria.userGraders.values():
            if grader.team_id == self.id:
                self.teamMember[grader.id] = grader
                self.totalGraderWeight += jr.getUserWeight(self._jsonData, grader.id)
                self.nbTeamMember += 1

    def calculStdDev(self):
        """calculates the both stdDev

        - weightedStdDev
        - equalStdDev
        """
        for grader in self.teamMember.values():
            self.weightedStdDev += grader.weightedStdDev * jr.getUserWeight(self._jsonData, grader.id)
            self.equalStdDev += grader.equalStdDev
        self.weightedStdDev /= self.totalGraderWeight
        self.equalStdDev /= self.nbTeamMember

    def calculateRatios(self):
        """ calculates the both ratios

        - weightedDevRatio
        - equalDevRatio
        """
        if self.criteria.maxWeightedTeamStdDev:
            self.weightedDevRatio = self.weightedStdDev / self.criteria.maxWeightedTeamStdDev
        if self.criteria.maxWeightedTeamStdDev:
            self.equalDevRatio = self.equalStdDev / self.criteria.maxWeightedTeamStdDev
