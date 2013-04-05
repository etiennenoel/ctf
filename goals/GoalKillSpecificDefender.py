from Goal import Goal
from api import gameinfo 

class GoalKillSpecificDefender(Goal):
    """description of class"""
    ##################################################################################
    ## Function   : initialize
    ## Description: Methode pour initialiser le but 
    ## Parametres : self
    ##              gameInfo: informations sur la partie
    ##################################################################################
    def __init__(self, gameInfo):
        Goal.__init__(self, gameInfo)
        self.goalString = "KillSpecificDefender"

    ##################################################################################
    ## Function   : calculteUtility
    ## Description: Methode permettant de calculer l'utilite du but de tuer un defenseur precis
    ## Parametres : self
    ##################################################################################   
    def calculateUtility(self):
        return 0

