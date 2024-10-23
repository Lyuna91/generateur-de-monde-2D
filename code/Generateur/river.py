from .pixel import Pixel

class River:
    """
    classe permettant de définir les rivières.
    """

######################### INIT
    def __init__(self, id, size, pixels):
        """
        Initialise une rivière avec ses caractéristiques de base.
        
        :param id: Identifiant unique de la rivière
        :param size: La taille de la rivière
        :param pixels: La liste des pixels de la rivière
        """
        self.id = id
        self.size = size
        self.pixels = pixels

    def __repr__(self):
        """
        Retourne une représentation de la rivière sous forme de string.
        """
        return f"River(id={self.id}, size={self.size}, pixels={self.pixels})"
    
######################### METHODS

    def create_river(self):
        pass
        