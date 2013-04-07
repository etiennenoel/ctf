from Goal import Goal
from api import gameinfo 

class GoalBringBackEnemyFlag(Goal):
    """Classe représentant le but d'aller scorer un point si le bot a le flag en sa possession"""

    def __init__(self, gameInfo):
        """Methode pour initialiser le but"""
        Goal.__init__(self, gameInfo)
        self.goalString = "BringBackEnemyFlag"

    def calculateUtility(self, bot):
        """Methode permettant de calculer l'utilité de ramener le flag"""
        carrier = self.gameInfo.enemyTeam.flag.carrier
        if carrier is not None and bot == carrier:
            return 1
        else:
            return 0