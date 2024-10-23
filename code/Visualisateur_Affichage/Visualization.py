from .render import render

class Visualization:
    """
    Classe permettant de gérer la visualisation de la carte générée.
    """

######################### INIT

    def __init__(self, zoom, cameraPosition, render):
        """
        Initialise une visualisation avec ses caractéristiques de base.
        
        :param zoom: Zoom de la carte
        :param cameraPosition: Position de la caméra
        :param render: Rendu de la carte
        """
        self.zoom = zoom
        self.cameraPosition = cameraPosition
        self.render = render
    
    def __repr__(self):
        """
        Retourne une représentation de la visualisation sous forme de string.
        """
        return f"Visualization(zoom={self.zoom}, cameraPosition={self.cameraPosition}, render={self.render})"
    
######################### METHODS

    def update_map_size(self, size, render):
        pass

    def update_camera_position(self, position, render):
        pass

    