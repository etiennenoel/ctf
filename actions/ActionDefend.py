from Action import Action
from api import commands

class ActionDefend(Action):
    """Objet représentant l'action de défendre"""

    def __init__(self, target):
        Action.__init__(self)
        self.command = commands.Defend
        self.target = target
        self.description = "Defend position"


