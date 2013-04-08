from api import commands
from api import gameinfo
from Plan import Plan
from actions.ActionCharge import ActionCharge

class PlanGetEnemyFlag(Plan):
    """Des plans possibles pour atteindre le but d'aller chercher le flag"""

    def __init__(self, gameInfo):
        Plan.__init__(self, "GetEnemyFlag", gameInfo)
        
    def setSequence(self, bot, blackboard):
        self.actionSequence = [ActionCharge(self.gameInfo.enemyTeam.flag.position)]
