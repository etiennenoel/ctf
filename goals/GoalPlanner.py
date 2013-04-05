from api import gameinfo
from goals.Goal import Goal
from goals.GoalGetEnemyFlag import GoalGetEnemyFlag
from goals.GoalKillAnyone import GoalKillAnyone
from goals.GoalKillFlagCarrier import GoalKillFlagCarrier
from goals.GoalKillSpecificDefender import GoalKillSpecificDefender

class GoalPlanner:
    """Conteneur des buts et méthode pour trouver le plus utile"""

    def __init__(self, gameInfo):
        self.goals = [GoalKillAnyone(gameInfo), GoalKillSpecificDefender(gameInfo), GoalKillFlagCarrier(gameInfo), GoalGetEnemyFlag(gameInfo)]
        self.game = gameInfo

    def findMostRevelantGoal(self):
        # Valeur d'utilite par defaut
        mostRelevant = -1

        # Le but le plus utile dans le contexte actuel
        doGoal = Goal(self.game)
        
        # Itere sur tous les buts pour trouver le plus utile
        for goal in self.goals:
            utility = goal.calculateUtility()
            if mostRelevant < goal.calculateUtility():
                mostRelevant = utility
                doGoal = goal

        return doGoal