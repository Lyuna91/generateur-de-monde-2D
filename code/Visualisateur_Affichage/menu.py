from Visualisateur_Affichage.Enum.display_type import display_type
from Visualisateur_Affichage.Enum.export_type import export_type
from Generateur.map import Map

class Menu:
    """
    Classe Menu permettant de gérer les différentes options de l'interface utilisateur.
    """
    
######################### INIT

    def __init__(self, display_type, export_type, map):
        """
        Initialise un menu avec ses caractéristiques de base.
        
        :param display_type: Type d'affichage
        :param export_type: Type d'export
        :param map: Carte à afficher
        """
        self.display_type = display_type
        self.export_type = export_type
        self.map = map

    def __repr__(self):
        """
        Retourne une représentation du menu sous forme de string.
        """
        return f"Menu(display_type={self.display_type}, export_type={self.export_type}, map={self.map})"    

######################### METHODS

    def export_map(self):
        pass

    def modify_button(self):
        pass

    def modify_map(self):
        pass

    def new_map(self):
        pass

    def display_map(self):
        pass