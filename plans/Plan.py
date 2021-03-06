﻿from goals import Goal

class Plan:
    """Classe abstraite représentant une séquence d'action: un plan"""

    def __init__(self, goalString, gameInfo):
        self.assignGoal = goalString
        self.value = 0.5;
        self.actionSequence = []
        self.currentActionIndex = 0
        self.target = ""
        self.gameInfo = gameInfo

    def executePlan(self):
        action = self.actionSequence[self.currentActionIndex]
        self.currentActionIndex += 1
        return action

    def isPlanValid(self):
        if self.currentActionIndex < len(self.actionSequence):
            return True
        else:
            self.currentActionIndex = 0
            return False

    def setSequence(self, bot):
        abstract
