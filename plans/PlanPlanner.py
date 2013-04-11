from api import gameinfo
from PlanGetEnemyFlag import PlanGetEnemyFlag
from plans.PlanProtectFlagCarrier import PlanProtectFlagCarrier
from plans.PlanBringBackEnemyFlag import PlanBringBackEnemyFlag
from plans.PlanProtectFlag import PlanProtectFlag
from plans.PlanKillFlagCarrier import PlanKillFlagCarrier
from Blackboard import Blackboard

import copy

class PlanPlanner(object):
    """Classe pour déterminer le bon plan à utiliser pour résoudre le but"""
    
    def __init__(self, gameInfo):
        self.planAvailable = {}
        self.planAvailable["GetEnemyFlag"] = [PlanGetEnemyFlag(gameInfo)]
        self.planAvailable["ProtectFlagCarrier"] = [PlanProtectFlagCarrier(gameInfo)]
        self.planAvailable["BringBackEnemyFlag"] = [PlanBringBackEnemyFlag(gameInfo)]
        self.planAvailable["ProtectFlag"] = [PlanProtectFlag(gameInfo)]
        self.planAvailable["KillFlagCarrier"] = [PlanKillFlagCarrier(gameInfo)]

        self.gameInfo = gameInfo

    def choosePlan(self, bot, blackboard):
        #Choisi le meilleur plan remplissant le but
        goal = blackboard.botsAssignGoal[bot.name]
        for planIteration in self.planAvailable[goal]:
            if planIteration.assignGoal == goal:
                plan = copy.deepcopy(self.planAvailable[goal][0])

                #Set la sequence parce que le target est variable
                plan.setSequence(bot, blackboard)

        return plan

    def addPlan(self, goal, actionSequence):
        pass


