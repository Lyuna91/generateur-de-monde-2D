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
        
        # Séparation des zones terrestres et lacs
        land_zones = [zone for zone in zones if zone.biome.name not in ["Ocean", "Lake"]]
        lake_zones = [zone for zone in zones if zone.biome.name == "Lake"]
        available_land = set(land_zones)
        available_lakes = set(lake_zones)

        for country_id in range(num_countries):
            if not available_land:
                break

            # Démarrer avec une zone terrestre
            start_zone = random.choice(list(available_land))
            available_land.remove(start_zone)
            country_zones = [start_zone]
            frontier = [start_zone]
            target_size = random.randint(3, 5)
            max_lakes = max(1, target_size // 3)  # Maximum 33% de lacs
            current_lakes = 0

            while frontier and len(country_zones) < target_size:
                current_zone = frontier.pop(0)
                
                # Recherche des zones adjacentes (terre et lacs)
                adjacent_land = [
                    zone for zone in available_land 
                    if current_zone.is_adjacent(zone, distance_threshold=50)
                ]
                adjacent_lakes = [
                    zone for zone in available_lakes 
                    if current_zone.is_adjacent(zone, distance_threshold=50) and current_lakes < max_lakes
                ]

                # Augmenter le seuil si nécessaire
                if not adjacent_land and not adjacent_lakes:
                    adjacent_land = [
                        zone for zone in available_land 
                        if current_zone.is_adjacent(zone, distance_threshold=100)
                    ]
                    adjacent_lakes = [
                        zone for zone in available_lakes 
                        if current_zone.is_adjacent(zone, distance_threshold=100) and current_lakes < max_lakes
                    ]

                # Ajouter des zones terrestres en priorité
                for zone in adjacent_land[:2]:  # Limiter à 2 zones par itération
                    if len(country_zones) < target_size:
                        country_zones.append(zone)
                        frontier.append(zone)
                        available_land.remove(zone)

                # Ajouter un lac si possible
                if adjacent_lakes and current_lakes < max_lakes and len(country_zones) < target_size:
                    lake = adjacent_lakes[0]
                    country_zones.append(lake)
                    frontier.append(lake)
                    available_lakes.remove(lake)
                    current_lakes += 1

            # Créer le pays
            new_country = Country(id=country_id, zones=country_zones)
            countries.append(new_country)

            # Debug info
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
                border_pixels.add(pixel)
        return list(border_pixels)

def generate_country_name():
    title = random.choice(country_titles)
    name = random.choice(prefixes) + random.choice(middles) + random.choice(suffixes)
    return f"{title} {name}"

