
class GridHistoryModule(Object):
    """
    Classe responsable de maintenir l'information sur les cases de la carte. Pour chaque
    case, on conserve le nombre de fois o� un ennemi a �t� aper�u en train de se d�placer (Move, Attack, Charge),
    le nombre de fois o� un ennemi a �t� vu en train de d�fendre (Defend), et le nombre de fois o� un alli�
    s'est fait tu�.
    """

    def __init__(self):
        pass