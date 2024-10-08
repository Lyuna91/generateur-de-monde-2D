from .zone import Zone
class Country:
    def __init__(self, id, name, size, zones):
        self.id = id
        self.name = name
        self.size = size
        self.zones = zones