from Goal import Goal
from api import gameinfo 

class GoalKillAnyone(Goal):
    """But d'aller à la recherche de quelqu'un à tuer"""

    def __init__(self, gameInfo):
        """Méthode pour initialiser le but"""
        Goal.__init__(self, gameInfo)
        self.goalString = "KillAnyone"

    def calculateUtility(self, bot):
        """Méthode permettant de calculer l'utilité d'aller en mode tuerie"""
        return 0