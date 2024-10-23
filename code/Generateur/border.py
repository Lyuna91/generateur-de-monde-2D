from .pixel import Pixel
class Border :

######################### INIT

    def __init__(self, id, countries, size, pixels):
        """
        Initialise une frontière avec ses caractéristiques de base.
        
        :param id: Identifiant unique de la frontière
        :param countries: Les deux pays séparés par la frontière
        :param size: La taille de la frontière
        :param pixels: La liste des pixels de la frontière
        """
        self.id = id
        self.country = countries
        self.size = size
        self.pixels = pixels

    def __repr__(self):
        """
        Retourne une représentation de la frontière sous forme de string.
        """
        return f"Border(id={self.id}, countries={self.countries}, size={self.size}, pixels={self.pixels})"

######################### METHODS
    def create_border(self):
        pass
