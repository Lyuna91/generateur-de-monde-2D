from .pixel import Pixel
from .river import River
from .road import Road
from .city import City
from .biome import Biome
from .country import Country
from .zone import Zone
from .lake import Lake

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
        self.lakes = []

    def __repr__(self):
        """
        Retourne une représentation de la carte sous forme de string.
        """
        return f"Map(name={self.name}, size={self.size}, options={self.options})"

    ######################### METHODS

    def generate_empty_map(self, size):
        pass

    def generate_map(self, num_countries, num_cities, num_rivers, num_zones, mode, lake_size_min, lake_size_max, num_lakes):
        """
        Génère la carte en fonction des paramètres et du mode de génération.

        :param num_countries: Nombre de pays
        :param num_cities: Nombre de villes
        :param num_rivers: Nombre de rivières
        :param num_zones: Nombre de zones Voronoi
        :param mode: Mode de génération (Pangea ou Archipel)
        :param lake_size_min: Taille minimale de chaque lac en nombre de pixels
        :param lake_size_max: Taille maximale de chaque lac en nombre de pixels
        :param num_lakes: Nombre de lacs à créer
        """
        self.zones = Zone.generate_voronoi_zones(self.size[0], self.size[1], num_zones)
        
        if mode == "Pangea":
            self.generate_biomes_for_pangea()
        elif mode == "Archipel":
            self.generate_biomes_for_archipel()
        elif mode == "Continent" :
            self.generate_biomes_for_continents()
        else:
            raise ValueError(f"[ERROR] Mode inconnu : {mode}")

        self.countries = self.generate_countries(num_countries)
        self.cities = self.generate_cities(num_cities)
        self.roads = self.generate_roads()
        self.rivers = self.generate_rivers(num_rivers)
        self.lakes = self.generate_lakes(lake_size_min, lake_size_max, num_lakes)

         # Assigner des couleurs aléatoires à chaque pays
        self.country_colors = {
            country.id: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for country in self.countries}

    def assign_biomes(self):
        """
        Assigne des biomes aléatoires aux zones après leur génération.
        """
        for zone in self.zones:
            zone.biome = Biome.create_random_biome()
            for pixel in zone.pixels:
                pixel.color = zone.biome.color

    def generate_biomes_for_continents(self):
        """
        Génère les biomes pour chaque zone de la carte.
        """
        for zone in self.zones:
            zone.biome = Biome.create_random_biome()

    def generate_biomes_for_archipel(self):
        """
        Génère des biomes sous forme d'archipel, avec des îles dispersées au milieu d'une carte océanique.
        """
        for zone in self.zones:
            if random.random() < 0.2:  # 20% des zones deviennent des îles
                zone.biome = Biome.create_random_biome_without_water()  # Biome terrestre (sans eau)
            else:
                zone.biome = Biome.create_ocean_biome()

            for pixel in zone.pixels:
                pixel.color = zone.biome.color

    def generate_biomes_for_pangea(self):
        """
        Génère des biomes désert pour chaque zone de la carte, sauf pour la zone centrale et quelques zones adjacentes qui seront des biomes océan.
        """
        self.assign_biomes_for_island()

    def generate_countries(self, num_countries):
        return Country.create_countries_from_zones(self.zones, num_countries)

    def generate_cities(self, num_cities):
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
    
    def generate_lakes(self, lake_size_min, lake_size_max, num_lakes):
        self.lakes = Lake.create_lakes(self.zones, lake_size_min, lake_size_max, num_lakes)
        return self.lakes

    def delete_all_lake(self):
        self.lakes = []
        return self.lakes
        
    def delete_all_road(self):
        self.roads = []
        return self.roads

    def delete_all_biome(self):
        for zone in self.zones:
            if zone.biome.name != "Ocean":
                zone.biome = None
                for pixel in zone.pixels:
                    pixel.color = (255, 255, 255)
        return self.zones

    def generate_biomes_after_deletion(self):

        """
        Creation des nouveaux biomes après la suppression des biomes existants.
        """
        for zone in self.zones: 
            if zone.biome is None: 
                zone.biome = Biome.create_random_biome_without_water()
                for pixel in zone.pixels:
                    pixel.color = zone.biome.color

        return self.zones

    def delete_all_city(self):
        self.cities = []
        return self.cities

    def delete_all_river(self):
        self.rivers = []
        return self.rivers

    def find_central_pixel(self):
        """
        Trouve le pixel le plus au centre de la carte.
        :return: Le pixel le plus au centre de la carte.
        """
        width, height = self.size
        center_x, center_y = width // 2, height // 2

        min_distance = float('inf')
        central_pixel = None

        for zone in self.zones:
            for pixel in zone.pixels:
                distance = math.sqrt((pixel.x - center_x) ** 2 + (pixel.y - center_y) ** 2)
                if distance < min_distance:
                    min_distance = distance
                    central_pixel = pixel

        return central_pixel
    
    def assign_biomes_for_island(self):
        """
        Assigne des biomes de manière à former une île centrale entourée d'océans.
        """
        central_pixel = self.find_central_pixel()
        central_zone = next(zone for zone in self.zones if central_pixel in zone.pixels)

        island_zones = [central_zone]
        checked_zones = set(island_zones)
        nb_pixels = central_zone.size
        max_pixels = sum(zone.size for zone in self.zones) // 2  # Limite de pixels pour l'île
        # Trouver les zones adjacentes et les ajouter à la liste
        while nb_pixels < max_pixels: 
            new_adjacent_zones = []
            for zone in island_zones:
                for other_zone in self.zones:
                    if other_zone not in checked_zones and zone.is_adjacent(other_zone):
                        new_adjacent_zones.append(other_zone)
                        nb_pixels += other_zone.size
                        if nb_pixels >= max_pixels:
                            break
                        checked_zones.add(other_zone)
            if not new_adjacent_zones:
                print("[DEBUG] Aucune zone pour pangée trouvée")
                break  # Si aucune nouvelle zone adjacente n'est trouvée, arrêter la boucle
            island_zones.extend(new_adjacent_zones)


        # Assigner des biomes désert aux autres zones
        for zone in self.zones:
            if zone not in island_zones:
                zone.biome = Biome.create_ocean_biome()
                for pixel in zone.pixels:
                    pixel.color = zone.biome.color

        # Assigner des biomes aléatoires (sans eau) aux zones de l'île
        for zone in island_zones:
            zone.biome = Biome.create_random_biome_without_water()
            for pixel in zone.pixels:
                pixel.color = zone.biome.color