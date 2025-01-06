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

PIXEL_SIZE = 5

class Render:
    """
    Classe permettant de gérer l'affichage de la carte générée.
    """

    def __init__(self, width, height, title, num_countries, num_cities, num_rivers, num_zones, mode, num_lakes):
        self.width = width
        self.height = height
        self.title = title
        self.num_countries = num_countries
        self.num_cities = num_cities
        self.num_rivers = num_rivers
        self.num_lakes = num_lakes
        self.num_zones = num_zones
        self.mode = mode  # Ajout du mode
        self.show_borders = False  # Par défaut, frontières masquées
        self.show_roads = False  # Par défaut, routes masquées
        self.show_cities = False  # Par défaut, villes masquées        
        self.screen = pygame.Surface((self.width, self.height))
        self.map = Map(name=title, size=(self.width, self.height), options={})
        self.display_mode = "pays"  # Mode d'affichage par défaut
        self.generate_map()  # Générer la carte initiale

        self.show_city_names = False  # Par défaut, noms des villes masqués
        self.show_country_names = False  # Par défaut, noms des pays masqués


        pygame.font.init()  # Initialiser les polices
        self.font = pygame.font.SysFont('Arial', 15, bold=True)  # Police plus grande et en gras


    def toggle_display_mode(self, mode):
        self.display_mode = mode
        self.display_pixels()

    def generate_map(self):
        """
        Génère la carte en utilisant la classe Map.
        """
        self.map.generate_map(self.num_countries, self.num_cities, self.num_rivers, self.num_zones, self.mode,10,50, self.num_lakes)

    def display_pixels(self):
        """
        Dessine les éléments de la carte (pays, villes, routes) sur la surface.
        """
        self.screen.fill((255, 255, 255))  # Remplir l'écran de blanc

        if self.display_mode == "biome":
            # Affichage des biomes
            for zone in self.map.zones:
                for pixel in zone.pixels:
                    color = zone.biome.color
                    if zone.biome.name == "Forest" and random.random() < 0.2:  # 10% des pixels seront plus foncés
                        color = (max(0, color[0] - 30), max(0, color[1] - 30), max(0, color[2] - 30))
                    pygame.draw.rect(self.screen, color, (pixel.x, pixel.y, PIXEL_SIZE, PIXEL_SIZE))
            
            for lake in self.map.lakes:
                for pixel in lake.lake_pixels:
                    pygame.draw.rect(self.screen, pixel.color, (pixel.x, pixel.y, PIXEL_SIZE, PIXEL_SIZE))


            for river in self.map.rivers:
                for pixel in river.river_pixels:
                    pygame.draw.rect(self.screen, (0, 105, 148), (pixel.x, pixel.y, PIXEL_SIZE, PIXEL_SIZE))
            
            # self.display_beaches()
            
            # Affichage conditionnel des frontières
            if self.show_borders:
                for country in self.map.countries:
                    for pixel in country.border_pixels:
                        pygame.draw.rect(self.screen, (0, 0, 0), (pixel.x, pixel.y, PIXEL_SIZE, PIXEL_SIZE))
        
            # Affichage conditionnel des routes
            if self.show_roads:
                for road in self.map.roads:
                    for pixel in road.road_pixels:
                        pygame.draw.rect(self.screen, (255, 255, 0), (pixel.x, pixel.y, PIXEL_SIZE, PIXEL_SIZE))
            
            # Affichage conditionnel des villes
            if self.show_cities:
                for city in self.map.cities:
                    pygame.draw.rect(self.screen, (100, 100, 100), (city.position.x - PIXEL_SIZE*2, city.position.y, PIXEL_SIZE * 5, PIXEL_SIZE * 2))
                    pygame.draw.rect(self.screen, (100, 100, 100), (city.position.x - PIXEL_SIZE*2, city.position.y - PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
                    pygame.draw.rect(self.screen, (100, 100, 100), (city.position.x, city.position.y - PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
                    pygame.draw.rect(self.screen, (100, 100, 100), (city.position.x + PIXEL_SIZE*2, city.position.y - PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
                    pygame.draw.rect(self.screen, (165, 70, 70), (city.position.x, city.position.y + PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

            if self.show_city_names:
                for city in self.map.cities:
                    city_name = city.name
                    text_surface = self.font.render(city_name, True, (0, 0, 255))
                    text_rect = text_surface.get_rect(center=(city.position.x, city.position.y - PIXEL_SIZE))
                    pygame.draw.rect(self.screen, (255, 255, 255), text_rect.inflate(PIXEL_SIZE, PIXEL_SIZE))
                    self.screen.blit(text_surface, text_rect)

            if self.show_country_names:
                for country in self.map.countries:
                    avg_x = sum(pixel.x for zone in country.zones for pixel in zone.pixels) // max(1, sum(len(zone.pixels) for zone in country.zones))
                    avg_y = sum(pixel.y for zone in country.zones for pixel in zone.pixels) // max(1, sum(len(zone.pixels) for zone in country.zones))
                    country_name = country.name
                    text_surface = self.font.render(country_name, True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=(avg_x, avg_y))
                    pygame.draw.rect(self.screen, (255, 255, 255), text_rect.inflate(PIXEL_SIZE, PIXEL_SIZE))
                    self.screen.blit(text_surface, text_rect)

        elif self.display_mode == "pays":
            for zone in self.map.zones:
                for pixel in zone.pixels:
                    pygame.draw.rect(self.screen, zone.biome.color, (pixel.x, pixel.y, PIXEL_SIZE, PIXEL_SIZE))

            for country in self.map.countries:
                country_color = self.map.country_colors[country.id]
                for zone in country.zones:
                    for pixel in zone.pixels:
                        pygame.draw.rect(self.screen, country_color, (pixel.x, pixel.y, PIXEL_SIZE, PIXEL_SIZE))
            
            for river in self.map.rivers:
                for pixel in river.river_pixels:
                    pygame.draw.rect(self.screen, (0, 105, 148), (pixel.x, pixel.y, PIXEL_SIZE, PIXEL_SIZE))

            # Affichage conditionnel des routes
            if self.show_roads:
                for road in self.map.roads:
                    for pixel in road.road_pixels:
                        pygame.draw.rect(self.screen, (255, 255, 0), (pixel.x, pixel.y, PIXEL_SIZE, PIXEL_SIZE))
                        
            for lake in self.map.lakes:
                for pixel in lake.lake_pixels:
                    pygame.draw.rect(self.screen, pixel.color, (pixel.x, pixel.y, PIXEL_SIZE, PIXEL_SIZE))


           # Affichage conditionnel des frontières
            if self.show_borders:
                for country in self.map.countries:
                    for pixel in country.border_pixels:
                        pygame.draw.rect(self.screen, (0, 0, 0), (pixel.x, pixel.y, PIXEL_SIZE, PIXEL_SIZE))
        
            
            # Affichage conditionnel des villes
            if self.show_cities:
                for city in self.map.cities:
                    pygame.draw.rect(self.screen, (100, 100, 100), (city.position.x - PIXEL_SIZE*2, city.position.y, PIXEL_SIZE * 5, PIXEL_SIZE * 2))
                    pygame.draw.rect(self.screen, (100, 100, 100), (city.position.x - PIXEL_SIZE*2, city.position.y - PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
                    pygame.draw.rect(self.screen, (100, 100, 100), (city.position.x, city.position.y - PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
                    pygame.draw.rect(self.screen, (100, 100, 100), (city.position.x + PIXEL_SIZE*2, city.position.y - PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
                    pygame.draw.rect(self.screen, (165, 70, 70), (city.position.x, city.position.y + PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
                    
            if self.show_city_names:
                for city in self.map.cities:
                    city_name = city.name
                    text_surface = self.font.render(city_name, True, (0, 0, 255))
                    text_rect = text_surface.get_rect(center=(city.position.x, city.position.y - PIXEL_SIZE))
                    pygame.draw.rect(self.screen, (255, 255, 255), text_rect.inflate(PIXEL_SIZE, PIXEL_SIZE))
                    self.screen.blit(text_surface, text_rect)

            if self.show_country_names:
                for country in self.map.countries:
                    avg_x = sum(pixel.x for zone in country.zones for pixel in zone.pixels) // max(1, sum(len(zone.pixels) for zone in country.zones))
                    avg_y = sum(pixel.y for zone in country.zones for pixel in zone.pixels) // max(1, sum(len(zone.pixels) for zone in country.zones))
                    country_name = country.name
                    text_surface = self.font.render(country_name, True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=(avg_x, avg_y))
                    pygame.draw.rect(self.screen, (255, 255, 255), text_rect.inflate(PIXEL_SIZE, PIXEL_SIZE))
                    self.screen.blit(text_surface, text_rect)

            




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
    def display_beaches(self):
        """
        Affiche les plages en colorant les pixels à la bordure des zones terrestres adjacentes à l'océan en jaune.
        """
        for zone in self.map.zones:
            if zone.biome.name != "Ocean":
                for pixel in zone.pixels:
                    x, y = pixel.x, pixel.y
                    adjacent_pixels = [(x-PIXEL_SIZE, y), (x+PIXEL_SIZE, y), (x, y-PIXEL_SIZE), (x, y+PIXEL_SIZE)]
                    for adj_x, adj_y in adjacent_pixels:
                        adj_pixel = next((p for z in self.map.zones if z.biome.name == "Ocean" for p in z.pixels if p.x == adj_x and p.y == adj_y), None)
                        if adj_pixel:
                            pygame.draw.rect(self.screen, (255, 255, 0), (pixel.x, pixel.y, PIXEL_SIZE, PIXEL_SIZE))
                            break

    def save_image(self, filename):
            """
            Sauvegarde l'image actuelle affichée dans un fichier.
            :param filename: Nom du fichier où sauvegarder l'image (avec extension, ex. 'map.png').
            """
            pygame.image.save(self.screen, filename)
            print(f"[DEBUG] Image sauvegardée sous : {filename}")