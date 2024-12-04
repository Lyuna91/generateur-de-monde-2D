import sys
import os
import pygame
import random
from scipy.spatial import Voronoi

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Generateur.map import Map
from Generateur.biome import Biome
from Generateur.zone import Zone
from Generateur.pixel import Pixel
from Generateur.country import Country
from Generateur.city import City
from Generateur.road import Road
from Generateur.river import River


class Render:
    """
    Classe permettant de gérer l'affichage de la carte générée.
    """

    def __init__(self, width, height, title, num_countries):
        self.width = width
        self.height = height
        self.title = title
        self.num_countries = num_countries
        self.screen = pygame.Surface((self.width, self.height))
        self.generate_map()  # Générer la carte initiale

    def generate_map(self):
        """
        Génère la carte en recréant les pays, villes, routes et zones Voronoi.
        """
        self.zones = Zone.generate_voronoi_zones(self.width, self.height, 20)
        self.countries = self.generate_countries(self.num_countries)
        self.cities = self.generate_cities(self.num_countries)
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
        # for road in roads:
        #     print(road)
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
    
    def display_pixels(self):
        """
        Dessine les éléments de la carte (pays, villes, routes) sur la surface.
        """
        self.screen.fill((255, 255, 255))  # Remplir l'écran de blanc
        for zone in self.zones:
            if zone.biome.name == "Ocean" or zone.biome.name == "Lake":
                for pixel in zone.pixels:
                    pygame.draw.rect(self.screen, zone.biome.color, (pixel.x, pixel.y, 10, 10))

        for river in self.rivers:
            for pixel in river.route_pixels:
                pygame.draw.rect(self.screen, (0, 105, 148), (pixel.x, pixel.y, 10, 10))

        for country in self.countries:
            country_color = self.country_colors[country.id]
            for zone in country.zones:
                for pixel in zone.pixels:
                    pygame.draw.rect(self.screen, country_color, (pixel.x, pixel.y, 10, 10))

        for country in self.countries:
            for pixel in country.border_pixels:
                pygame.draw.rect(self.screen, (0, 0, 0), (pixel.x, pixel.y, 10, 10))

        for road in self.roads:
            for pixel in road.route_pixels:
                for zone in self.zones:
                    if (zone.id == pixel.zone_id):
                        if(zone.biome.name == "Ocean" or zone.biome.name == "Lake"):
                            pass
                        else:
                            pygame.draw.rect(self.screen, (255, 255, 0), (pixel.x, pixel.y, 10, 10))

        for city in self.cities:
            pygame.draw.rect(self.screen, (255, 0, 0), (city.position.x, city.position.y, 10, 10))