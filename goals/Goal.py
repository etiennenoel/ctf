class Goal:
    """Classe abstraite représentant un but"""

    def __init__(self, gameInfo):
        """Methode pour initialiser le but"""
        self.gameInfo = gameInfo
        self.goalString = ""
        self.defaultValue = 0

    def calculateUtility(self, bot, blackboard):
        """Methode abstraite permettant de calculer l'utilite du but"""
        abstract

    def numberOfBotWithSameGoal(self, blackboard):
        # nombre de bot qui ont déjà cet ordre
        numberOfBot = 0
        for goal in blackboard.botsAssignGoal.values():
            if goal == self.goalString:
                numberOfBot += 1
        
        return numberOfBot