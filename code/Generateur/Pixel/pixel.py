#from Generateur.Zone import Zone
import random

class Pixel:
    """
    Classe permettant de définir les pixels.
    """

######################### INIT

# J'ai enlevé le paramètre "zone" des paramètres, je n'arrive pas a accéder à sa classe

    def __init__(self, x, y, color, altitude=0, element=None):
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
        # self.zone = zone  # je suis pas sûre de mettre la zone dans le pixel
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

    def get_info(self):
        """
        Renvoie les informations du pixel pour le débogage.
        """
        return {
            'Position': (self.x, self.y),
            'Couleur': self.color,
            # 'Zone': self.zone,
            'Altitude': self.altitude,
            'Element': self.element
        }

    # def get_biome(self):
    #     """
    #     Renvoie le biome auquel appartient ce pixel en fonction de sa zone.
    #     """
    #     if self.zone and hasattr(self.zone, 'biome'):
    #         return self.zone.biome
    #     return None
    
######################### GENERATEUR DE PIXELS

    @staticmethod
    def generate_pixels(largeur, hauteur, taille_pixel):
        """
        Génère automatiquement une grille de pixels pour remplir une fenêtre avec des couleurs aléatoires.
        
        :param largeur: Largeur de la fenêtre en pixels
        :param hauteur: Hauteur de la fenêtre en pixels
        :param taille_pixel: Taille de chaque pixel (par exemple 10x10)
        :return: Liste de pixels générés
        """
        list_pixels = []
        for x in range(0, largeur, taille_pixel):
            for y in range(0, hauteur, taille_pixel):
                # Générer une couleur aléatoire
                color = (0, 0, random.randint(200, 255))
                # Créer un pixel à la position (x, y) avec une couleur aléatoire
                pixel = Pixel(x=x, y=y, color=color)
                list_pixels.append(pixel)
        return list_pixels
