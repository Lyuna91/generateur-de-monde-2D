######################### GENERATEUR

from .pixel import Pixel
from .border import Border
from .river import River
from .road import Road
from .city import City
from .biome import Biome
from .country import Country

######################### IMPORT 

import random


class Map: 
    def __init__(self, name, size, options):
        self.name = name
        self.size = size
        self.options = options

    def generate_empty_map(self, size):
        pass

    def generate_map(self, size, options):
        pass

    def generate_pixels(width, height, pixel_size):
        """
        Génère automatiquement une grille de pixels pour remplir une fenêtre avec des couleurs aléatoires.
        
        :param width: Largeur de la fenêtre en pixels
        :param height: hauteur de la fenêtre en pixels
        :param pixel_size: Taille de chaque pixel (par exemple 10x10)
        :return: Liste de pixels générés
        """

        list_pixels = []
        for x in range(0, width, pixel_size):
            for y in range(0, height, pixel_size):
                # Générer une couleur aléatoire
                color = (0, 0, random.randint(200, 255))
                # Créer un pixel à la position (x, y) avec une couleur aléatoire
                pixel = Pixel(x=x, y=y, color=color)
                list_pixels.append(pixel)
        return list_pixels

    def generate_continent(self, size, options):
        pass

    def generate_pangea(self, size, options):
        pass

    def generate_archipelago(self, size, options):
        pass

    def generate_biome(self, size, biome, options):
        pass

    def generate_country(self, size, options):
        pass

    def generate_border(self, size, options):
        pass

    def generate_road(self, size, options):
        pass

    def generate_river(self, size, options):
        pass

    def generate_cities(self, size, options):
        pass


     