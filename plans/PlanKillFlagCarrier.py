from api import commands
from api import gameinfo

from Plan import Plan
from actions.ActionAttack import ActionAttack
from actions.ActionCharge import ActionCharge
from Blackboard import Blackboard

#TODO: meilleur des cas - coupe le flag carrier dans son chemin vers le score point

class PlanKillFlagCarrier(Plan):
    """Plan pour tuer le flag carrier ennemi"""

    def __init__(self, gameInfo):
        Plan.__init__(self, "KillFlagCarrier", gameInfo)

    def setSequence(self, bot, blackboard):
        botName = self.gameInfo.team.flag.carrier
        interceptPoint = botName.position.midPoint(self.gameInfo.enemyTeam.flagScoreLocation)

        if not botName is None:
            distance = bot.position.distance(self.gameInfo.team.flag.position)
            if distance > 10:
                self.actionSequence = [ActionCharge(blackboard.level.findNearestFreePosition(interceptPoint))]
            else:
                self.actionSequence = [ActionAttack(self.gameInfo.team.flag.position)]
