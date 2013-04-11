from Goal import Goal
from api import gameinfo 
from Blackboard import Blackboard

class GoalBringBackEnemyFlag(Goal):
    """Classe représentant le but d'aller scorer un point si le bot a le flag en sa possession"""

    def __init__(self, gameInfo):
        """Methode pour initialiser le but"""
        Goal.__init__(self, gameInfo)
        self.goalString = "BringBackEnemyFlag"

    def calculateUtility(self, bot, blackboard):
        """Methode permettant de calculer l'utilité de ramener le flag"""
        if bot.flag:
            return 100
        else:
            return 0