import random
from scipy.spatial import Voronoi
from .pixel import Pixel
from .biome import Biome
from math import sqrt

PIXEL_SIZE = 5

class Zone:
    """
    Classe permettant de définir les zones de Voronoi.
    """

######################### INIT

    def __init__(self, id, size, seed, pixels):
        """
        Initialise une zone avec un ID, une taille, un centre (seed), une liste de pixels et une couleur unique.
        
        :param id: Identifiant unique de la zone
        :param size: Taille de la zone (nombre de pixels)
        :param seed: Coordonnées du centre de la zone
        :param pixels: Liste de pixels appartenant à cette zone
        :param color: Couleur unique de la zone
        """
        self.id = id
        self.seed = seed
        self.size = size
        self.biome = None
        self.pixels = pixels if pixels is not None else []

    def __repr__(self):
        """
        Retourne une représentation de la zone sous forme de string.
        """
        return f"Zone(id={self.id}, size={self.size}, seed={self.seed}, biome={self.biome})"

######################### METHODS

    def get_info_zone(self):
        """
        Renvoie les informations principales de la zone pour le débogage.

        :return: Dictionnaire des informations de la zone
        """
        return {
            'ID': self.id,
            'Size': self.size,
            'Seed': self.seed,
            'Biome': self.biome
        }

    @staticmethod
    def generate_voronoi_zones(width, height, num_zones, pixel_size=PIXEL_SIZE):
        """
        Génère des pixels individuels, assignés aux zones de Voronoi les plus proches.

        :param width: Largeur de la carte
        :param height: Hauteur de la carte
        :param num_zones: Nombre de zones de Voronoi
        :param pixel_size: Taille du pixel (1 pour chaque pixel individuel)
        :return: Liste d'objets Zone contenant des pixels
        """
        # Générer des centres aléatoires pour les zones
        centers = [(random.randint(0, width), random.randint(0, height)) for _ in range(num_zones)]
        
        # Créer les zones avec des couleurs uniques
        zones = [Zone(id=idx, seed=centers[idx],
                    size=0, pixels=[]) for idx in range(num_zones)]

        # Initialiser le compteur de pixels
        pixel_count = 0

        # Assigner chaque pixel individuel à la zone la plus proche
        for x in range(0, width, pixel_size):
            for y in range(0, height, pixel_size):
                # Trouver la zone la plus proche pour chaque pixel
                closest_zone = min(zones, key=lambda zone: (zone.seed[0] - x) ** 2 + (zone.seed[1] - y) ** 2)
                pixel = Pixel(x, y, (255,255,255), zone_id=closest_zone.id)  # Crée le pixel avec l'ID de la zone
                closest_zone.pixels.append(pixel)  # Ajoute le pixel à la liste de pixels de la zone
                closest_zone.size += 1  # Incrémente la taille de la zone
                pixel_count += 1  # Incrémente le compteur de pixels
                # print(pixel)  # Affiche tout les pixels

        # Affiche les informations de chaque zone pour le débogage
        for zone in zones:
            print(zone)
            print("\n")

        # Afficher le nombre total de pixels créés
        print(f"Total number of pixels created: {pixel_count}")

        return zones

    def is_adjacent(self, other_zone, distance_threshold=200):
        """
        Vérifie si une autre zone est adjacente à cette zone.
        
        :param other_zone: L'autre zone à vérifier
        :param distance_threshold: La distance maximale pour être considéré comme adjacent
        :return: True si les zones sont adjacentes, False sinon
        """
        distance = sqrt((self.seed[0] - other_zone.seed[0]) ** 2 + (self.seed[1] - other_zone.seed[1]) ** 2)
        return distance <= distance_threshold