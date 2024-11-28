# import random
# from .country import Country
# from .names_cities import introductions, prefixes, middles, suffixes
# id = 0
# import random

# class City:
#     """
#     Classe permettant de définir les villes."""

# ######################### INIT

#     def __init__(self, id, name, position, country):
#         """
#         Initialise une ville avec ses caractéristiques de base.

#         :param id: Identifiant unique de la ville
#         :param name: Nom de la ville
#         :param position: Position de la ville sur la carte
#         :param country: Pays auquel la ville appartient
#         """
#         self.id = id
#         self.name = name
#         self.position = position
#         self.country = country  

#     def __repr__(self):
#         """
#         Retourne une représentation de la ville sous forme de string.
#         """
#         return f"City(id={self.id}, name={self.name}, position={self.position}, country={self.country})"

# ######################### METHODS

#     def create_city(self):
#         pass

#     def generate_city_name():
#         intro = random.choice(introductions)
#         name = random.choice(prefixes) + random.choice(middles) + random.choice(suffixes)
#         return f"{intro} {name}".strip()
        
        
# for i in range(10):
#     print(City.generate_city_name())

import math
import random
import pygame

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 1000, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Intersections avec divergence")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)

depart = (100, 600)
fin = (500, 400)

def calculer_distance(depart, fin):
    x1, y1 = depart
    x2, y2 = fin
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def calculer_intersections(distance):
    intersections = max(1, round(distance / 110))  # Diviser par une valeur plus grande pour moins de points
    return intersections

def creer_intersections(depart, fin, divergence=1.5):
    x1, y1 = depart
    x2, y2 = fin
    intersections = calculer_intersections(calculer_distance(depart, fin))
    dx = (x2 - x1) / intersections
    dy = (y2 - y1) / intersections
    x, y = x1, y1
    liste_intersections = [depart]  # Ajouter le point de départ
    for i in range(intersections - 1):  # On s'arrête avant le dernier point
        x += dx
        y += dy
        divergence_x = random.uniform(-divergence, divergence) * dx
        divergence_y = random.uniform(-divergence, divergence) * dy
        liste_intersections.append((round((x + divergence_x) / 10) * 10, round((y + divergence_y) / 10) * 10))
    liste_intersections.append(fin)  # Ajouter le point d'arrivée
    return liste_intersections

distance = calculer_distance(depart, fin)
intersections = calculer_intersections(distance)
points_intersections = creer_intersections(depart, fin)
