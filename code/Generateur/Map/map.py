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

    def generateEmptyMap(self, size):
        pass

    def generateMap(self, size, options):
        pass

    def generatePixels(self, size, options):
        pass

    def generateContinent(self, size, options):
        pass

    def generatePangea(self, size, options):
        pass

    def generateArchipelago(self, size, options):
        pass

    def generateBiome(self, size, biome, options):
        pass

    def generateCountry(self, size, options):
        pass

    def generateBorder(self, size, options):
        pass

    def generateRoad(self, size, options):
        pass

    def generateRiver(self, size, options):
        pass

    def generateCities(self, size, options):
        pass


     