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

    def calculateUtility(self, bot):
        """Methode permettant de calculer l'utilite du but d'aller chercher leur flag"""

        enemyTeamFlag = self.gameInfo.enemyTeam.name + "Flag"
        if self.gameInfo.flags[enemyTeamFlag].carrier is None:
            return 1
        else:
            return 0

