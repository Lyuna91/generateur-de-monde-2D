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


class Render:
    """
    Classe permettant de gérer l'affichage de la carte générée.
    """

    def __init__(self, width, height, title, num_countries):
        """
        Initialise un rendu avec une largeur, une hauteur et un titre de fenêtre.

        :param width: Largeur de la fenêtre
        :param height: Hauteur de la fenêtre
        :param title: Titre de la fenêtre
        """
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.zones = Zone.generate_voronoi_zones(self.width, self.height, 20)  # Exemple avec 20 zones
        self.countries = self.generate_countries(num_countries)  # Appel pour créer les pays
        self.cities = self.generate_cities(num_countries)  # Appel pour créer les villes
        self.roads = self.generate_roads(10)  # Appel pour créer les routes
        self.country_colors = {
            country.id: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for country in self.countries
        }

    def __repr__(self):
        """
        Retourne une représentation du rendu sous forme de string.
        """
        return f"Render(width={self.width}, height={self.height}, title={self.title}, roads={len(self.roads)})"

######################### METHODS

    def generate_countries(self, num_countries):
        """
        Appelle la méthode de création des pays avec les zones disponibles.
        """
        return Country.create_countries_from_zones(self.zones, num_countries)

    def generate_cities(self, num_countries):
        """
        Appelle la méthode de création des villes avec les pays disponibles.
        """
        num_cities = num_countries + random.randint(1, num_countries)
        return City.create_cities_from_countries(self.countries, num_cities)

    def generate_roads(self, max_roads):
        """
        Crée des routes connectant des villes aléatoires et des points aléatoires sur la carte.
        Chaque ville aura entre 1 et 2 routes, avec un nombre total de routes limité par max_roads.
        """
        roads = []
        if len(self.cities) < 2:
            return roads  # Pas assez de villes pour créer des routes

        total_roads = 0

        while total_roads < max_roads:
            city = random.choice(self.cities) # Choisir une ville aléatoire
            num_roads = random.randint(1, 2)
            for _ in range(num_roads):
                if total_roads >= max_roads:
                    break
                if random.choice([True, False]):
                    # Connecter à une autre ville aléatoire
                    next_city = random.choice(self.cities)
                    while next_city == city:
                        next_city = random.choice(self.cities)
                    road = Road(id=len(roads), start_point=(city.position.x, city.position.y),
                                end_point=(next_city.position.x, next_city.position.y))
                else:
                    # Connecter à un point aléatoire sur la carte
                    random_zone = random.choice(self.zones)
                    random_pixel = random.choice(random_zone.pixels)
                    random_point = (random_pixel.x, random_pixel.y)
                    road = Road(id=len(roads), start_point=(city.position.x, city.position.y),
                                end_point=random_point)
                roads.append(road)
                total_roads += 1

        return roads

    def display_pixels(self):
        """
        Affiche les pixels des zones, pays, villes et routes.
        """
        # Affiche les pays et zones
        for country in self.countries:
            country_color = self.country_colors[country.id]
            for zone in country.zones:
                for pixel in zone.pixels:
                    pygame.draw.rect(self.screen, country_color, (pixel.x, pixel.y, 10, 10))

        # Affiche les bordures des pays
        for country in self.countries:
            for pixel in country.border_pixels:
                pygame.draw.rect(self.screen, (0, 0, 0), (pixel.x, pixel.y, 10, 10))

        # Affiche les villes
        for city in self.cities:
            pygame.draw.rect(self.screen, (255, 0, 0), (city.position.x, city.position.y, 10, 10))  # Rouge

        # Affiche les routes
        for road in self.roads:
            for pixel in road.pixels:
                pygame.draw.rect(self.screen, pixel.color, (pixel.x, pixel.y, 2, 2))  # Routes jaunes

    def display_grid(self, pixel_size, couleur):
        """
        Affiche un quadrillage sur la fenêtre.
        """
        for x in range(0, self.width, pixel_size):
            pygame.draw.line(self.screen, couleur, (x, 0), (x, self.height))
        for y in range(0, self.height, pixel_size):
            pygame.draw.line(self.screen, couleur, (0, y), (self.width, y))

    def display_window(self):
        """
        Permet d'afficher la fenêtre et de la maintenir ouverte.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))  # Remplir l'écran de blanc
            self.display_pixels()  # Afficher les pixels
            self.display_grid(10, (200, 200, 200))  # Afficher le quadrillage
            pygame.display.flip()  # Mettre à jour l'affichage

        pygame.quit()
