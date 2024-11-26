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
        Crée une ligne de pixels entre les points de départ et d'arrivée en avançant de 10 en 10 pour X et Y.

        :param all_pixels: Liste des pixels disponibles sur le plateau.
        :return: Liste des pixels formant la route.
        """
        route_pixels = []
        x1, y1 = self.start_city.position.x, self.start_city.position.y
        x2, y2 = self.end_city.position.x, self.end_city.position.y

        # Variables actuelles
        current_x, current_y = x1, y1

        # Tant que nous n'avons pas atteint la destination
        while current_x != x2 or current_y != y2:
            # Ajuster X vers la cible
            if current_x < x2:
                current_x = min(current_x + 10, x2)  # Avancer de 10 ou s'arrêter à x2
            elif current_x > x2:
                current_x = max(current_x - 10, x2)  # Reculer de 10 ou s'arrêter à x2

            # Ajuster Y vers la cible
            if current_y < y2:
                current_y = min(current_y + 10, y2)  # Avancer de 10 ou s'arrêter à y2
            elif current_y > y2:
                current_y = max(current_y - 10, y2)  # Reculer de 10 ou s'arrêter à y2

            # Trouver le pixel correspondant dans la liste des pixels existants
            pixel = next((p for p in all_pixels if p.x == current_x and p.y == current_y), None)
            if pixel:
                pixel.set_element("Road")  # Marquer le pixel comme une route
                route_pixels.append(pixel)  # Ajouter le pixel à la liste de la route

        return route_pixels


    ######################### STATIC METHODS

    @staticmethod
    def create_roads_between_cities(cities, all_pixels):
        """
        Génère des routes entre toutes les villes disponibles.

        :param cities: Liste des villes.
        :param all_pixels: Liste des pixels disponibles sur le plateau.
        :return: Liste d'objets Road.
        """
        roads = []
        for i, start_city in enumerate(cities[:-1]):
            end_city = cities[i + 1]
            road = Road(id=len(roads), start_city=start_city, end_city=end_city, pixels=all_pixels)
            roads.append(road)
        return roads
