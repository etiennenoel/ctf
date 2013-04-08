from api import commands
from api import gameinfo
from Plan import Plan
from actions.ActionAttack import ActionAttack

class PlanBringBackEnemyFlag(Plan):
    """Des plans possibles pour ramener le flag"""

    def __init__(self, gameInfo):
        Plan.__init__(self, "BringBackEnemyFlag", gameInfo)
        
    def setSequence(self, bot, blackboard):
        self.actionSequence = [ActionAttack(self.gameInfo.team.flagScoreLocation)]
