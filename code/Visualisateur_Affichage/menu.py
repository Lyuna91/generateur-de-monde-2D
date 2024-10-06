from Visualisateur_Affichage.Enum.DisplayType import DisplayType
from Visualisateur_Affichage.Enum.ExportType import ExportType
from Generateur.Map.map import Map

class Menu:
    def __init__(self, displayType, exportType, map):
        self.displayType = displayType
        self.exportType = exportType
        self.map = map

    def exportMap(self):
        pass

    def ModifyButton(self):
        pass

    def modifyMap(self):
        pass

    def newMap(self):
        pass

    def displayMap(self):
        pass