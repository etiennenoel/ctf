from api import commands
from api import gameinfo

class PlanGetEnemyFlag:
    """Des plans possibles pour atteindre le but d'aller chercher le flag"""

    def __init__(self, gameInfo):
        self.chargePath = [(commands.Charge, gameInfo.enemyTeam.flagSpawnLocation, "Charge sur leur flag")]
        self.movePath = [(commands.Move, gameInfo.enemyTeam.flagSpawnLocation), "Move a leur flag"]

