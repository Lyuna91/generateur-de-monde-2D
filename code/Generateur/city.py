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


def generate_position(Country):
    zone = Country.zones[random.randint(0, len(Country.zones)-1)]
    pixel = zone.pixels[random.randint(0, len(zone.pixels)-1)]
    while pixel in Country.border_pixels or zone.biome.name == "Ocean" or zone.biome.name == "Lake":
        pixel = zone.pixels[random.randint(0, len(zone.pixels)-1)]
        pixel.set_element("city")
    return pixel
        