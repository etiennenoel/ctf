from Goal import Goal
from api import gameinfo 

#TODO: Nombre de bot defending: au début tout le monde va protéger notre flag et les restants vont partir à l'attaque

class GoalProtectFlag(Goal):
    """Classe représentant le but de protéger notre flag"""

    def __init__(self, gameInfo):
        """Methode pour initialiser le but"""
        Goal.__init__(self, gameInfo)
        self.goalString = "ProtectFlag"

    def calculateUtility(self, bot, blackboard):
        """Methode permettant de calculer l'utilité de protéger notre flag"""
        return 0.5

