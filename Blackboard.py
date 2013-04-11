
class Blackboard(object):
    """
    Informations inter bot
    Contient des informations qui permettra à un bot de connaître 
    ce qui l'entour afin de choisir un but et un plan éclairés.
    """

    def __init__(self, hidingLocations, level, commander):
        # Informations sur les cachettes (kill, death, bot a la position, position)
        self.hidingLocations = hidingLocations

        # Pour connaitre le but de chaque bot
        self.botsAssignGoal = {}

        # Informations sur la carte en cours
        self.level = level
        
        # Nombre de defenseurs
        self.numberOfDefender = 0
        self.actualDefender = 0 

        # commander pour pouvoir log
        self.commander = commander

