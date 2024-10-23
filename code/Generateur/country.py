from .zone import Zone
class Country:
    def __init__(self, id, name, size, zones):
        self.id = id
        self.name = name
        self.zones = zones # Liste des zones 
