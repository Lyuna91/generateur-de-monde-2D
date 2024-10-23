from .pixel import Pixel

class Road:
    """
    Classe permettant de définir les routes.
    """

######################### INIT

    def __init__(self, id, pixels):
        """
        Initialise une route avec ses caractéristiques de base.
        
        :param id: Identifiant unique de la route
        :param pixels: La liste des pixels de la route
        """
        self.id = id
        self.pixels = pixels  

    def __repr__(self):
        """
        Retourne une représentation de la route sous forme de string.
        """
        return f"Road(id={self.id}, pixels={self.pixels})"  

######################### METHODS

    def create_road(self):
        return self