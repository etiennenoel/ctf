import random

from api import commands
from api import gameinfo

from Plan import Plan
from actions.ActionAttack import ActionAttack
from actions.ActionCharge import ActionCharge
from Blackboard import Blackboard

class PlanProtectFlagCarrier(Plan):
    """Des plans possibles pour atteindre le but de protéger le flag carrier"""

    def __init__(self, gameInfo):
        Plan.__init__(self, "ProtectFlagCarrier", gameInfo)

    def setSequence(self, bot, blackboard):
        botName = self.gameInfo.enemyTeam.flag.carrier
        if not botName is None:
            #self.gameInfo.enemyTeam.flag.carrier.position
            #,random.choice([b.position for b in bot.visibleEnemies])
            self.actionSequence = [ActionAttack(self.gameInfo.team.flagScoreLocation)]
        

