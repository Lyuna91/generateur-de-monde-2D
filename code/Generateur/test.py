import random
from .country import Country
id = 0
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

        