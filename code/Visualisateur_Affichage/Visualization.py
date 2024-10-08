
from .render import render

class Visualization:
    def __init__(self, zoom, cameraPosition, render):
        self.zoom = zoom
        self.cameraPosition = cameraPosition
        self.render = render
    
    def update_map_size(self, size, render):
        pass

    def update_camera_position(self, position, render):
        pass

    