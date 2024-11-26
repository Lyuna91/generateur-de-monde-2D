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
        self.roads = self.generate_roads()  # Génère les routes
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

    def generate_roads(self):
        """
        Génère des routes connectant les villes avec les pixels existants.
        """
        all_pixels = [pixel for zone in self.zones for pixel in zone.pixels]  # Liste de tous les pixels
        roads = Road.create_roads_between_cities(self.cities, all_pixels)
        for road in roads:
            print(road)  # Print des informations des routes pour vérification
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
        self.display_routes()

    def display_routes(self):
        """
        Affiche les pixels des routes en jaune.
        """
        for road in self.roads:
            for pixel in road.route_pixels:
                 if(pixel.element == "city"):
                     pygame.draw.rect(self.screen, (255, 0, 0), (pixel.x, pixel.y, 10, 10))  # Jaune pour la route
                 else:
                     pygame.draw.rect(self.screen, (255, 255, 0), (pixel.x, pixel.y, 10, 10))  # Jaune pour la route
               


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
