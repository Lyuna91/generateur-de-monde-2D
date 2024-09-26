"""
Il s'agit de la liste des fonctions a réaliser ( pas encore complete)

Grammaire à respecter:

    - Pour les Classes : le nom de la classe acommence avec une Majuscule et si le nom est composé de plusieurs noms on mettra une majuscule au debut de chaque nouveaux noms. Ex: class GenerateurDeCarte, GenerateurCarte ect...

    - Pour les fonctions : pareil que pour les classes

    - Pour les variable : Toutes les lettres en minuscules et l'usage de "_" pour separer les mots Ex: couleur_pixel, position_pixel ect...

"""



class Route:
    """Une classe pour les routes"""
    def __init__(self, id, liste_des_pixels = []):
        self.id = id
        self.liste_des_pixels = liste_des_pixels

    def ajouterPixel (self, pixel):
        """ ajoute un pixel à une route
        :param self:
        :param pixel (tuple ou liste) les informations liés aux pixels
        """
        self.liste_des_pixels.append

    def tracerRoute(self,pixel_d, pixel_f):
        """ Trace une route optimal entre deux pixel, 
        on voudras determiner le meilleur chemin (le plus court)
        
        :param pixel_d: le pixel de départ
        :param pixel_f: le pixel d'arrivé
        """



class GenerateurCarte:

    def genererCarteVide(longueur, largeur):
        """ Cree une carte blanche
        :param longueur: la longueur de la fenetre d'affichage
        :param largeur: la largeur de la fenetre
        """

    def genererCarteTaille(taille):
        """
        Cree une carte blanche en fonction de la taille rentrée en parametre
        :param taille: (str) M pour moyenne, P pour petite, G pour grande
        """

    def genererArchipel():
        """
        Cree une archipel
        """
    
    def genererContinent():
        """
        Cree un continent
        """

    def genererPange():
        """
        Cree une pangée
        """

    def genererMonde(type_monde):
        """
        Cree un monde en fonction du type choisis
        par l'utilisateur

        :param type_monde: type du monde : archipel, pangée ect... 
        """

    def genererBiome(biome):
        """
        Cree un biome sur une carte
        :param biome: (dict) les informations du biome
        """

    def genererRoute(route):
        """
        Cree une route sur la carte
        :param route: (dict) les informations de la route
        """


class Biome: 
    """
    Les Biomes de la Carte
    """
    pass


class Riviere: 

    """
    Les rivieres de la map
    
    """

    pass


class VisualisateurCarte:

    """
    Visualisation de la Map
    
    """

class ModificateurCarte:

    """
    Modification de la map , de l'affichage, sauvegarde et chargement de la map  aussi appelle ControleurCarte
    
    """

class Render: 
    """
    Render ...

    """

