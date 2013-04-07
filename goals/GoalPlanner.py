from api import gameinfo
from goals.Goal import Goal
from goals.GoalGetEnemyFlag import GoalGetEnemyFlag
from goals.GoalKillAnyone import GoalKillAnyone
from goals.GoalKillFlagCarrier import GoalKillFlagCarrier
from goals.GoalKillSpecificDefender import GoalKillSpecificDefender
from goals.GoalProtectFlagCarrier import GoalProtectFlagCarrier
from goals.GoalBringBackEnemyFlag import GoalBringBackEnemyFlag

# TODO: Limiter le nombre de bot pour chaque goal?

class GoalPlanner:
    """Conteneur des buts et méthode pour trouver le plus utile"""

    def __init__(self, gameInfo):
        self.goals = [GoalKillAnyone(gameInfo), GoalKillSpecificDefender(gameInfo), GoalKillFlagCarrier(gameInfo), GoalGetEnemyFlag(gameInfo), GoalProtectFlagCarrier(gameInfo), GoalBringBackEnemyFlag(gameInfo)]
        self.game = gameInfo

    def findMostRevelantGoal(self,bot):
        # Valeur d'utilite par defaut
        mostRelevant = -1

        # Le but le plus utile dans le contexte actuel
        doGoal = Goal(self.game)
        
        # Itere sur tous les buts pour trouver le plus utile
        for goal in self.goals:
            utility = goal.calculateUtility(bot)
            if mostRelevant < utility:
                mostRelevant = utility
                doGoal = goal

        return doGoal