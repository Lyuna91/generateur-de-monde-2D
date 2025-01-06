import random

PIXEL_SIZE = 5

class River:
    """
    Classe permettant de définir les rivières à partir des pixels océaniques.
    """
    ######################### INIT

    def __init__(self, id, start_pixel, target_point, all_pixels):
        """
        Initialise une rivière avec ses caractéristiques de base.
        """
        self.id = id
        self.start_pixel = start_pixel
        self.target_point = target_point
        self.river_pixels = self.create_river_pixels(all_pixels)
    
    def __repr__(self):
        """
        Retourne une représentation lisible de la rivière.
        """
        start_coords = f"({self.start_pixel.x}, {self.start_pixel.y})"
        target_coords = f"({self.target_point[0]}, {self.target_point[1]})"
        return f"River(id={self.id}, start={start_coords}, target={target_coords}, length={len(self.river_pixels)})"

    ######################### METHODS

    def create_river_pixels(self, all_pixels):
        """
        Crée une rivière en suivant un chemin organique.
        """
        x1, y1 = self.start_pixel.x, self.start_pixel.y
        x2, y2 = self.target_point
        current_x, current_y = x1, y1

        river_pixels = []
        max_length = 50  # Longueur maximale de la rivière

        for _ in range(max_length):
            if current_x == x2 and current_y == y2:
                break

            dx = x2 - current_x
            dy = y2 - current_y

            # Déterminer une direction prioritaire
            if abs(dx) > abs(dy):
                step_x = PIXEL_SIZE if dx > 0 else -PIXEL_SIZE
                step_y = 0
            else:
                step_x = 0
                step_y = PIXEL_SIZE if dy > 0 else -PIXEL_SIZE

            # Ajouter un mouvement organique
            if random.random() > 0.7:  # 30% de chance de variation
                step_x, step_y = step_y, step_x

            next_x = current_x + step_x
            next_y = current_y + step_y

            # Vérifier que le pixel existe
            next_pixel = next((p for p in all_pixels if p.x == next_x and p.y == next_y), None)
            if next_pixel:
                next_pixel.set_element("River")
                river_pixels.append(next_pixel)

            current_x, current_y = next_x, next_y

        return river_pixels

    @staticmethod
    def create_rivers_from_oceans(ocean_pixels, all_pixels, num_rivers):
        """
        Génère plusieurs rivières à partir des pixels des zones océaniques.
        """
        rivers = []
        for i in range(num_rivers):
            start_pixel = random.choice(ocean_pixels)
            target_point = (random.randint(0, 800), random.randint(0, 600))  # Point aléatoire
            river = River(id=i, start_pixel=start_pixel, target_point=target_point, all_pixels=all_pixels)
            if len(river.river_pixels) > 5:
                rivers.append(river)
                print(f"[DEBUG] Rivière générée : {river}")
            else:
                print(f"[DEBUG] Rivière ignorée (trop courte) : {river}")

        return rivers
    
    @staticmethod
    def delete_all_rivers(rivers):
        """
        Supprime toutes les rivières en vidant la liste fournie et réinitialisant les pixels associés.

        :param rivers: Liste des objets River à supprimer
        """
        for river in rivers:
            for pixel in river.river_pixels:
                pixel.set_element(None)  # Réinitialise les pixels de la rivière
        rivers.clear()
        print("[DEBUG] Toutes les rivières ont été supprimées.")
