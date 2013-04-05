from Goal import Goal
from api import gameinfo 

class GoalGetEnemyFlag(Goal):
    """description of class"""
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
        return 1

