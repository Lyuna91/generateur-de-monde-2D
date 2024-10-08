import random

class Pixel:
    """
    Classe permettant de définir les pixels.
    """

######################### INIT

# J'ai enlevé le paramètre "zone" des paramètres, je n'arrive pas a accéder à sa classe

    def __init__(self, x, y, color, zone_id, altitude=0, element=None):
        """
        Initialise un pixel avec ses caractéristiques de base.

        :param x: Position x du pixel
        :param y: Position y du pixel
        :param color: Couleur du pixel en fonction de son biome ou élément
        :param zone: La zone à laquelle appartient le pixel
        :param altitude: Altitude du pixel
        :param element: (pas sûre) Élément supplémentaire (rivière, route, etc.) ou None si pas d'élément particulier 
        """
        self.x = x
        self.y = y
        self.color = color
        self.zone_id = zone_id  # Utilise l'ID de la zone
        self.altitude = altitude
        self.element = element


######################### SETTER

    def set_color(self, new_color):
        """
        Modifie la couleur du pixel.
        :param new_color: La nouvelle couleur du pixel
        """
        self.color = new_color

    def set_element(self, new_element):
        """
        Modifie l'élément associé au pixel.
        :param new_element: L'élément (rivière, route, frontière) à associer au pixel
        """
        self.element = new_element

######################### GETTER

    def get_info_pixel(self):
        """
        Renvoie les informations du pixel pour le débogage.
        """
        return {
            'Position': (self.x, self.y),
            'Couleur': self.color,
            'Zone ID': self.zone_id,
            'Altitude': self.altitude,
            'Element': self.element
        }