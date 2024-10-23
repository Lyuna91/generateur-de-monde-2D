from Visualisateur_Affichage.Enum.class_enum import class_enum

class Panel: 
    """
    Classe Panel permettant de gérer les différentes options de l'interface utilisateur.
    """

######################### INIT

    def __init__(self, Class):
        """
        Initialise un panel avec ses caractéristiques de base.

        :param Class: Classe à afficher
        """
        self.Class = Class

    def __repr__(self):
        """
        Retourne une représentation du panel sous forme de string.
        """
        return f"Panel(Class={self.Class})"

######################### METHODS
    
    def modify_class(self, Class):
        pass
