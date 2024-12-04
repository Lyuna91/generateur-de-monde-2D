import random

class River:
    """
    Classe permettant de définir les rivières à partir des pixels océaniques.
    """

    def __init__(self, id, start_pixel, all_pixels, map_width, map_height):
        """
        Initialise une rivière avec ses caractéristiques de base.

        :param id: Identifiant unique de la rivière
        :param start_pixel: Pixel de départ (dans un biome océanique)
        :param all_pixels: Liste de tous les pixels disponibles
        :param map_width: Largeur de la carte
        :param map_height: Hauteur de la carte
        """
        self.id = id
        self.start_pixel = start_pixel
        self.all_pixels = all_pixels
        self.map_width = map_width
        self.map_height = map_height
        self.route_pixels = self.create_route_pixels()

    def __repr__(self):
        """
        Retourne une représentation de la rivière sous forme de chaîne de caractères.
        """
        end_pixel = self.route_pixels[-1] if self.route_pixels else None
        end_coords = (end_pixel.x, end_pixel.y) if end_pixel else "Inconnu"
        return f"River(id={self.id}, start=({self.start_pixel.x}, {self.start_pixel.y}), end={end_coords}, length={len(self.route_pixels)})"

    def create_route_pixels(self):
        """
        Génère une rivière avec une trajectoire organique.
        """
        current_pixel = self.start_pixel
        route_pixels = [current_pixel]
        max_length = 50
        deviation_chance = 0.3  # Probabilité de changer de direction

        print(f"[DEBUG] Début de la création de la rivière depuis ({current_pixel.x}, {current_pixel.y})")

        for _ in range(max_length):
            # Choix aléatoire d'un pixel adjacent
            possible_directions = [
                (10, 0), (-10, 0), (0, 10), (0, -10),
                (10, 10), (-10, -10), (10, -10), (-10, 10)
            ]
            if random.random() < deviation_chance:
                random.shuffle(possible_directions)  # Ajout de variété dans les directions

            for dx, dy in possible_directions:
                next_x = current_pixel.x + dx
                next_y = current_pixel.y + dy

                if 0 <= next_x < self.map_width and 0 <= next_y < self.map_height:
                    next_pixel = next((p for p in self.all_pixels if p.x == next_x and p.y == next_y), None)
                    if next_pixel and next_pixel not in route_pixels:
                        next_pixel.set_element("River")
                        route_pixels.append(next_pixel)
                        current_pixel = next_pixel
                        break

        print(f"[DEBUG] Fin de la création de la rivière. Longueur totale : {len(route_pixels)}")
        return route_pixels

    @staticmethod
    def create_rivers_from_oceans(ocean_pixels, all_pixels, num_rivers, map_width, map_height):
        """
        Génère plusieurs rivières à partir des pixels océaniques.
        """
        rivers = []
        for i in range(num_rivers):
            start_pixel = random.choice(ocean_pixels)
            river = River(id=i, start_pixel=start_pixel, all_pixels=all_pixels, map_width=map_width, map_height=map_height)

            if len(river.route_pixels) >= 10:  # Filtrer les rivières trop courtes
                rivers.append(river)
                print(f"[DEBUG] Rivière générée : {river}")
            else:
                print(f"[DEBUG] Rivière ignorée (trop courte)")

        print(f"[DEBUG] Nombre total de rivières générées : {len(rivers)}")
        return rivers
