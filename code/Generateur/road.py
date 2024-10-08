from .pixel import Pixel
class Road:
    def __init__(self, id, pixels):
        self.id = id
        self.pixels = pixels    

    def create_road(self):
        return self