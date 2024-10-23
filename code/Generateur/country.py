from .zone import Zone

class Country:

######################### INIT

    def __init__(self, id, name, size, zones):
        """
        Initialise un pays avec ses caractéristiques de base.
        
        :param id: Identifiant unique du pays
        :param name: Nom du pays
        :param zones: Liste des zones du pays
        """
        self.id = id
        self.name = name
        self.zones = zones

    def __repr__(self):
        """
        Retourne une représentation du pays sous forme de string.
        """
        return f"Country(id={self.id}, name={self.name}, zones={self.zones})"
    
######################### METHODS
