from Generateur.Zone import Zone
class Pixel:
    def __init__(self, position, zone, altitude, isRiver = False, isBorder= False, isCity = False):
        self.position = position
        self.zone = zone
        self.altitude = altitude
        self.isRiver = isRiver
        self.isBorder = isBorder
        self.isCity = isCity
    