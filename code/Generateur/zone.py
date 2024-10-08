from .pixel import Pixel
class Zone:
    def __init__(self, id , biome, size, seed, pixels):
        self.id = id
        self.biome = biome
        self.size = size
        self.seed = seed
        self.pixels = pixels

    def create_zone(self):
        pass
