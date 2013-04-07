
class Blackboard(object):
    """Contient des informations qui permettra à un bot de connaître 
    ce qui l'entour afin de choisir un but et un plan éclairés"""

    def __init__(self, hidingSpot):
        self.hidingSpot = hidingSpot
        self.botsAssignGoal = {}
