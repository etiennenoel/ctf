from api import gameinfo
from PlanGetEnemyFlag import PlanGetEnemyFlag
from plans.PlanProtectFlagCarrier import PlanProtectFlagCarrier
import copy

class PlanPlanner(object):
    """Classe pour déterminer le bon plan à utiliser pour résoudre le but"""
    
    def __init__(self, gameInfo):
        self.planAvailable = {}
        self.planAvailable["GetEnemyFlag"] = [PlanGetEnemyFlag(gameInfo)]
        self.planAvailable["ProtectFlagCarrier"] = [PlanProtectFlagCarrier(gameInfo)]

        self.gameInfo = gameInfo

    def choosePlan(self, goal, bot):
        #Choisi le meilleur plan remplissant le but
        for planIteration in self.planAvailable[goal.goalString]:
            if planIteration.assignGoal == goal.goalString:
                plan = copy.deepcopy(self.planAvailable[goal.goalString][0])

                #Set la sequence parce que le target est variable
                plan.setSequence(bot)

        return plan

    def addPlan(self, goal, actionSequence):
        pass


