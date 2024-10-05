class Biome:
    """
    Classe permettant de définir les biomes.
    """
    
######################### INIT

    def __init__(self, id, name, color, altitude_avg):
        """
        Initialise un biome avec ses caractéristiques de base.
        
        :param id: Identifiant unique du biome
        :param name: Nom du biome (e.g., Forêt, Désert, Montagne)
        :param color: Couleur du biome pour l'affichage graphique
        :param altitude_avg: Altitude moyenne des zones du biome (pour peut être set les pixels autours de la moyenne ?)
        """
        self.id = id
        self.name = name
        self.color = color
        self.altitude_avg = altitude_avg

######################### GETTER

    def get_biome_info(self):
        """
        Retourne les informations du biome.
        """
        return {
            'ID': self.id,
            'Nom': self.name,
            'Couleur': self.color,
            'Altitude Moyenne': self.altitude_avg,
        }
    
######################### BIOME COLOR
    biome_colors = {
        "Forest": (34, 139, 34),
        "Desert": (210, 180, 140),
        "Mountain": (139, 137, 137),
        "Ocean": (0, 105, 148),
        "Plains": (124, 252, 0),
        "Lake": (65, 105, 225),  # Bleu royal pour les lacs
    }

######################### CREATE BIOME

    @staticmethod
    def create_forest_biome():
        """
        Crée et retourne un biome forêt.
        """
        return Biome(id=1, name="Forest", color=Biome.biome_colors["Forest"], altitude_avg=150)

    @staticmethod
    def create_desert_biome():
        """
        Crée et retourne un biome désert.
        """
        return Biome(id=2, name="Desert", color=Biome.biome_colors["Desert"], altitude_avg=50)

    @staticmethod
    def create_mountain_biome():
        """
        Crée et retourne un biome montagne.
        """
        return Biome(id=3, name="Mountain", color=Biome.biome_colors["Mountain"], altitude_avg=300)

    @staticmethod
    def create_ocean_biome():
        """
        Crée et retourne un biome océan.
        """
        return Biome(id=4, name="Ocean", color=Biome.biome_colors["Ocean"], altitude_avg=0)

    @staticmethod
    def create_plains_biome():
        """
        Crée et retourne un biome plaine.
        """
        return Biome(id=5, name="Plains", color=Biome.biome_colors["Plains"], altitude_avg=100)

    @staticmethod
    def create_lake_biome():
        """
        Crée et retourne un biome lac.
        """
        return Biome(id=6, name="Lake", color=Biome.biome_colors["Lake"], altitude_avg=0)
