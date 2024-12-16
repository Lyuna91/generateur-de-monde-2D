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

def set_parameters(size, mode):
    """
    Configure les paramètres globaux en fonction de la taille et du mode sélectionnés.
    """
    global COUNTRIES, CITIES, RIVERS, ZONES, MAP_MODE

    # Mettre à jour le mode de génération
    MAP_MODE = mode

    # Configurer les paramètres en fonction de la taille
    if size == 'Petit':
        if mode == "Pangea" :
            COUNTRIES = 5
            CITIES = random.randint(7, 10)
            RIVERS = random.randint(1, 3)
            ZONES = 20
        if mode == "Archipel" :
            COUNTRIES = 5
            CITIES = random.randint(2, 5)
            RIVERS = random.randint(0, 2)
            ZONES = 20
    elif size == 'Moyen':
        if mode == "Pangea" :
            COUNTRIES = 7
            CITIES = random.randint(10, 20)
            RIVERS = random.randint(1, 6)
            ZONES = 50
        if mode == "Archipel" :
            COUNTRIES = 5
            CITIES = random.randint(2, 15)
            RIVERS = random.randint(0, 5)
            ZONES = 50
    elif size == 'Grand':
        if mode == "Pangea" :
            COUNTRIES = 10
            CITIES = random.randint(7, 30)
            RIVERS = random.randint(2, 10)
            ZONES = 100
        if mode == "Archipel" :
            COUNTRIES = 10
            CITIES = random.randint(0, 20)
            RIVERS = random.randint(0, 7)
            ZONES = 100

    print(f"Paramètres configurés : Taille={size}, Mode={MAP_MODE}")

def create_menu():
    """
    Menu principal pour sélectionner la taille de la carte et le mode de génération.
    """
    root = tk.Tk()
    root.title("Paramètres de génération de la carte")

    # Variables pour les sélections
    size_var = tk.StringVar(value='Moyen')
    mode_var = tk.StringVar(value='Pangea')

    # Choix de la taille
    tk.Label(root, text="Choisissez la taille de la carte :", font=BUTTON_FONT).pack(pady=10)
    for size in ['Petit', 'Moyen', 'Grand']:
        tk.Radiobutton(
            root, text=size, variable=size_var, value=size,
            font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR, selectcolor=HOVER_COLOR
        ).pack(pady=5)

    # Choix du mode
    tk.Label(root, text="Choisissez le mode de génération :", font=BUTTON_FONT).pack(pady=10)
    for mode in ['Pangea', 'Archipel', 'Continent']:
        tk.Radiobutton(
            root, text=mode, variable=mode_var, value=mode,
            font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR, selectcolor=HOVER_COLOR
        ).pack(pady=5)

    # Bouton Valider
    def validate_and_close():
        """
        Valider les paramètres sélectionnés et fermer la fenêtre.
        """
        set_parameters(size_var.get(), mode_var.get())
        root.destroy()

    tk.Button(
        root, text="Valider", command=validate_and_close,
        width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
        font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR
    ).pack(pady=20)

    root.mainloop()


# Appeler le menu principal pour sélectionner les paramètres
create_menu()


class MapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Carte avec interface utilisateur")

        # Initialiser Pygame
        pygame.init()
        pygame.display.init()

        # Créer l'instance Render
        self.render = Render(
            CANVAS_WIDTH, CANVAS_HEIGHT, "Carte",
            num_countries=COUNTRIES, num_cities=CITIES,
            num_rivers=RIVERS, num_zones=ZONES, mode=MAP_MODE
        )

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
        # Conteneur principal
        main_container = tk.Frame(self.root)
        main_container.pack(expand=True, fill=tk.BOTH)

        # Conteneur pour les boutons
        button_frame = tk.Frame(main_container)
        button_frame.pack(side=tk.LEFT, pady=10, padx=10, fill=tk.Y)

        # Boutons de contrôle
        tk.Button(button_frame, text="Régénérer la carte", command=self.generate_new_map,
                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT,
                  bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)

        tk.Button(button_frame, text="Réinitialiser villes/routes", command=self.reset_cities_and_roads,
                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT,
                  bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)

        tk.Button(button_frame, text="Réinitialiser rivières", command=self.reset_rivers,
                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT,
                  bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)

        # Bouton pour télécharger l'image
        tk.Button(button_frame, text="Télécharger l'image", command=self.download_image,
                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT,
                  bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)
        
        # Variables pour les modes d'affichage
        self.show_countries = tk.BooleanVar(value=True)
        self.show_biomes = tk.BooleanVar(value=False)

        # Boutons pour afficher les pays ou les biomes
        tk.Checkbutton(button_frame, text="Afficher Pays", variable=self.show_countries,
                       command=lambda: self.handle_checkbox_change("pays"),
                       font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR, selectcolor=HOVER_COLOR).pack(pady=5, anchor='w')

        tk.Checkbutton(button_frame, text="Afficher Biomes", variable=self.show_biomes,
                       command=lambda: self.handle_checkbox_change("biome"),
                       font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR, selectcolor=HOVER_COLOR).pack(pady=5, anchor='w')

        # Canvas pour afficher la carte
        self.canvas = tk.Canvas(main_container, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    def handle_checkbox_change(self, mode):
        """
        Gère le changement de mode d'affichage (Pays ou Biomes).
        """
        if mode == "pays":
            self.show_biomes.set(False)
            self.show_countries.set(True)
        elif mode == "biome":
            self.show_countries.set(False)
            self.show_biomes.set(True)

        self.update_display()

    def update_display(self):
        """
        Met à jour l'affichage selon le mode sélectionné (Pays ou Biomes).
        """
        mode = "pays" if self.show_countries.get() else "biome"
        self.render.toggle_display_mode(mode)
        self.update_canvas()

    def generate_new_map(self):
        """
        Régénère une nouvelle carte.
        """
        self.render.generate_map()
        self.update_canvas()

    def reset_cities_and_roads(self):
        """
        Réinitialise les villes et les routes, puis en génère de nouvelles.
        """
        self.render.map.delete_all_city()
        self.render.map.delete_all_road()
        self.render.map.cities = self.render.map.generate_cities(self.render.num_countries)
        self.render.map.roads = self.render.map.generate_roads()
        self.update_canvas()

    def reset_rivers(self):
        """
        Réinitialise les rivières, puis en génère de nouvelles.
        """
        self.render.map.delete_all_river()
        self.render.map.rivers = self.render.map.generate_rivers(RIVERS)
        self.update_canvas()

    def update_canvas(self):
        """
        Met à jour le canvas avec l'affichage actuel de la carte.
        """
        self.render.display_pixels()
        pygame_image = pygame.surfarray.array3d(self.render.screen)
        pygame_image = pygame_image.swapaxes(0, 1)
        img = Image.fromarray(pygame_image)
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        self.canvas.image_tk = img_tk  # Empêche le garbage collector de supprimer l'image


# Lancer l'application principale
root = tk.Tk()
app = MapApp(root)
root.mainloop()
