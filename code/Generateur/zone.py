import random
from scipy.spatial import Voronoi
from .pixel import Pixel
from .biome import Biome

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
        self.biome = Biome.create_random_biome()
        self.pixels = pixels if pixels is not None else []

        def __repr__(self):
            """
            Retourne une représentation de la zone sous forme de string.
            """
            return f"Zone(id={self.id}, size={self.size}, seed={self.seed}, pixels={self.pixels}, biome={self.biome})"

######################### METHODS

    def get_info_zone(self):
        """
        Renvoie les informations principales de la zone pour le débogage.

        :return: Dictionnaire des informations de la zone
        """
        print('ID :')
        print(self.id)
        print('\n')

        print('Position du centre (seed)')
        print(self.seed)
        print('\n')

        print('Nombre de pixels')
        print(self.size)
        print('\n')

        print('Biome')
        print(self.biome.get_biome_info()) # A creer
        print('\n')

        return 1

    @staticmethod
    def generate_voronoi_zones(width, height, num_zones, pixel_size=10):
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
                pixel = Pixel(x, y, closest_zone.biome.color, zone_id=closest_zone.id)  # Crée le pixel avec l'ID de la zone
                closest_zone.pixels.append(pixel)  # Ajoute le pixel à la liste de pixels de la zone
                closest_zone.size += 1  # Incrémente la taille de la zone
                pixel_count += 1  # Incrémente le compteur de pixels
                print(f"Pixel Info - X: {pixel.x}, Y: {pixel.y}, Color: {pixel.color}, Zone: {pixel.zone_id}")  # Ligne ajoutée

        # Affiche les informations de chaque zone pour le débogage
        for zone in zones:
            zone.get_info_zone()

        # Afficher le nombre total de pixels créés
        print(f"Total number of pixels created: {pixel_count}")

        return zones

   