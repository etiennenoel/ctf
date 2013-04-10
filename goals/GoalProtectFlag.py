from Goal import Goal
from api import gameinfo 

#TODO: Nombre de bot defending

class GoalProtectFlag(Goal):
    """Classe représentant le but de protéger notre flag"""

    def __init__(self, gameInfo):
        """Methode pour initialiser le but"""
        Goal.__init__(self, gameInfo)
        self.goalString = "ProtectFlag"

    def calculateUtility(self, bot, blackboard):
        """Methode permettant de calculer l'utilité de protéger notre flag"""
        if blackboard.actualDefender < blackboard.numberOfDefender:
            return 100
        else:
            return 0

