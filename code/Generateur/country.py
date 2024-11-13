from .zone import Zone
import random
from math import sqrt
from .names_countries import country_titles, prefixes, middles, suffixes

class Country:
    """
    Classe permettant de définir les pays.
    """

    ######################### INIT

    def __init__(self, id, zones):
        """
        Initialise un pays avec ses caractéristiques de base.

        :param id: Identifiant unique du pays
        :param zones: Liste des zones du pays
        """
        self.id = id
        self.name = generate_country_name()
        self.zones = zones
        self.size = len(zones)  # Taille calculée directement à partir du nombre de zones
        self.border_pixels = self.get_border_pixels()

    def __repr__(self):
        """
        Retourne une représentation du pays sous forme de string.
        """
        return f"Country(id={self.id}, name={self.name}, size={self.size}, zones={len(self.zones)} zones)"

    ######################### METHODS

    @staticmethod
    def create_countries_from_zones(zones, num_countries):
        """
        Crée des pays en regroupant des zones adjacentes sans inclure les zones avec le biome "Ocean".

        :param zones: Liste des zones disponibles
        :param num_countries: Nombre de pays à créer
        :return: Liste d'objets Country
        """
        countries = []
        
        # Filtrer les zones pour exclure celles ayant le biome "Ocean"
        terrestrial_zones = [zone for zone in zones if zone.biome.name != "Ocean"]
        available_zones = set(terrestrial_zones)

        for country_id in range(num_countries):
            if not available_zones:
                break  # Si plus de zones disponibles, arrêter

            # Choisir une zone de départ aléatoire
            start_zone = available_zones.pop()
            country_zones = [start_zone]
            frontier = [start_zone]

            # Définir la taille cible du pays entre 1 et 5 zones
            target_size = random.randint(3, 5)  # Assure une taille minimale de 3 pour plus de chances

            # Parcours en largeur pour ajouter les zones adjacentes
            while frontier and len(country_zones) < target_size:
                current_zone = frontier.pop(0)
                # Premier seuil de distance d'adjacence
                adjacent_zones = [
                    zone for zone in available_zones if current_zone.is_adjacent(zone, distance_threshold=50)
                ]

                # Relâche le seuil d'adjacence si aucune zone trouvée
                if not adjacent_zones and len(country_zones) < target_size:
                    adjacent_zones = [
                        zone for zone in available_zones if current_zone.is_adjacent(zone, distance_threshold=100)
                    ]

                for adj_zone in adjacent_zones:
                    country_zones.append(adj_zone)
                    frontier.append(adj_zone)
                    available_zones.remove(adj_zone)

            # Créer le pays avec les zones trouvées
            new_country = Country(id=country_id, zones=country_zones)
            countries.append(new_country)

            # Print pour vérifier la structure des pays
            print(f"Country ID: {new_country.id}, Name: {new_country.name}")
            print(f"Number of Zones: {len(new_country.zones)}")
            for zone in new_country.zones:
                print(f"  Zone ID: {zone.id}, Seed: {zone.seed}, Biome: {zone.biome.name}")

        return countries
    
    def get_border_pixels(self):
        """
        Calcule et retourne une liste de pixels qui se trouvent à la bordure du pays.
        """
        border_pixels = set()
        all_pixels = {pixel for zone in self.zones for pixel in zone.pixels}
        for pixel in all_pixels:
            x, y = pixel.x, pixel.y
            # Vérifier les pixels adjacents
            adjacent_pixels = [(x-10, y), (x+10, y), (x, y-10), (x, y+10)]
            is_border = False
            for adj_pixel in adjacent_pixels:
                if not any(adj_pixel == (p.x, p.y) for p in all_pixels):
                    is_border = True
                    break
            if is_border:
                print(f"Border Pixel: {pixel.x}, {pixel.y}")
                border_pixels.add(pixel)
        return list(border_pixels)

def generate_country_name():
    title = random.choice(country_titles)
    name = random.choice(prefixes) + random.choice(middles) + random.choice(suffixes)
    return f"{title} {name}"

