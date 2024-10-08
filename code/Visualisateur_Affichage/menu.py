from Visualisateur_Affichage.Enum.DisplayType import DisplayType
from Visualisateur_Affichage.Enum.ExportType import ExportType
from Generateur.Map.map import Map

class Menu:
    def __init__(self, displayType, exportType, map):
        self.displayType = displayType
        self.exportType = exportType
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