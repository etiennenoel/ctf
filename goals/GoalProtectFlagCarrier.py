from Goal import Goal
from api import gameinfo 

class GoalProtectFlagCarrier(Goal):
    """Représente le but de protéger le flag carrier"""

    def __init__(self, gameInfo):
        """Méthode pour initialiser le but"""
        Goal.__init__(self, gameInfo)
        self.goalString = "ProtectFlagCarrier"

    def calculateUtility(self, bot, blackboard):
        """Méthode permettant de calculer l'utilité de protéger le flag carrier"""
        enemyTeamFlag = self.gameInfo.enemyTeam.name + "Flag"
        if not self.gameInfo.flags[enemyTeamFlag].carrier is None:
            return 0.5
        else:
            return 0