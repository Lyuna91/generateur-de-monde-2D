from .country import Country
from .names_cities import introductions, prefixes, middles, suffixes
import random

class City:
    """
    Classe permettant de définir les villes."""

######################### INIT

    def __init__(self, id, position, country):
        """
        Initialise une ville avec ses caractéristiques de base.

        :param id: Identifiant unique de la ville
        :param name: Nom de la ville
        :param position: Position de la ville sur la carte
        :param country: Pays auquel la ville appartient
        """
        self.id = id
        self.name = generate_city_name()
        self.position = position
        self.country = country  

    def __repr__(self):
        """
        Retourne une représentation de la ville sous forme de string.
        """
        return f"City {self.id}: {self.name}, Position: ({self.position.x}, {self.position.y}), Country: {self.country.name}"

######################### METHODS

    def create_city(self):
        pass

    def create_cities_from_countries(countries, num_cities):
        cities = []
        i = 0
        for country in countries:
            position = generate_position(country)
            city = City(i, position, country)
            cities.append(city)
            i += 1
            print(city)
        cities_positions = [city.position for city in cities]
        if i < num_cities:
            while i < num_cities:
                position = generate_position(countries[random.randint(0, len(countries)-1)])
                while position in cities:
                    position = generate_position(countries[random.randint(0, len(countries)-1)])
                city = City(i, position, countries[random.randint(0, len(countries)-1)])
                cities.append(city)
                cities_positions.append(position)
                i += 1
                print(city)
        return cities
    
def generate_city_name():
    intro = random.choice(introductions)
    name = random.choice(prefixes) + random.choice(middles) + random.choice(suffixes)
    return f"{intro} {name}".strip()


def generate_position(country):
    """
    Génère une position valide pour une ville dans un pays donné.
    """
    
    # Obtenir tous les pixels valides du pays
    pixels_valides = []
    for zone in country.zones:
        if zone.biome.name not in ["Ocean", "Lake"]:
            pixels_valides.extend([p for p in zone.pixels if p not in country.border_pixels and p.element is None])
    
    # Si aucun pixel valide n'est trouvé, utiliser n'importe quel pixel non-océanique
    if not pixels_valides:
        for zone in country.zones:
            if zone.biome.name not in ["Ocean", "Lake"]:
                pixels_valides.extend(zone.pixels)
    
    # Si toujours aucun pixel valide, lever une exception
    if not pixels_valides:
        raise ValueError(f"Impossible de trouver une position valide pour une ville dans le pays {country.id}")
    
    # Sélectionner un pixel aléatoire parmi les pixels valides
    position = random.choice(pixels_valides)
    position.set_element("city")

    return position
