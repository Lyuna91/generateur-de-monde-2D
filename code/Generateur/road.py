from .pixel import Pixel
import random


class Road:
    """
    Classe permettant de définir les routes.
    """

######################### INIT

    def __init__(self, id, start_point, end_point):
        """
        Initialise une route avec ses caractéristiques de base.

        :param id: Identifiant unique de la route
        :param start_point: Coordonnées (x, y) du point de départ
        :param end_point: Coordonnées (x, y) du point d'arrivée
        """
        self.id = id
        self.start_point = start_point
        self.end_point = end_point
        self.pixels = self.generate_road_pixels()

    def __repr__(self):
        """
        Retourne une représentation de la route sous forme de string.
        """
        return f"Road(id={self.id}, start_point={self.start_point}, end_point={self.end_point}, num_pixels={len(self.pixels)})"

######################### METHODS

    def generate_road_pixels(self):
        """
        Génère les pixels qui constituent la route entre le point de départ et d'arrivée avec des variations pour un effet naturel.
        :return: Liste des pixels de la route
        """
        pixels = []
        x1, y1 = self.start_point
        x2, y2 = self.end_point

        # Générer quelques points intermédiaires pour créer un chemin naturel
        num_segments = 5  # Divise la route en segments
        intermediate_points = [(x1, y1)]

        for i in range(1, num_segments):
            # Calculer un point intermédiaire en progressant vers l'objectif
            ratio = i / num_segments
            target_x = int(x1 + (x2 - x1) * ratio)
            target_y = int(y1 + (y2 - y1) * ratio)

            # Ajouter une courbure perpendiculaire à la direction principale
            perpendicular_dx = -(y2 - y1)  # Perpendiculaire à dx
            perpendicular_dy = (x2 - x1)  # Perpendiculaire à dy
            length = max(abs(perpendicular_dx), abs(perpendicular_dy))
            if length > 0:
                perpendicular_dx //= length
                perpendicular_dy //= length

            # Appliquer une déviation avec une intensité contrôlée
            deviation_strength = random.randint(-20, 20)
            target_x += perpendicular_dx * deviation_strength
            target_y += perpendicular_dy * deviation_strength

            # Ajouter le point intermédiaire
            intermediate_points.append((target_x, target_y))

        intermediate_points.append((x2, y2))  # Ajouter le point final

        # Connecter les points intermédiaires avec des lignes
        for i in range(len(intermediate_points) - 1):
            start = intermediate_points[i]
            end = intermediate_points[i + 1]

            # Utiliser Bresenham pour connecter les segments
            pixels.extend(self._bresenham_line(start, end))

        return pixels


    def _bresenham_line(self, start, end):
        """
        Génère les pixels entre deux points en utilisant l'algorithme de Bresenham.
        :param start: Point de départ (x, y)
        :param end: Point d'arrivée (x, y)
        :return: Liste des pixels
        """
        x1, y1 = start
        x2, y2 = end
        pixels = []

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            pixels.append(Pixel(x1, y1, (255, 255, 0), zone_id=None, element="Road"))  # Couleur jaune

            if (x1, y1) == (x2, y2):
                break

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

        return pixels

def create_road(self):
    """
    Retourne la route elle-même pour chaînage éventuel.
    """
    return self

"""
def generate_roads(self):
        
        Crée des routes connectant des villes aléatoires.
        
        roads = []
        if len(self.cities) < 2:
            return roads  # Pas assez de villes pour créer des routes
        
        # Connecter chaque ville à une autre aléatoire
        for i, city in enumerate(self.cities):
            if i + 1 < len(self.cities):
                next_city = self.cities[(i + 1) % len(self.cities)]
                road = Road(id=len(roads), start_point=(city.position.x, city.position.y),
                            end_point=(next_city.position.x, next_city.position.y))
                roads.append(road)
        return roads
        """