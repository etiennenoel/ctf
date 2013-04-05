class Goal:
    """Classe abstraite représentant un but"""

    ##################################################################################
    ## Function   : initialize
    ## Description: Methode pour initialiser le but 
    ## Parametres : self
    ##              gameInfo: informations sur la partie
    ##################################################################################    
    def __init__(self, gameInfo):
        self.gameInfo = gameInfo
        self.goalString = ""

    ##################################################################################
    ## Function   : calculteUtility
    ## Description: Methode permettant de calculer l'utilite du but
    ## Parametres : self
    ##################################################################################   
    def calculateUtility(self):
        abstract

