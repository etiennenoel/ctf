from Action import Action
from api import commands

class ActionCharge(Action):
    """Objet représentant l'action de charger une position"""

    def __init__(self, target):
        Action.__init__(self)
        self.command = commands.Charge
        self.target = target
        self.description = "Charge position"


