import pygame

pygame.init()

class Fenetre:
    def __init__(self,largeur, hauteur, titre):
        self.largeur = largeur
        self.hauteur = hauteur
        self.titre = titre
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption(self.titre)

    def afficher_quadrillage(self, taille_case, couleur):
        for x in range(0, self.largeur, taille_case):
            pygame.draw.line(self.ecran, couleur, (x, 0), (x, self.hauteur))
        for y in range(0, self.hauteur, taille_case):
            pygame.draw.line(self.ecran, couleur, (0, y), (self.largeur, y))

    def afficher(self):
        ouvert = True
        while ouvert:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ouvert = False
            self.ecran.fill((255,255,255))
            self.afficher_quadrillage(10, (200,200,200))
            pygame.display.flip()
        pygame.quit()
