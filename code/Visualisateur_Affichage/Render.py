import sys
import os
import pygame

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Generateur.map import Map

# J'ai enlevé Map et options pour le moment, ils n'éxistent pas pour l'instant dans le code
class Render:
    def __init__(self, width, height, title):
        # self.map = Map
        # self.options = options
        self.width = width
        self.height = height
        self.title = title
        self.ecran = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.pixels = Map.generate_pixels(width, height, 10) # Récupérer une liste de pixels générés dans Pixel

    
    def render_map(self, Map, options):
        pass

    def display_grid(self, pixel_size, couleur):
        """
        Affiche un quadrillage sur la fenêtre.
        """
        for x in range(0, self.width, pixel_size):
            pygame.draw.line(self.ecran, couleur, (x, 0), (x, self.height))
        for y in range(0, self.height, pixel_size):
            pygame.draw.line(self.ecran, couleur, (0, y), (self.width, y))

    def display_pixels(self,pixel_size=10):
        """
        Dessine les pixels sur l'écran à partir de la liste de pixels.
        """
        for pixel in self.pixels:
            pygame.draw.rect(self.ecran, pixel.color, (pixel.x, pixel.y, pixel_size, pixel_size))

    def display_window(self):
        """
        Permet d'afficher la fenêtre et de la maintenir ouverte.
        """
        ouvert = True
        while ouvert:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ouvert = False

            self.ecran.fill((255, 255, 255))  # Remplir l'écran de blanc
            # self.display_grid(10, (200, 200, 200))  # Afficher le quadrillage
            self.display_pixels()  # Afficher les pixels
            pygame.display.flip()  # Mettre à jour l'affichage
        pygame.quit()