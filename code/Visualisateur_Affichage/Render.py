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

    def __init__(self, width, height, title, num_countries, num_cities, num_rivers, num_zones, mode):
        self.width = width
        self.height = height
        self.title = title
        self.num_countries = num_countries
        self.num_cities = num_cities
        self.num_rivers = num_rivers
        self.num_zones = num_zones
        self.mode = mode  # Ajout du mode
        self.show_borders = False  # Par défaut, frontières masquées
        self.show_roads = False  # Par défaut, routes masquées
        self.show_cities = False  # Par défaut, villes masquées        
        self.screen = pygame.Surface((self.width, self.height))
        self.map = Map(name=title, size=(self.width, self.height), options={})
        self.display_mode = "pays"  # Mode d'affichage par défaut
        self.generate_map()  # Générer la carte initiale

    def toggle_display_mode(self, mode):
        self.display_mode = mode
        self.display_pixels()

    def generate_map(self):
        """
        Génère la carte en utilisant la classe Map.
        """
        self.map.generate_map(self.num_countries, self.num_cities, self.num_rivers, self.num_zones, self.mode)

    def display_pixels(self):
        """
        Dessine les éléments de la carte (pays, villes, routes) sur la surface.
        """
        self.screen.fill((255, 255, 255))  # Remplir l'écran de blanc

        if self.display_mode == "biome":
            # Affichage des biomes
            for zone in self.map.zones:
                for pixel in zone.pixels:
                    pygame.draw.rect(self.screen, zone.biome.color, (pixel.x, pixel.y, 10, 10))
            
            for river in self.map.rivers:
                for pixel in river.route_pixels:
                    pygame.draw.rect(self.screen, (0, 105, 148), (pixel.x, pixel.y, 10, 10))
            
            # Affichage conditionnel des frontières
            if self.show_borders:
                for country in self.map.countries:
                    for pixel in country.border_pixels:
                        pygame.draw.rect(self.screen, (0, 0, 0), (pixel.x, pixel.y, 10, 10))
        
            # Affichage conditionnel des routes
            if self.show_roads:
                for road in self.map.roads:
                    for pixel in road.route_pixels:
                        pygame.draw.rect(self.screen, (255, 255, 0), (pixel.x, pixel.y, 10, 10))
            
            # Affichage conditionnel des villes
            if self.show_cities:
                for city in self.map.cities:
                    pygame.draw.rect(self.screen, (255, 0, 0), (city.position.x, city.position.y, 10, 10))

        elif self.display_mode == "pays":
            for zone in self.map.zones:
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

           # Affichage conditionnel des frontières
            if self.show_borders:
                for country in self.map.countries:
                    for pixel in country.border_pixels:
                        pygame.draw.rect(self.screen, (0, 0, 0), (pixel.x, pixel.y, 10, 10))
        
            # Affichage conditionnel des routes
            if self.show_roads:
                for road in self.map.roads:
                    for pixel in road.route_pixels:
                        pygame.draw.rect(self.screen, (255, 255, 0), (pixel.x, pixel.y, 10, 10))
            
            # Affichage conditionnel des villes
            if self.show_cities:
                for city in self.map.cities:
                    pygame.draw.rect(self.screen, (255, 0, 0), (city.position.x, city.position.y, 10, 10))


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

            """

    def save_image(self, filename):
            """
            Sauvegarde l'image actuelle affichée dans un fichier.
            :param filename: Nom du fichier où sauvegarder l'image (avec extension, ex. 'map.png').
            """
            pygame.image.save(self.screen, filename)
            print(f"[DEBUG] Image sauvegardée sous : {filename}")