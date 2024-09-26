import pygame

pygame.init()

class Fenetre:
    def __init__(self,largeur, hauteur, titre):
        self.largeur = largeur
        self.hauteur = hauteur
        self.titre = titre
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption(self.titre)
        self.ecran.fill((255,255,255))

    def afficher(self):
        ouvert = True
        while ouvert:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ouvert = False
            pygame.display.flip()
        pygame.quit()
