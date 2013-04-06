from Goal import Goal
from api import gameinfo 

class GoalProtectFlagCarrier(Goal):
    """Représente le but de protéger le flag carrier"""

    ##################################################################################
    ## Function   : initialize
    ## Description: Methode pour initialiser le but 
    ## Parametres : self
    ##              gameInfo: informations sur la partie
    ##################################################################################
    def __init__(self, gameInfo):
        Goal.__init__(self, gameInfo)
        self.goalString = "ProtectFlagCarrier"

    ##################################################################################
    ## Function   : calculteUtility
    ## Description: Methode permettant de calculer l'utilite du but de protéger le flag carrier
    ## Parametres : self
    ##################################################################################   
    def calculateUtility(self):
        enemyTeamFlag = self.gameInfo.enemyTeam.name + "Flag"
        if not self.gameInfo.flags[enemyTeamFlag].carrier is None:
            return 1
        else:
            return 0


