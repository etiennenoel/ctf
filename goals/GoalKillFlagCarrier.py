from Goal import Goal
from api import gameinfo 

# TODO: Si on est plus proche du flag position, alors on choisi ce but sinon on va protéger leur capture point

class GoalKillFlagCarrier(Goal):
    """Classe représentant le but d'aller tuer l'ennemi possédant notre flag"""

    def __init__(self, gameInfo):
        """Methode pour initialiser le but"""
        Goal.__init__(self, gameInfo)
        self.goalString = "KillFlagCarrier"
        self.defaultValue = 70

    def calculateUtility(self, bot, blackboard):
        """Methode permettant de calculer l'utilite du but de tuer le flag carrier"""
        if self.gameInfo.team.flag.carrier is not None:
            enemyDistanceToScoreZone = self.gameInfo.team.flag.position.distance(self.gameInfo.enemyTeam.flagScoreLocation)
            botDistanceToEnemy = bot.position.distance(self.gameInfo.team.flag.position)

            distanceConstant = 5
            distanceScore = (enemyDistanceToScoreZone/botDistanceToEnemy)*5

            score = self.defaultValue + distanceScore

            if blackboard.botsAssignGoal[bot.name] == 'ProtectFlag':
                score += 35

            return score

        else:
            return 0

