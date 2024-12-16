import tkinter as tk
import sys
import os
from PIL import Image, ImageTk
import pygame


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Generateur.map import Map
from Render import Render
import random

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
COUNTRIES = 10
CITIES = 10
RIVERS = 5
ZONES = 100
MAP_MODE = "Pangea"

BUTTON_WIDTH = 20
BUTTON_HEIGHT = 2
BUTTON_FONT = ('Helvetica', 12, 'bold')
BG_COLOR = '#4a90e2'  # Blue
HOVER_COLOR = '#357abd'  # Darker blue
FG_COLOR = 'white'
CHECK_BG = 'white'

def set_parameter(size):
    global COUNTRIES, CITIES, RIVERS, ZONES, MAP_MODE
    
    # Définir les paramètres de la carte en fonction de la taille choisie
    if size == 'Petit': 
        COUNTRIES = 5
        CITIES = random.randint(0, 10)
        RIVERS = random.randint(0, 3)
        ZONES = 20
    elif size == 'Moyen':
        COUNTRIES = 7
        CITIES = random.randint(0, 20)
        RIVERS = random.randint(0, 6)
        ZONES = 50
    elif size == 'Grand':
        COUNTRIES = 10
        CITIES = random.randint(0, 30)
        RIVERS = random.randint(0, 10)
        ZONES = 100
    
    print(f"Paramètres de la Carte : {size}")

    # Ouvrir une fenêtre pour choisir le mode de génération
    choose_mode()

def choose_mode():
    """
    Ouvre une fenêtre pour choisir entre le mode Pangée et Archipel.
    """
    def set_mode(mode):
        global MAP_MODE
        MAP_MODE = mode
        print(f"[INFO] Mode sélectionné : {MAP_MODE}")
        root.destroy()  # Fermer la fenêtre après le choix

    root = tk.Tk()
    root.title("Choix du mode de génération")

    tk.Label(root, text="Choisissez le mode de génération :", font=BUTTON_FONT).pack(pady=10)

    pangea_button = tk.Button(root, text="Pangée", command=lambda: set_mode("Pangea"),
                              width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BG_COLOR, fg=FG_COLOR)
    pangea_button.pack(pady=5)

    archipel_button = tk.Button(root, text="Archipel", command=lambda: set_mode("Archipel"),
                                width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BG_COLOR, fg=FG_COLOR)
    archipel_button.pack(pady=5)

    root.mainloop()

def on_enter(e):
    e.widget['background'] = HOVER_COLOR

def on_leave(e):
    e.widget['background'] = BG_COLOR

def create_menu():
    """
    Menu principal : choix de la taille de la carte, puis du mode de génération.
    """
    def set_parameter_and_mode(size):
        """
        Configure les paramètres en fonction de la taille et ouvre le menu pour choisir le mode.
        """
        global COUNTRIES, CITIES, RIVERS, ZONES, MAP_MODE

        # Paramètres en fonction de la taille
        if size == 'Petit': 
            COUNTRIES = 5
            CITIES = random.randint(0, 10)
            RIVERS = random.randint(0, 3)
            ZONES = 20
        elif size == 'Moyen':
            COUNTRIES = 7
            CITIES = random.randint(0, 20)
            RIVERS = random.randint(0, 6)
            ZONES = 50
        elif size == 'Grand':
            COUNTRIES = 10
            CITIES = random.randint(0, 30)
            RIVERS = random.randint(0, 10)
            ZONES = 100
        
        print(f"Paramètres de la Carte : {size}")

        # Détruire la fenêtre actuelle avant d'ouvrir le choix de mode
        root.destroy()

        # Ouvrir le menu pour choisir le mode de génération
        choose_mode()

    def choose_mode():
        """
        Menu secondaire pour choisir entre Pangée et Archipel.
        """
        def set_mode(mode):
            global MAP_MODE
            MAP_MODE = mode
            print(f"[INFO] Mode sélectionné : {MAP_MODE}")
            mode_root.destroy()  # Fermer la fenêtre après le choix

        mode_root = tk.Tk()
        mode_root.title("Choix du mode de génération")

        tk.Label(mode_root, text="Choisissez le mode de génération :", font=BUTTON_FONT).pack(pady=10)

        pangea_button = tk.Button(mode_root, text="Pangée", command=lambda: set_mode("Pangea"),
                                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BG_COLOR, fg=FG_COLOR)
        pangea_button.pack(pady=5)

        archipel_button = tk.Button(mode_root, text="Archipel", command=lambda: set_mode("Archipel"),
                                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BG_COLOR, fg=FG_COLOR)
        archipel_button.pack(pady=5)

        mode_root.mainloop()

    # Fenêtre principale pour la taille
    root = tk.Tk()
    root.title("Sélectionnez la taille de la carte")

    tk.Label(root, text="Choisissez la taille de la carte :", font=BUTTON_FONT).pack(pady=10)

    small_button = tk.Button(root, text="Petite", command=lambda: set_parameter_and_mode('Petit'),
                             width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BG_COLOR, fg=FG_COLOR)
    small_button.pack(pady=5)

    medium_button = tk.Button(root, text="Moyenne", command=lambda: set_parameter_and_mode('Moyen'),
                              width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BG_COLOR, fg=FG_COLOR)
    medium_button.pack(pady=5)

    large_button = tk.Button(root, text="Grande", command=lambda: set_parameter_and_mode('Grand'),
                             width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=BG_COLOR, fg=FG_COLOR)
    large_button.pack(pady=5)

    root.mainloop()



create_menu()

class MapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Carte avec interface utilisateur")

        # Initialiser Pygame
        pygame.init()
        pygame.display.init()

        # Créer l'instance Render
        self.render = Render(CANVAS_WIDTH, CANVAS_HEIGHT, "Carte", 
                     num_countries=COUNTRIES, num_cities=CITIES, 
                     num_rivers=RIVERS, num_zones=ZONES, mode=MAP_MODE)

        # Créer les widgets Tkinter
        self.create_widgets()
        self.update_canvas()  # Affiche la première carte
    
    def download_image(self):
        """
        Télécharge l'image actuelle de la carte en tant que fichier PNG.
        """
        filename = "map.png"  # Vous pouvez le rendre configurable
        self.render.save_image(filename)
        print(f"[INFO] L'image a été téléchargée : {filename}")

    def create_widgets(self):
        # Create main container
        main_container = tk.Frame(self.root)
        main_container.pack(expand=True, fill=tk.BOTH)

        # Create button frame on the left
        button_frame = tk.Frame(main_container)
        button_frame.pack(side=tk.LEFT, pady=10, padx=10, fill=tk.Y)

        # Add buttons vertically in the button frame
        self.generate_button = tk.Button(button_frame,text="Régénérer la carte",command=self.generate_new_map,width=BUTTON_WIDTH,height=BUTTON_HEIGHT,font=BUTTON_FONT,bg=BG_COLOR,fg=FG_COLOR)
        self.generate_button.pack(pady=5)

        self.reset_cities_button = tk.Button(button_frame,text="Réinitialiser villes/routes",command=self.reset_cities_and_roads,width=BUTTON_WIDTH,height=BUTTON_HEIGHT,font=BUTTON_FONT,bg=BG_COLOR,fg=FG_COLOR)
        self.reset_cities_button.pack(pady=5)

        self.reset_rivers_button = tk.Button(button_frame,text="Réinitialiser rivières",command=self.reset_rivers,width=BUTTON_WIDTH,height=BUTTON_HEIGHT,font=BUTTON_FONT,bg=BG_COLOR,fg=FG_COLOR)
        self.reset_rivers_button.pack(pady=5)

        self.display_countries_button = tk.Button(button_frame,text="Mode Pays",command=lambda: self.render.toggle_display_mode("pays"),width=BUTTON_WIDTH,height=BUTTON_HEIGHT,font=BUTTON_FONT,bg=BG_COLOR,fg=FG_COLOR)
        self.display_countries_button.pack(pady=5)

        self.show_countries = tk.BooleanVar(value=True)
        self.show_biomes = tk.BooleanVar(value=False)

        self.countries_check = tk.Checkbutton(button_frame,text="Afficher Pays",variable=self.show_countries,command=lambda: self.handle_checkbox_change("pays"),bg=CHECK_BG,font=BUTTON_FONT)
        self.countries_check.pack(pady=5, anchor='w')

        self.biomes_check = tk.Checkbutton(button_frame,text="Afficher Biomes",variable=self.show_biomes,command=lambda: self.handle_checkbox_change("biome"),bg=CHECK_BG,font=BUTTON_FONT)
        self.biomes_check.pack(pady=5, anchor='w')

        self.download_button = tk.Button(
        button_frame,
        text="Télécharger l'image",
        command=self.download_image,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        font=BUTTON_FONT,
        bg=BG_COLOR,
        fg=FG_COLOR
        )
        self.download_button.pack(pady=5)

        self.canvas = tk.Canvas(main_container, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)


    def handle_checkbox_change(self, mode):
        """Gère le changement d'état des checkboxes"""
        if mode == "pays":
            self.show_biomes.set(False)
            self.show_countries.set(True)
        else:  # mode == "biome"
            self.show_countries.set(False)
            self.show_biomes.set(True)
        self.update_display()

    
    def update_display(self):
        """Met à jour l'affichage"""
        mode = "pays" if self.show_countries.get() else "biome"
        self.render.toggle_display_mode(mode)
        self.update_canvas()

    def generate_new_map(self):
        # Régénère une nouvelle carte dans l'objet Render
        self.render.generate_map()
        self.update_canvas()

    def reset_cities_and_roads(self):
        """Reset cities and roads and generate new ones"""
        # Delete existing cities and roads
        self.render.map.delete_all_city()
        self.render.map.delete_all_road()
        
        # Generate new cities and roads
        self.render.map.cities = self.render.map.generate_cities(self.render.num_countries)
        self.render.map.roads = self.render.map.generate_roads()
        
        # Update display
        self.update_canvas()

    def reset_rivers(self):
        self.render.map.delete_all_river()
        self.render.map.rivers = self.render.map.generate_rivers(5)
        self.update_canvas()

    def update_canvas(self):
        # Dessine la carte sur la surface Pygame
        self.render.display_pixels()

        # Convertir la surface Pygame en image Tkinter
        pygame_image = pygame.surfarray.array3d(self.render.screen)
        pygame_image = pygame_image.swapaxes(0, 1)  # Inverser les axes pour Tkinter
        img = Image.fromarray(pygame_image)
        img_tk = ImageTk.PhotoImage(img)

        # Afficher l'image dans le Canvas Tkinter
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        self.canvas.image_tk = img_tk  # Empêcher le garbage collector de supprimer l'image


# Création de la fenêtre Tkinter
root = tk.Tk()
app = MapApp(root)
root.mainloop()
