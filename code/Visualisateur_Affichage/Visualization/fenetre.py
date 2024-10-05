import pygame
from Generateur.Pixel import Pixel

pygame.init()

class Fenetre:
    def __init__(self,largeur, hauteur, titre, pixels):
        self.largeur = largeur
        self.hauteur = hauteur
        self.titre = titre
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption(self.titre)
        self.pixels = self.generer_pixels(self.largeur,self.hauteur,5)  # Générer automatiquement les pixels
        # list_pixels
        # Ajoutée par Jade : Liste des pixels à afficher ??? J'ai du mal avec Pygame pour l'instant, c'est une proposition


    def afficher_quadrillage(self, taille_case, couleur):
        """
        Affiche un quadrillage sur la fenêtre.
        """
        for x in range(0, self.largeur, taille_case):
            pygame.draw.line(self.ecran, couleur, (x, 0), (x, self.hauteur))
        for y in range(0, self.hauteur, taille_case):
            pygame.draw.line(self.ecran, couleur, (0, y), (self.largeur, y))

    def afficher_pixels(self):
        for pixel in self.pixels:
            pixel.dessiner(self.ecran)

    def afficher_fenetre(self):
        """
        Boucle principale pour afficher la fenêtre et les pixels.
        """
        ouvert = True
        while ouvert:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ouvert = False

            # Remplir l'écran de blanc
            self.ecran.fill((255, 255, 255))

            # Afficher le quadrillage
            self.afficher_quadrillage(10, (200, 200, 200))

            # Afficher les pixels
            self.afficher_pixels()

            # Mettre à jour l'affichage
            pygame.display.flip()
        pygame.quit()
