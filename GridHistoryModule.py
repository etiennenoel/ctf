
class GridHistoryModule(Object):
    """
    Classe responsable de maintenir l'information sur les cases de la carte. Pour chaque
    case, on conserve le nombre de fois où un ennemi a été aperçu en train de se déplacer (Move, Attack, Charge),
    le nombre de fois où un ennemi a été vu en train de défendre (Defend), et le nombre de fois où un allié
    s'est fait tué.
    """

    def __init__(self):
        pass