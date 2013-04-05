from goals import Goal

class Plan:
    """Classe abstraite représentant une séquence d'action: un plan"""

    def __init__(self, goal):
        self.assignGoal = goal.goalString
        self.value = 0.5;
        self.actionSequence = []

    def executePlan():
        abstract

    def isPlanValid():
        abstract
