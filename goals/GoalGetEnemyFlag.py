from Goal import Goal
from api import gameinfo 

# Score: si on gagne, l'utilite diminue
# Temps: vers la fin de la game, si on est en train de gagne, l'utilite diminue
# Distance entre le bot et le flag

class GoalGetEnemyFlag(Goal):
    """Représente le but d'aller chercher le flag ennemi"""

    def __init__(self, gameInfo):
        """Methode pour initialiser le but """

        Goal.__init__(self, gameInfo)
        self.goalString = "GetEnemyFlag"
        self.defaultValue = 50

    def calculateUtility(self, bot, blackboard):
        """Methode permettant de calculer l'utilité d'aller chercher leur flag"""
        enemyTeamFlag = self.gameInfo.enemyTeam.name + "Flag"
        if self.gameInfo.flags[enemyTeamFlag].carrier is None:

            # score et temps
            STConstant = 3
            goalDifference= (self.gameInfo.match.scores[self.gameInfo.team.name] - self.gameInfo.match.scores[self.gameInfo.enemyTeam.name])
            STValue = goalDifference * (self.gameInfo.match.timeRemaining - blackboard.level.gameLength) * STConstant

            # nombre de bot qui ont déjà cet ordre
            BotConstant = 2
            numberOfBot = 0
            for goal in blackboard.botsAssignGoal.values():
                if goal == self.goalString:
                    numberOfBot += 1

            BotValue = numberOfBot * BotConstant

            # Total value
            blackboard.commander.log.info(self.goalString + " " + str(self.defaultValue - STValue - BotValue))
            return self.defaultValue - STValue - BotValue
        else:
            return 0

