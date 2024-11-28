import random
import math

class Road:
    """
    Classe permettant de définir les routes à partir des pixels existants sur la carte.
    """

    ######################### INIT

    def __init__(self, id, start_city, end_city, pixels):
        """
        Initialise une route avec ses caractéristiques de base.

        :param id: Identifiant unique de la route
        :param start_city: Ville de départ
        :param end_city: Ville d'arrivée
        :param pixels: Liste des pixels disponibles sur le plateau
        """
        self.id = id
        self.start_city = start_city
        self.end_city = end_city
        self.route_pixels = self.create_route_pixels(pixels)

    def __repr__(self):
        """
        Retourne une représentation de la route sous forme de chaîne de caractères.
        """
        return f"Road(id={self.id}, start_city={self.start_city.name}, end_city={self.end_city.name}, pixels={len(self.route_pixels)})"

    ######################### METHODS

    def create_route_pixels(self, all_pixels):
        """
        Crée une ligne de pixels entre les points de départ et d'arrivée en utilisant des points intermédiaires aléatoires.

        :param all_pixels: Liste des pixels disponibles sur le plateau.
        :return: Liste des pixels formant la route.
        """
        def calculer_distance(depart, fin):
            x1, y1 = depart
            x2, y2 = fin
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            return distance

        def calculer_intersections(distance):
            intersections = max(1, round(distance / 110))  # Diviser par une valeur plus grande pour moins de points
            return intersections

        def creer_intersections(depart, fin, divergence=1.5):
            x1, y1 = depart
            x2, y2 = fin
            intersections = calculer_intersections(calculer_distance(depart, fin))
            dx = (x2 - x1) / intersections
            dy = (y2 - y1) / intersections
            x, y = x1, y1
            liste_intersections = [depart]  # Ajouter le point de départ
            for i in range(intersections - 1):  # On s'arrête avant le dernier point
                x += dx
                y += dy
                divergence_x = random.uniform(-divergence, divergence) * dx
                divergence_y = random.uniform(-divergence, divergence) * dy
                liste_intersections.append((round((x + divergence_x) / 10) * 10, round((y + divergence_y) / 10) * 10))
            liste_intersections.append(fin)  # Ajouter le point d'arrivée
            return liste_intersections

        route_pixels = []
        x1, y1 = self.start_city.position.x, self.start_city.position.y
        x2, y2 = self.end_city.position.x, self.end_city.position.y

        # Générer les points intermédiaires
        points_intersections = creer_intersections((x1, y1), (x2, y2))

        # Créer la route en passant par les points intermédiaires
        for i in range(len(points_intersections) - 1):
            x1, y1 = points_intersections[i]
            x2, y2 = points_intersections[i + 1]
            current_x, current_y = x1, y1

            while current_x != x2 or current_y != y2:
                if current_x < x2:
                    current_x = min(current_x + 1, x2)
                elif current_x > x2:
                    current_x = max(current_x - 1, x2)

                if current_y < y2:
                    current_y = min(current_y + 1, y2)
                elif current_y > y2:
                    current_y = max(current_y - 1, y2)

                pixel = next((p for p in all_pixels if p.x == current_x and p.y == current_y), None)
                if pixel:
                    pixel.set_element("Road")
                    route_pixels.append(pixel)

        return route_pixels

    ######################### STATIC METHODS

    @staticmethod
    def create_roads_between_cities(cities, all_pixels, max_roads):
        """
        Génère des routes entre des paires de villes aléatoires.

        :param cities: Liste des villes.
        :param all_pixels: Liste des pixels disponibles sur le plateau.
        :param max_roads: Nombre maximum de routes à générer.
        :return: Liste d'objets Road.
        """
        roads = []
        city_pairs = set()

        while len(roads) < max_roads and len(city_pairs) < len(cities) * (len(cities) - 1) // 2:
            start_city, end_city = random.sample(cities, 2)
            if (start_city, end_city) not in city_pairs and (end_city, start_city) not in city_pairs:
                road = Road(id=len(roads), start_city=start_city, end_city=end_city, pixels=all_pixels)
                roads.append(road)
                city_pairs.add((start_city, end_city))

        return roads