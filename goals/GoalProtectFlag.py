from Goal import Goal
from api import gameinfo 

#TODO: Nombre de bot defending

class GoalProtectFlag(Goal):
    """Classe représentant le but de protéger notre flag"""

    def __init__(self, gameInfo):
        """Methode pour initialiser le but"""
        Goal.__init__(self, gameInfo)
        self.goalString = "ProtectFlag"
        self.defaultValue = 30

    def calculateUtility(self, bot, blackboard):
        """Methode permettant de calculer l'utilité de protéger notre flag"""

        # Si le flag a ete pris
        if not self.gameInfo.team.flag.position == self.gameInfo.team.flagSpawnLocation:
            # A terre?
            if self.gameInfo.team.flag.carrier is not None:
                return 0
            else:
                # Proteger le flag jusqu'a temps qu'il revient a la base
                return self.defaultValue

        # Avoir un minimum de defenseur
        elif blackboard.actualDefender < blackboard.numberOfDefender:
            return 100
        else:
            return self.defaultValue
            

