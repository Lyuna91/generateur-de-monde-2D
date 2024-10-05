from Generateur.Pixel import Pixel
from Generateur.Border import Border
from Generateur.River import River
from Generateur.Road import Road
from Generateur.City import City
from Generateur.Biome import Biome
from Generateur.Country import Country

class Map: 
    def __init__(self, name, size, options):
        self.name = name
        self.size = size
        self.options = options

    def generate_empty_map(self, size):
        pass

    def generate_map(self, size, options):
        pass

    def generate_pixels(self, size, options):
        pass

    def generate_continent(self, size, options):
        pass

    def generate_pangea(self, size, options):
        pass

    def generate_archipelago(self, size, options):
        pass

    def generate_biome(self, size, biome, options):
        pass

    def generate_country(self, size, options):
        pass

    def generate_border(self, size, options):
        pass

    def generate_road(self, size, options):
        pass

    def generate_river(self, size, options):
        pass

    def generate_cities(self, size, options):
        pass


     