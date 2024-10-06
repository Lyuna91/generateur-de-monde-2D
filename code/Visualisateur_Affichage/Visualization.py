
from Visualisateur_Affichage.Render import Render

class Visualization:
    def __init__(self, zoom, cameraPosition, render):
        self.zoom = zoom
        self.cameraPosition = cameraPosition
        self.render = render
    
    def updateMapSize(self, size, render):
        pass

    def updateCameraPosition(self, position, render):
        pass

    