import sys
import math

from api import commands
from api import gameinfo
from api import Vector2
from Plan import Plan
from actions.ActionAttack import ActionAttack
from actions.ActionCharge import ActionCharge
from actions.ActionDefend import ActionDefend

#TODO: LOS bloquer
#TODO: se mettre le plus proche du mur possible et pas au milieu
#TODO: en cas d'égalité, le plus proche de nous et celui avec le meilleur rating
#TODO: Sweep
#TODO: si la case est déjà pris: stacker ou en prendre un autre?

class PlanProtectFlag(Plan):
    """Plan pour protéger le flag"""

    def __init__(self, gameInfo):
        """Méthode pour initialiser le plan"""
        Plan.__init__(self, "ProtectFlag", gameInfo)

    def setSequence(self, bot, blackboard):
        # On trouve la meilleur cachette pour défendre le flag
        bestDistanceToFlag = sys.maxint
        flagPosition = self.gameInfo.team.flag.position

        for square in blackboard.hidingSpot:
            # distance entre la case et le flag
            distance = flagPosition.distance(square)
            if distance == bestDistanceToFlag:
                # si egaliter, on choisi la case la plus proche du bot
                if bot.position.distance(square) < bot.position.distance(bestSquare):
                    bestDistanceToFlag = distance
                    bestSquare = square

            elif distance < bestDistanceToFlag:
                bestDistanceToFlag = distance
                bestSquare = square

        # On set la sequence d'actions pour se rendre a la position et se mettre en defend
        targetSquare = blackboard.level.findNearestFreePosition(bestSquare)
        self.actionSequence = [ActionCharge(targetSquare),ActionDefend([flagPosition - targetSquare])]


