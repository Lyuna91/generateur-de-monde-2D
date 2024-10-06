import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Accéder à la classe Pixel
from Generateur.pixel import Pixel  # Importer la classe Pixel depuis le module pixel

pygame.init()

class Window:

    """
    Classe permettant de définir une fenêtre d'affichage pour visualiser les pixels.
    """

######################### INIT

    def __init__(self, largeur, hauteur, titre):
        self.largeur = largeur
        self.hauteur = hauteur
        self.titre = titre
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption(self.titre)
        self.pixels = Pixel.generate_pixels(largeur, hauteur, 10) # Récupérer une liste de pixels générés dans Pixel

######################### METHODES

    def display_grid(self, taille_case, couleur):
        """
        Affiche un quadrillage sur la fenêtre.
        """
        for x in range(0, self.largeur, taille_case):
            pygame.draw.line(self.ecran, couleur, (x, 0), (x, self.hauteur))
        for y in range(0, self.hauteur, taille_case):
            pygame.draw.line(self.ecran, couleur, (0, y), (self.largeur, y))

    def display_pixels(self,taille_pixel=10):
        """
        Dessine les pixels sur l'écran à partir de la liste de pixels.
        """
        for pixel in self.pixels:
            pygame.draw.rect(self.ecran, pixel.color, (pixel.x, pixel.y, taille_pixel, taille_pixel))

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
