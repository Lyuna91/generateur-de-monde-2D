import sys
import os
import pygame
import random
from scipy.spatial import Voronoi #test

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Generateur.map import Map
from Generateur.biome import Biome
from Generateur.zone import Zone
from Generateur.pixel import Pixel
from Generateur.country import Country


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
        self.zones = Zone.generate_voronoi_zones(self.width, self.height, 20)  # Exemple avec 10 zones
        self.countries = self.generate_countries(num_countries)  # Appel pour créer les pays
        self.country_colors = {
            country.id: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for country in self.countries
        }

    def __repr__(self):
        """
        Retourne une représentation du rendu sous forme de string.
        """
        return f"Render(width={self.width}, height={self.height}, title={self.title}, screen={self.screen}, zones={self.zones})"

######################### METHODS

    def render_map(self, Map, options):
        pass

    def display_grid(self, pixel_size, couleur):
        """
        Affiche un quadrillage sur la fenêtre.
        """
        for x in range(0, self.width, pixel_size):
            pygame.draw.line(self.screen, couleur, (x, 0), (x, self.height))
        for y in range(0, self.height, pixel_size):
            pygame.draw.line(self.screen, couleur, (0, y), (self.width, y))


    def generate_countries(self, num_countries):
        """
        Appelle la méthode de création des pays avec les zones disponibles.
        """
        return Country.create_countries_from_zones(self.zones, num_countries)


    def display_pixels(self):
        # Dessine chaque pixel de chaque zone
        """for zone in self.zones:
            for pixel in zone.pixels:
                pygame.draw.rect(self.screen, pixel.color, (pixel.x, pixel.y, 10, 10))  # Taille du pixel 1x1
"""

         # Utilise les couleurs de chaque pays pour afficher les zones
        for country in self.countries:
            country_color = self.country_colors[country.id]  # Récupère la couleur du pays
            for zone in country.zones:
                for pixel in zone.pixels:
                    pygame.draw.rect(self.screen, country_color, (pixel.x, pixel.y, 10, 10))

        # Affiche les graines des zones comme des cercles pour référence
        for zone in self.zones:
            pygame.draw.circle(self.screen, (0, 0, 0), zone.seed, 3)
        



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

    def add_pixel(self, pixel):
        self.pixels.append(pixel)