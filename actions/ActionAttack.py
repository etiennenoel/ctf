from Action import Action
from api import commands

class ActionAttack(Action):
    """Objet représentant l'action d'attaquer"""

    def __init__(self, target):
        Action.__init__(self)
        self.command = commands.Attack
        self.target = target
        self.description = "Attack position"


