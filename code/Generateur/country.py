from .zone import Zone
import random
from math import sqrt
from .names_countries import country_titles, prefixes, middles, suffixes


class Country:
    """
    Classe permettant de définir les pays."""

######################### INIT

    def __init__(self, id, size, zones):
        """
        Initialise un pays avec ses caractéristiques de base.
        
        :param id: Identifiant unique du pays
        :param name: Nom du pays
        :param zones: Liste des zones du pays
        """
        self.id = id
        self.name = generate_country_name()
        self.zones = zones

    def __repr__(self):
        """
        Retourne une représentation du pays sous forme de string.
        """
        return f"Country(id={self.id}, name={self.name}, zones={self.zones})"
        
    
######################### METHODS

    def generate_countries(self, num_countries):
            """
            Crée des pays en regroupant des zones aléatoires.
            
            :param num_countries: Nombre de pays à créer
            :return: Liste des objets Country
            """
            # Récupérer toutes les zones disponibles
            available_zones = [zone for zone in self.zones if zone.country_id is None]
            countries = []
            
            for country_id in range(num_countries):
                # Définir un nom de pays unique (ex. généré)
                country_name = f"Country_{country_id}"
                
                # Choisir aléatoirement des zones pour ce pays
                country_zones = random.sample(available_zones, k=random.randint(3, 7))
                
                # Créer un objet Country avec ces zones
                new_country = Country(id=country_id, zones=country_zones)
                countries.append(new_country)
                
                # Marquer les zones comme appartenant à ce pays
                for zone in country_zones:
                    zone.country_id = country_id
                    available_zones.remove(zone)

            return countries


    @staticmethod
    def create_countries_from_zones(zones, num_countries):
        countries = []
        available_zones = set(zones)  # Utiliser un set pour une suppression efficace des zones

        for country_id in range(num_countries):
            if not available_zones:
                break  # Si plus de zones disponibles, arrêter

            # Choisir une zone de départ aléatoire pour le pays
            start_zone = available_zones.pop()
            country_zones = [start_zone]
            frontier = [start_zone]

            # Parcours en largeur pour ajouter les zones adjacentes
            while frontier and len(country_zones) < random.randint(3, 5):
                current_zone = frontier.pop(0)  # Prendre la première zone de la frontière
                adjacent_zones = [zone for zone in available_zones if current_zone.is_adjacent(zone, distance_threshold=30)]

                for adj_zone in adjacent_zones:
                    country_zones.append(adj_zone)
                    frontier.append(adj_zone)
                    available_zones.remove(adj_zone)  # Retirer la zone des zones disponibles

            # Créer le pays avec les zones trouvées
            new_country = Country(
                id=country_id,
                size=len(country_zones),
                zones=country_zones
            )
            countries.append(new_country)

            # Print pour afficher les informations du pays créé
            print(f"Country ID: {new_country.id}, Name: {new_country.name}")
            print(f"Number of Zones: {len(new_country.zones)}")
            for zone in new_country.zones:
                print(f"  Zone ID: {zone.id}, Seed: {zone.seed}, Biome: {zone.biome.name}")

        return countries
    
    
def generate_country_name():
    title = random.choice(country_titles)
    name = random.choice(prefixes) + random.choice(middles) + random.choice(suffixes)
    return f"{title} {name}"


