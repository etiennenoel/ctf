from Goal import Goal
from api import gameinfo 

class GoalGetEnemyFlag(Goal):
    """Représente le but d'aller chercher le flag ennemi"""

    ##################################################################################
    ## Function   : initialize
    ## Description: Methode pour initialiser le but 
    ## Parametres : self
    ##              gameInfo: informations sur la partie
    ##################################################################################
    def __init__(self, gameInfo):
        Goal.__init__(self, gameInfo)
        self.goalString = "GetEnemyFlag"

    ##################################################################################
    ## Function   : calculteUtility
    ## Description: Methode permettant de calculer l'utilite du but d'aller chercher leur flag
    ## Parametres : self
    ##################################################################################   
    def calculateUtility(self):
        enemyTeamFlag = self.gameInfo.enemyTeam.name + "Flag"
        if self.gameInfo.flags[enemyTeamFlag].carrier is None:
            return 1
        else:
            return 0

