from Goal import Goal
from api import gameinfo 
import math

class GoalProtectFlagCarrier(Goal):
    """Représente le but de protéger le flag carrier"""

    def __init__(self, gameInfo):
        """Méthode pour initialiser le but"""
        Goal.__init__(self, gameInfo)
        self.goalString = "ProtectFlagCarrier"
        self.defaultValue = 0 

    def calculateUtility(self, bot, blackboard):
        """Méthode permettant de calculer l'utilité de protéger le flag carrier"""

        # Le but est important seulement si on a leur flag
        if not self.gameInfo.enemyTeam.flag.carrier is None:
            score = 0 

            # Regarde si on est un défenseur ou un attaquant
            if blackboard.botsAssignGoal[bot.name] == "ProtectFlag":
                score += 40
            else:
                score += 75

            # Regarde la distance du bot avec le flag carrier
            DistanceConstant = 10
            distance = bot.position.distance(self.gameInfo.enemyTeam.flag.carrier.position)

            if not math.floor(distance) == 0: #pour ne pas avoir une division par 0
                score += DistanceConstant / distance

            return self.defaultValue + score
        else:
            return 0