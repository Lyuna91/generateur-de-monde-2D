from .zone import Zone
from .biome import Biome
from .pixel import Pixel
import random

PIXEL_SIZE = 5

class Lake:
    """
    Classe permettant de définir les lacs.
    """

    ######################### INIT

    def __init__(self, id, lake_pixels):
        """
        Initialise un lac avec ses caractéristiques de base.

        :param id: Identifiant unique du lac
        :param lake_pixels: Liste des pixels constituant le lac
        """
        self.id = id
        self.lake_pixels = lake_pixels

    def __repr__(self):
        """
        Retourne une représentation du lac sous forme de string.
        """
        return f"Lake(id={self.id}, lake_pixels={self.lake_pixels})"

    ######################### METHODS

    @staticmethod
    def get_adjacent_pixels(pixel, all_zones):
        """
        Retourne les pixels adjacents à un pixel donné.
    
        :param pixel: Le pixel pour lequel trouver les pixels adjacents.
        :param all_zones: Liste de toutes les zones de la carte.
        :return: Liste des pixels adjacents.
        """
        adjacent_pixels = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Gauche, Droite, Haut, Bas
        for dx, dy in directions:
            adj_x, adj_y = pixel.x + dx * PIXEL_SIZE, pixel.y + dy * PIXEL_SIZE
            adj_pixel = next((p for zone in all_zones for p in zone.pixels if p.x == adj_x and p.y == adj_y), None)
            if adj_pixel:
                adjacent_pixels.append(adj_pixel)
        return adjacent_pixels
    
    @staticmethod
    def is_far_from_ocean(pixel, all_zones, min_distance=5):
        """
        Vérifie si un pixel est suffisamment éloigné des pixels océan.
    
        :param pixel: Le pixel à vérifier.
        :param all_zones: Liste de toutes les zones de la carte.
        :param min_distance: Distance minimale par rapport aux pixels océan.
        :return: True si le pixel est suffisamment éloigné des pixels océan, False sinon.
        """
        for zone in all_zones:
            if zone.biome.name == "Ocean":
                for ocean_pixel in zone.pixels:
                    if abs(pixel.x - ocean_pixel.x) <= min_distance * PIXEL_SIZE and abs(pixel.y - ocean_pixel.y) <= min_distance * PIXEL_SIZE:
                        return False
        return True

    @staticmethod
    def create_lakes(all_zones, lake_size_min, lake_size_max, num_lakes):
        """
        Crée des lacs sur la carte.

        :param all_zones: Liste de toutes les zones de la carte
        :param lake_size_min: Taille minimale de chaque lac en nombre de pixels
        :param lake_size_max: Taille maximale de chaque lac en nombre de pixels
        :param num_lakes: Nombre de lacs à créer
        :return: Liste de listes de pixels représentant les lacs.
        """
        ocean_biome = Biome.create_ocean_biome()
        lake_list = []

        for i in range(num_lakes):
            lake_pixels = []
            lake_size = random.randint(lake_size_min, lake_size_max)
            while not lake_pixels:
                random_zone = random.choice([zone for zone in all_zones if zone.biome.name != "Ocean"])
                random_pixel = random.choice(random_zone.pixels)
                if random_zone.biome.name != "Ocean" and Lake.is_far_from_ocean(random_pixel, all_zones):
                    lake_pixels.append(random_pixel)

            # Ajouter des pixels adjacents pour former le lac
            checked_pixels = set(lake_pixels)
            while len(lake_pixels) < lake_size:
                new_adjacent_pixels = []
                for pixel in lake_pixels:
                    for adj_pixel in Lake.get_adjacent_pixels(pixel, all_zones):
                        if adj_pixel not in checked_pixels and random.random() < 0.8:  # Probabilité d'ajouter un pixel adjacent
                            new_adjacent_pixels.append(adj_pixel)
                            checked_pixels.add(adj_pixel)
                            if len(lake_pixels) + len(new_adjacent_pixels) >= lake_size:
                                break
                    if len(lake_pixels) + len(new_adjacent_pixels) >= lake_size:
                        break
                if not new_adjacent_pixels:
                    break  # Si aucune nouvelle zone adjacente n'est trouvée, arrêter la boucle
                lake_pixels.extend(new_adjacent_pixels)

            # Vérifier si un pixel du lac contient une ville
            if any(pixel.element == "City" for pixel in lake_pixels):
                continue  # Annuler la génération de ce lac et passer au suivant

            # Définir l'élément des pixels comme étant un lac
            for pixel in lake_pixels:
                pixel.set_element("Lake")
                pixel.color = ocean_biome.color

            lake = Lake(id=i, lake_pixels=lake_pixels)
            lake_list.append(lake)

        return lake_list