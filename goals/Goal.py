class Goal:
    """Classe abstraite représentant un but"""

    def __init__(self, gameInfo):
        """Methode pour initialiser le but"""
        self.gameInfo = gameInfo
        self.goalString = ""

    def calculateUtility(self, bot, blackboard):
        """Methode abstraite permettant de calculer l'utilite du but"""
        abstract

