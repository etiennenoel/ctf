from api import commands
from api import gameinfo
from Plan import Plan
from actions.ActionCharge import ActionCharge

class PlanGetEnemyFlag(Plan):
    """Des plans possibles pour atteindre le but d'aller chercher le flag"""

    def __init__(self, gameInfo):
        Plan.__init__(self, "GetEnemyFlag", gameInfo)

    def isPlanValid(self):
        if self.gameInfo.enemyTeam.flag.carrier is not None:
            return false
        elif self.currentActionIndex < len(self.actionSequence):
            return True
        else:
            self.currentActionIndex = 0
            return False
        
    def setSequence(self, bot, blackboard):
        self.actionSequence = [ActionCharge(self.gameInfo.enemyTeam.flag.position)]
