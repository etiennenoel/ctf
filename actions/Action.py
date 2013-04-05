class Action(object):
    """Classe abstraite encapsulant les informations liées à une action"""

    def __init__(self):
        self.command = ""
        self.description = ""
        self.target= ""
