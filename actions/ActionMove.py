from Action import Action
from api import commands

class ActionMove(Action):
    """Objet représentant l'action de bouger à une position sans attaquer"""

    def __init__(self, target):
        Action.__init__(self)
        self.command = commands.Move
        self.target = target
        self.params['description'] = 'Move'


