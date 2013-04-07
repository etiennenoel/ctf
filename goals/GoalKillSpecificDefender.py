from Goal import Goal
from api import gameinfo 

#TODO: l'utilite augmente si on se fait tuer par le meme ennemie plusieurs fois a la meme place

class GoalKillSpecificDefender(Goal):
    """Représente le but de tuer un defender ennemie"""

    def __init__(self, gameInfo):
        """Méthode pour initialiser le but"""
        Goal.__init__(self, gameInfo)
        self.goalString = "KillSpecificDefender"

    def calculateUtility(self, bot, blackboard):
        """Méthode permettant de calculer l'utilité de tuer un defenseur précis"""
        return 0

