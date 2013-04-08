from Goal import Goal
from api import gameinfo 

# TODO: Si on est plus proche du flag position, alors on choisi ce but sinon on va protéger leur capture point

class GoalKillFlagCarrier(Goal):
    """Classe représentant le but d'aller tuer l'ennemi possédant notre flag"""

    def __init__(self, gameInfo):
        """Methode pour initialiser le but"""
        Goal.__init__(self, gameInfo)
        self.goalString = "KillFlagCarrier"

    def calculateUtility(self, bot, blackboard):
        """Methode permettant de calculer l'utilite du but de tuer le flag carrier"""
        if self.gameInfo.team.flag.carrier is not None:
            return 0.4
        else:
            return 0

