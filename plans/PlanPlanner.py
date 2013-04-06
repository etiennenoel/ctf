from api import gameinfo
from PlanGetEnemyFlag import PlanGetEnemyFlag
import copy

class PlanPlanner(object):
    """Classe pour déterminer le bon plan à utiliser pour résoudre le but"""
    
    def __init__(self, gameInfo):
        self.planAvailable = [PlanGetEnemyFlag(gameInfo)]
        self.gameInfo = gameInfo

    def choosePlan(self, goal):
        plan = copy.deepcopy(self.planAvailable[0])
        return plan

    def addPlan(self, goal, actionSequence):
        pass


