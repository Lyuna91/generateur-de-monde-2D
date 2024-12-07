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
        self.map = Map(name="Pangea", size=(self.width, self.height), options={})
        self.generate_map()  # Générer la carte initiale

    def generate_map(self):
        """
        Génère la carte en utilisant la classe Map.
        """
        self.map.generate_map(self.num_countries)

    def display_pixels(self):
        """
        Dessine les éléments de la carte (pays, villes, routes) sur la surface.
        """
        self.screen.fill((255, 255, 255))  # Remplir l'écran de blanc
        for zone in self.map.zones:
            if zone.biome.name == "Ocean" or zone.biome.name == "Lake":
                for pixel in zone.pixels:
                    pygame.draw.rect(self.screen, zone.biome.color, (pixel.x, pixel.y, 10, 10))

        for river in self.map.rivers:
            for pixel in river.route_pixels:
                pygame.draw.rect(self.screen, (0, 105, 148), (pixel.x, pixel.y, 10, 10))

        for country in self.map.countries:
            country_color = self.map.country_colors[country.id]
            for zone in country.zones:
                for pixel in zone.pixels:
                    pygame.draw.rect(self.screen, country_color, (pixel.x, pixel.y, 10, 10))

        for country in self.map.countries:
            for pixel in country.border_pixels:
                pygame.draw.rect(self.screen, (0, 0, 0), (pixel.x, pixel.y, 10, 10))

        for road in self.map.roads:
            for pixel in road.route_pixels:
                for zone in self.map.zones:
                    if (zone.id == pixel.zone_id):
                        if(zone.biome.name == "Ocean" or zone.biome.name == "Lake"):
                            pass
                        else:
                            pygame.draw.rect(self.screen, (255, 255, 0), (pixel.x, pixel.y, 10, 10))

        for city in self.map.cities:
            pygame.draw.rect(self.screen, (255, 0, 0), (city.position.x, city.position.y, 10, 10))
