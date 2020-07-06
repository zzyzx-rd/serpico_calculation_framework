import sys

sys.path.append("..")
from app.jsonTools import jsonReader as jr
from app.criteriaAnalise import GradedUser as gu
from app.criteriaAnalise import GradedTeam as gt
from app.criteriaAnalise import UserGrader as ug
from app.criteriaAnalise import TeamGrader as tg
import json
import math as m


class Criteria:
    """ Compute all results for a criteria, with a jsonData(created with jsonReader)

    - Creates instances of GradedUser and GradedTeam (it calculates the individual results)
    - calculate the average of results
    - creates instances of UserGraders and TeamGraders (process the stdDev)
    - calculate the global deviation values (maxStdDev needed for ratios)
    - calculates the individual ratios with the graders instances
    """

    def __init__(self, jsonData, criteria_id):
        """ Constructor

        @param jsonData: a dictionary instanced with jsonReader
        @param criteria_id: String the ID of the criteria in the json
        """
        # Weights
        self.totalUserGradersWeight = 0
        self.totalTeamsGradersWeight = 0
        self.totalGradedWeight = 0
        self.totalGradedTeamWeight = 0
        # nb
        self.nbGraders = 0
        self.nbGradersTeam = 0
        self.nbGraded = 0
        self.nbGradedTeams = 0
        # Result
        self.averageUsersWeightedResult = 0
        self.averageUsersEqualResult = 0
        self.averageTeamsWeightedResult = 0
        self.averageTeamsEqualResult = 0
        # StdDev
        self.averageEqualTeamStdDev = 0
        self.averageWeightedTeamStdDev = 0
        self.averageEqualUserStdDev = 0
        self.averageWeightedUserStdDev = 0
        # max StdDev
        self.maxWeightedUserStdDev = 0
        self.maxEqualUserStdDev = 0
        self.maxWeightedTeamStdDev = 0
        self.maxEqualTeamStdDev = 0
        # Inertia
        self.weightedUserInertia = 0
        self.equalUserInertia = 0
        self.weightedTeamInertia = 0
        self.equalTeamInertia = 0
        # devRatios
        self.weightedUserDevRatio = 0
        self.eqalUserDevRatio = 0
        self.weightedTeamDevRatio = 0
        self.equalTeamDevRatio = 0
        # Entities (grader and graded)
        self.userGraders = {}
        self.teamGraders = {}
        self.GradedUser = {}
        self.GradedTeam = {}
        # values
        self._jsonData = jsonData
        self.criteria_id = criteria_id
        self.lowerBound = jr.getLowerBound(self._jsonData, self.criteria_id)
        self.upperBound = jr.getUpperBound(self._jsonData, self.criteria_id)
        # process
        self.setGradedUsers()
        self.setGradedTeams()
        self.calculateResult()
        self.setGraders()
        self.calculateGlobalDevValues()
        self.calculateIndividualRatios()
        self.setAnswer()

    def setGradedUsers(self):
        """Instantiates all the gradedUsers

        build GradedUser{userID: GradedUser}
        """
        for user, weight in jr.getUserWeights(self._jsonData).items():
            if jr.isUserGraded(self._jsonData, self.criteria_id, user):
                self.GradedUser[user] = gu.GradedUser(user, self._jsonData, self.criteria_id)
                self.totalGradedWeight += weight
                self.nbGraded += 1
        if not self.totalGradedWeight:
            self.totalGradedWeight = 1

    def setGradedTeams(self):
        """Instantiates all the gradedTeams
        build GradedTeams{teamId: GradedTeam}
        """
        if jr.getTeams(self._jsonData) is None:
            self.GradedTeam = None
        else:
            for team, weight in jr.getTeamWeights(self._jsonData).items():
                if jr.isTeamGraded(self._jsonData, self.criteria_id, team):
                    self.GradedTeam[team] = gt.GradedTeam(team, self._jsonData, self.criteria_id)
                    self.totalGradedTeamWeight += weight
                    self.nbGradedTeams += 1

    def setGraders(self):
        """Instantiates all the graders (user and team)
        build userGraders and teamGraders {graderID: grader}
        """
        # users
        for graderID in jr.getUserGrades(self._jsonData, self.criteria_id).keys():
            self.userGraders[graderID] = ug.UserGrader(graderID, self)
            self.totalUserGradersWeight += jr.getUserWeight(self._jsonData, graderID)
            self.nbGraders += 1
        if self.totalUserGradersWeight == 0:
            self.totalUserGradersWeight = 1
        # teams (contains a least one grader)
        for grader in self.userGraders.values():
            if (grader.team_id is not None) and (not grader.team_id in self.teamGraders.keys()):
                self.teamGraders[grader.team_id] = tg.TeamGrader(grader.team_id, self)
                self.totalTeamsGradersWeight += jr.getTeamWeights(self._jsonData)[grader.team_id]
                self.nbGradersTeam += 1

    def calculateResult(self):
        """calculates the global results

        averageResult
        averageRelativeResult
        """
        # Results
        for graded in self.GradedUser.values():
            self.averageUsersWeightedResult += graded.weightedResult * graded.weight
            self.averageUsersEqualResult += graded.equalResult
        self.averageUsersWeightedResult /= self.totalGradedWeight
        self.averageUsersEqualResult /= self.nbGraded
        if self.nbGradedTeams:
            for team in self.GradedTeam.values():
                self.averageTeamsWeightedResult += team.weightedResult * team.weight
                self.averageTeamsEqualResult += team.equalResult
            self.averageTeamsWeightedResult /= self.totalGradedTeamWeight
            self.averageTeamsEqualResult /= self.nbGradedTeams
        # RelativeResults
        self.averageUsersWeightedRelativeResult = (self.averageUsersWeightedResult - self.lowerBound) / (
                self.upperBound - self.lowerBound)
        self.averageUsersEqualRelativeResult = (self.averageUsersEqualResult - self.lowerBound) / (
                self.upperBound - self.lowerBound)
        self.averageTeamsWeightedRelativeResult = (self.averageTeamsWeightedResult - self.lowerBound) / (
                self.upperBound - self.lowerBound)
        self.averageTeamsEqualRelativeResult = (self.averageTeamsEqualResult - self.lowerBound) / (
                self.upperBound - self.lowerBound)

    def calculateGlobalDevValues(self):
        """ calculates the global deviation values"""
        # StdDev
        self.computeStdDev()
        # Max stdDev
        self.computeMaxStdDev()
        # inertia
        self.computeInertia()
        # devRatios
        if self.maxWeightedUserStdDev:
            self.weightedUserDevRatio = self.weightedUserInertia / self.maxWeightedUserStdDev ** 2
        if self.maxEqualUserStdDev:
            self.eqalUserDevRatio = self.equalUserInertia / self.maxEqualUserStdDev ** 2
        if self.nbGradersTeam:
            self.weightedTeamDevRatio = self.weightedTeamInertia / self.maxWeightedTeamStdDev ** 2
            self.equalTeamDevRatio = self.equalTeamInertia / self.maxEqualTeamStdDev ** 2

    def computeStdDev(self):
        """computes the standard deviations values

        - averageWeightedUserStdDev
        - averageEqualUserStdDev
        - averageWeightedTeamStdDev
        - averageEqualTeamStdDev
        """
        for grader in self.userGraders.values():
            self.averageWeightedUserStdDev += grader.weightedStdDev * jr.getUserWeight(self._jsonData, grader.id)
            self.averageEqualUserStdDev += grader.equalStdDev
        self.averageWeightedUserStdDev /= self.totalUserGradersWeight
        self.averageEqualUserStdDev /= self.nbGraders
        if self.nbGradersTeam:
            for grader in self.teamGraders.values():
                self.averageWeightedTeamStdDev += grader.weightedStdDev * jr.getTeamWeights(self._jsonData)[grader.id]
                self.averageEqualTeamStdDev += grader.equalStdDev
            self.averageWeightedTeamStdDev /= self.totalTeamsGradersWeight
            self.averageEqualTeamStdDev /= self.nbGradersTeam

    def computeMaxStdDev(self):
        """computes the maximalStdDevs (the theoretical maximums)

        - maxWeightedUserStdDev
        - maxEqualUserStdDev
        - maxWeightedTeamStdDev
        - maxEqualTeamStdDev
        """
        # User
        for graded in self.GradedUser.values():
            # Weighted
            if graded.weightedResult < (self.lowerBound + self.upperBound) / 2:
                self.maxWeightedUserStdDev += (self.upperBound - graded.weightedResult) ** 2 * jr.getUserWeight(
                    self._jsonData, graded.id)
            else:
                self.maxWeightedUserStdDev += (self.lowerBound - graded.weightedResult) ** 2 * jr.getUserWeight(
                    self._jsonData, graded.id)
            # Equal
            if graded.equalResult < (self.lowerBound + self.upperBound) / 2:
                self.maxEqualUserStdDev += (self.upperBound - graded.equalResult) ** 2
            else:
                self.maxEqualUserStdDev += (self.lowerBound - graded.equalResult) ** 2
        self.maxWeightedUserStdDev /= self.totalGradedWeight
        self.maxWeightedUserStdDev = m.sqrt(self.maxWeightedUserStdDev)
        self.maxEqualUserStdDev /= self.nbGraded
        self.maxEqualUserStdDev = m.sqrt(self.maxEqualUserStdDev)
        # Team
        if self.nbGradedTeams:
            for graded in self.GradedTeam.values():
                if graded.weightedResult < (self.lowerBound + self.upperBound) / 2:
                    self.maxWeightedTeamStdDev += (self.upperBound - graded.weightedResult) ** 2 * \
                                                  jr.getTeamWeights(self._jsonData)[graded.id]
                else:
                    self.maxWeightedTeamStdDev += (self.lowerBound - graded.weightedResult) ** 2 * \
                                                  jr.getTeamWeights(self._jsonData)[graded.id]
                if graded.equalResult < (self.lowerBound + self.upperBound) / 2:
                    self.maxEqualTeamStdDev += (self.upperBound - graded.equalResult) ** 2
                else:
                    self.maxEqualTeamStdDev += (self.lowerBound - graded.equalResult) ** 2
            self.maxWeightedTeamStdDev /= self.totalGradedTeamWeight
            self.maxWeightedTeamStdDev = m.sqrt(self.maxWeightedTeamStdDev)
            self.maxEqualTeamStdDev /= self.nbGradedTeams
            self.maxEqualTeamStdDev = m.sqrt(self.maxEqualTeamStdDev)

    def computeInertia(self):
        """Computes the inertia values

        - weightedUserInertia
        - equalUserInertia
        - weightedTeamInertia
        - equalTeamInertia
        """
        # Users
        for grader in self.userGraders.values():
            self.weightedUserInertia += grader.weightedStdDev ** 2 * jr.getUserWeight(self._jsonData, grader.id)
            self.equalUserInertia += grader.equalStdDev ** 2
        self.weightedUserInertia /= self.totalUserGradersWeight
        self.equalUserInertia /= self.nbGraders
        # Teams
        if self.nbGradersTeam:
            for grader in self.teamGraders.values():
                self.weightedTeamInertia += grader.weightedStdDev ** 2 * jr.getTeamWeights(self._jsonData)[grader.id]
                self.equalTeamInertia += grader.equalStdDev ** 2
            self.weightedTeamInertia /= self.totalTeamsGradersWeight
            self.equalTeamInertia /= self.nbGradersTeam

    def calculateIndividualRatios(self):
        """computes the individual ratios values, for all graders
        """
        for grader in self.userGraders.values():
            grader.calculateRatios()
        for grader in self.teamGraders.values():
            grader.calculateRatios()

    def setAnswer(self, answerFile=None):
        """creates the json answer with all computed data

        @param answerFile : only used for tests, give the name of the answer file
        set the data in self.jsonResponse
        if answerFile is not None, write the json answer in the indicated file
        """
        self.result = {
            "averageUsersWeightedResult": round(self.averageUsersWeightedResult, 2),
            "averageUsersEqualResult": round(self.averageUsersEqualResult, 2),
            "averageTeamsWeightedResult": round(self.averageTeamsWeightedResult, 2),
            "averageTeamsEqualResult": round(self.averageTeamsEqualResult, 2),
            # RelativeResult
            "averageUsersWeightedRelativeResult": round(self.averageUsersWeightedRelativeResult, 2),
            "averageUsersEqualRelativeResult": round(self.averageUsersEqualRelativeResult, 2),
            "averageTeamsWeightedRelativeResult": round(self.averageTeamsWeightedRelativeResult, 2),
            "averageTeamsEqualRelativeResult": round(self.averageTeamsEqualRelativeResult, 2),
            # StdDev
            "averageUsersWeightedStdDev": round(self.averageWeightedUserStdDev, 2),
            "averageUsersEqualStdDev": round(self.averageEqualUserStdDev, 2),
            "averageTeamsWeightedStdDev": round(self.averageWeightedTeamStdDev, 2),
            "averageTeamsEqualStdDev": round(self.averageEqualTeamStdDev, 2),
            # Max stdDev
            "maxUsersWeightedStdDev": round(self.maxWeightedUserStdDev, 2),
            "maxUsersEqualStdDev": round(self.maxEqualUserStdDev, 2),
            "maxTeamsWeightedStdDev": round(self.maxWeightedTeamStdDev, 2),
            "maxTeamsEqualStdDev": round(self.maxEqualTeamStdDev, 2),
            # Inertia
            "weightedUserInertia": round(self.weightedUserInertia, 2),
            "equalUserInertia": round(self.equalUserInertia, 2),
            "weightedTeamInertia": round(self.weightedTeamInertia, 2),
            "equalTeamInertia": round(self.equalTeamInertia, 2),
            # maxInertia
            "maxWeightedUserInertia": round(self.maxWeightedUserStdDev ** 2, 2),
            "maxEqualUserInertia": round(self.maxEqualUserStdDev ** 2, 2),
            "maxWeightedTeamInertia": round(self.maxWeightedTeamStdDev ** 2, 2),
            "maxEqualTeamInertia": round(self.maxEqualTeamStdDev ** 2, 2),
            # dev Ratio
            "weightedUserDevRatio": round(self.weightedUserDevRatio, 2),
            "equalUserDevRatio": round(self.eqalUserDevRatio, 2),
            "weightedTeamDevRatio": round(self.weightedTeamDevRatio, 2),
            "equalTeamDevRatio": round(self.equalTeamDevRatio, 2),
            "user": {},
            "team": {}}
        # UserResult
        for user_id, userData in self.GradedUser.items():
            self.result["user"][user_id] = {}
            self.result["user"][user_id]["weightedResult"] = round(userData.weightedResult, 2)
            self.result["user"][user_id]["equalResult"] = round(userData.equalResult, 2)
            self.result["user"][user_id]["weightedRelativeResult"] = round(
                (userData.weightedResult - self.lowerBound) / (self.upperBound - self.lowerBound), 2)
            self.result["user"][user_id]["equalRelativeResult"] = round(
                (userData.equalResult - self.lowerBound) / (self.upperBound - self.lowerBound), 2)
        # TeamResult
        if self.nbGradedTeams:
            for team_id, teamData in self.GradedTeam.items():
                self.result["team"][team_id] = {}
                self.result["team"][team_id]["weightedResult"] = round(teamData.weightedResult, 2)
                self.result["team"][team_id]["equalResult"] = round(teamData.equalResult, 2)
                self.result["team"][team_id]["weightedRelativeResult"] = round(
                    (teamData.weightedResult - self.lowerBound) / (self.upperBound - self.lowerBound), 2)
                self.result["team"][team_id]["equalRelativeResult"] = round(
                    (teamData.equalResult - self.lowerBound) / (self.upperBound - self.lowerBound), 2)

        # user deviations
        for user_id, userData in self.userGraders.items():
            if not user_id in self.result["user"].keys():
                self.result["user"][user_id] = {}
            # StdDev
            self.result["user"][user_id]["weightedStdDev"] = round(userData.weightedStdDev, 2)
            self.result["user"][user_id]["equalStdDev"] = round(userData.equalStdDev, 2)
            # Ratios
            self.result['user'][user_id]["weightedDevRatio"] = round(userData.weightedDevRatio, 2)
            self.result['user'][user_id]["equalDevRatio"] = round(userData.equalDevRatio, 2)
        # teams deviation
        for team_id, teamData in self.teamGraders.items():
            if not team_id in self.result["team"].keys():
                self.result["team"][team_id] = {}
            # stdDev
            self.result["team"][team_id]["weightedStdDev"] = round(teamData.weightedStdDev, 2)
            self.result["team"][team_id]["equalStdDev"] = round(teamData.equalStdDev, 2)
            # ratios
            self.result['team'][team_id]["weightedDevRatio"] = round(teamData.weightedDevRatio, 2)
            self.result['team'][team_id]["equalDevRatio"] = round(teamData.equalDevRatio, 2)
        self.jsonResponse = json.dumps(self.result, ensure_ascii=False, indent=4)
        # Write the json in a file (for tests only)
        if answerFile is not None:
            with open(answerFile, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, ensure_ascii=False, indent=4)
