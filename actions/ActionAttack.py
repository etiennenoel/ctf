from Action import Action
from api import commands

class ActionAttack(Action):
    """Objet représentant l'action d'attaquer"""

    def __init__(self, target, lookAt = None):
        Action.__init__(self)
        self.command = commands.Attack
        self.target = target

        self.params['description'] = 'Attack'

        if lookAt is not None:
            self.params['lookAt'] = lookAt


