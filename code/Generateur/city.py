from .country import Country
from .names_cities import introductions, prefixes, middles, suffixes
import random

class City:
    """
    Classe permettant de définir les villes."""

######################### INIT

    def __init__(self, id, name, position, country):
        """
        Initialise une ville avec ses caractéristiques de base.

        :param id: Identifiant unique de la ville
        :param name: Nom de la ville
        :param position: Position de la ville sur la carte
        :param country: Pays auquel la ville appartient
        """
        self.id = id
        self.name = name
        self.position = position
        self.country = country  

    def __repr__(self):
        """
        Retourne une représentation de la ville sous forme de string.
        """
        return f"City(id={self.id}, name={self.name}, position={self.position}, country={self.country})"

######################### METHODS

    def create_city(self):
        pass

    def generate_city_name():
        intro = random.choice(introductions)
        name = random.choice(prefixes) + random.choice(middles) + random.choice(suffixes)
        return f"{intro} {name}".strip()
        
        
for i in range(10):
    print(City.generate_city_name())