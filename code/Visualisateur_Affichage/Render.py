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

# J'ai enlevé Map et options pour le moment, ils n'éxistent pas pour l'instant dans le code
class Render:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.zones = Zone.generate_voronoi_zones(self.width, self.height, 10)  # Exemple avec 10 zones

    
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

  
    def display_pixels(self):
        # Dessine chaque pixel de chaque zone
        for zone in self.zones:
            for pixel in zone.pixels:
                pygame.draw.rect(self.screen, pixel.color, (pixel.x, pixel.y, 10, 10))  # Taille du pixel 1x1

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