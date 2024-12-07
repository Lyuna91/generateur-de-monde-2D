from .pixel import Pixel
from .border import Border
from .river import River
from .road import Road
from .city import City
from .biome import Biome
from .country import Country
from .zone import Zone

import random
import math

class Map:
    """
    Classe permettant de définir les cartes.
    """

    ######################### INIT

    def __init__(self, name, size, options):
        """
        Initialise une carte avec ses caractéristiques de base.

        :param name: Nom de la carte
        :param size: Taille de la carte
        :param options: Options de génération de la carte
        """
        self.name = name
        self.size = size
        self.options = options
        self.zones = []
        self.countries = []
        self.cities = []
        self.roads = []
        self.rivers = []

    def __repr__(self):
        """
        Retourne une représentation de la carte sous forme de string.
        """
        return f"Map(name={self.name}, size={self.size}, options={self.options})"

    ######################### METHODS

    def generate_empty_map(self, size):
        pass


    def generate_map(self, num_countries):
        """
        Génère la carte en recréant les pays, villes, routes et zones Voronoi.
        """
        self.zones = Zone.generate_voronoi_zones(self.size[0], self.size[1], 20)
        self.countries = self.generate_countries(num_countries)
        self.cities = self.generate_cities(num_countries)
        self.roads = self.generate_roads()
        self.country_colors = {
            country.id: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for country in self.countries
        }
        self.rivers = self.generate_rivers(5)

    def generate_countries(self, num_countries):
        return Country.create_countries_from_zones(self.zones, num_countries)

    def generate_cities(self, num_countries):
        num_cities = num_countries + random.randint(1, num_countries)
        return City.create_cities_from_countries(self.countries, num_cities)

    def generate_roads(self):
        """
        Génère des routes connectant les villes avec les pixels existants.
        """
        all_pixels = [pixel for zone in self.zones for pixel in zone.pixels]  # Liste de tous les pixels
        roads = Road.create_roads_between_cities(self.cities, all_pixels, 3)
        return roads

    def generate_rivers(self, num_rivers):
        """
        Génère des rivières à partir des zones océaniques.

        :param num_rivers: Nombre de rivières à générer.
        """
        ocean_zones = [zone for zone in self.zones if zone.biome.name == "Ocean"]
        if not ocean_zones:
            print("[DEBUG] Aucune zone océanique trouvée.")
            return []

        ocean_pixels = [pixel for zone in ocean_zones for pixel in zone.pixels]
        all_pixels = [pixel for zone in self.zones for pixel in zone.pixels]

        print(f"[DEBUG] Nombre de pixels océaniques disponibles : {len(ocean_pixels)}")

        rivers = River.create_rivers_from_oceans(ocean_pixels, all_pixels, num_rivers)
        for river in rivers:
            print(f"[DEBUG] Rivière générée : {river}")

        return rivers

    def delete_all_road(self):
        self.roads = []
        return self.roads

    def delete_all_city(self):
        self.cities = []
        return self.cities

    def delete_all_river(self):
        self.rivers = []
        return self.rivers