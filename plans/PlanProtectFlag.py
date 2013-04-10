import sys
import math
from random import choice
from copy import deepcopy

from api import commands
from api import gameinfo
from api import Vector2
from Plan import Plan
from actions.ActionAttack import ActionAttack
from actions.ActionCharge import ActionCharge
from actions.ActionDefend import ActionDefend

#TODO: LOS bloquer
#TODO: Sweep
#TODO: si pas de cachette, se mettre sur le flag
#TODO: distance minimale depend du range
#TODO: si le flag etait tomber, et quil est revenu a notre base, rechercher une nouvelle cachette pres du flag

class PlanProtectFlag(Plan):
    """Plan pour protéger le flag"""

    def __init__(self, gameInfo):
        """Méthode pour initialiser le plan"""
        Plan.__init__(self, "ProtectFlag", gameInfo)

    def setSequence(self, bot, blackboard):
        # On trouve la meilleur cachette pour défendre le flag
        bestDistanceToFlag = sys.maxint
        flagPosition = self.gameInfo.team.flag.position

        ## Faire une liste de toutes les positions entre une borne superieur et inferieure
        possibleLocation = []
        for square in blackboard.hidingLocations:
            distance = flagPosition.distance(square.position)
            # TODO: minimum distance en lien avec l'angle
            if distance < blackboard.level.firingDistance and distance > 2.0:
                possibleLocation.append(square)

        ## Prendre celui avec le meilleur score ou sinon random
        bestSquare = choice(possibleLocation)

        #for square in blackboard.hidingLocations:
        #    # distance entre la case et le flag
        #    distance = flagPosition.distance(square.position)
        #    if distance == bestDistanceToFlag:
        #        # si egaliter, on choisi la case la plus proche du bot
        #        if bot.position.distance(square.position) < bot.position.distance(bestSquare.position):
        #            bestDistanceToFlag = distance
        #            bestSquare = square

        #    elif distance < bestDistanceToFlag:
        #        bestDistanceToFlag = distance
        #        bestSquare = square

        # On set la sequence d'actions pour se rendre a la position et se mettre en defend
        #targetSquareLocation = blackboard.level.findNearestFreePosition(bestSquare.position)
        targetSquareLocation = deepcopy(bestSquare.position)
        targetSquareLocation.x += 0.5
        targetSquareLocation.y += 0.5
        self.actionSequence = [ActionCharge(targetSquareLocation),ActionDefend([flagPosition - targetSquareLocation])]


