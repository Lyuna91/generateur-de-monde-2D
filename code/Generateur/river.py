import random

class River:
    """
    Classe permettant de définir les rivières à partir des pixels océaniques.
    """

    def __init__(self, id, start_pixel, all_pixels):
        """
        Initialise une rivière avec ses caractéristiques de base.

        :param id: Identifiant unique de la rivière
        :param start_pixel: Pixel de départ (dans un biome océanique)
        :param all_pixels: Liste de tous les pixels disponibles
        """
        self.id = id
        self.start_pixel = start_pixel
        self.route_pixels = self.create_route_pixels(all_pixels)

    def __repr__(self):
        """
        Retourne une représentation de la rivière sous forme de chaîne de caractères.
        """
        return f"River(id={self.id}, start_pixel=({self.start_pixel.x}, {self.start_pixel.y}), pixels={len(self.route_pixels)})"

    def create_route_pixels(self, all_pixels):
        """
        Crée une rivière à partir d'un point de départ en suivant une logique similaire à celle des routes.

        :param all_pixels: Liste des pixels disponibles.
        :return: Liste des pixels formant la rivière.
        """
        current_pixel = self.start_pixel
        route_pixels = [current_pixel]

        for _ in range(30):  # Limite de longueur de la rivière
            adjacent_pixels = [
                p for p in all_pixels
                if (abs(p.x - current_pixel.x) == 10 and p.y == current_pixel.y) or
                   (abs(p.y - current_pixel.y) == 10 and p.x == current_pixel.x)
            ]

            if not adjacent_pixels:
                break

            next_pixel = random.choice(adjacent_pixels)
            next_pixel.set_element("River")
            route_pixels.append(next_pixel)
            current_pixel = next_pixel

        return route_pixels

    @staticmethod
    def create_rivers_from_oceans(ocean_pixels, num_rivers):
        """
        Génère plusieurs rivières à partir des pixels des zones océaniques.

        :param ocean_pixels: Liste des pixels des zones océaniques.
        :param num_rivers: Nombre de rivières à générer.
        :return: Liste d'objets River.
        """
        if not ocean_pixels:
            print("Aucun pixel océan trouvé. Impossible de générer des rivières.")
            return []

        rivers = []
        for i in range(min(num_rivers, len(ocean_pixels))):
            start_pixel = random.choice(ocean_pixels)
            river = River(id=i, start_pixel=start_pixel, all_pixels=ocean_pixels)
            if river.route_pixels:
                rivers.append(river)

        return rivers
