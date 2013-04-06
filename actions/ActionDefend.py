from Action import Action
from api import commands

class ActionDefend(Action):
    """Objet représentant l'action de défendre"""

    def __init__(self, target):
        Action.__init__(self)

        #Command
        self.command = commands.Defend

        #Facing direction
        self.target = target

        #Parametres supplementaires
        self.params['description'] = 'Defend'


