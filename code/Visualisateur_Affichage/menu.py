from Visualisateur_Affichage.Enum.display_type import display_type
from Visualisateur_Affichage.Enum.export_type import export_type
from Generateur.map import Map

class Menu:
    def __init__(self, display_type, export_type, map):
        self.display_type = display_type
        self.export_type = export_type
        self.map = map

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