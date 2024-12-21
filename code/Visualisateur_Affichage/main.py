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

PIXEL_SIZE = 5


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

        # Initialiser les variables de contrôle
        self.show_borders = tk.BooleanVar(value=False)  # Ajouter cette ligne avant create_widgets
        self.show_countries = tk.BooleanVar(value=True)
        self.show_biomes = tk.BooleanVar(value=False)
        self.show_roads = tk.BooleanVar(value=False)  # Par défaut, routes masquées
        self.show_cities = tk.BooleanVar(value=False)  # Par défaut, villes masquées
        self.show_city_names = tk.BooleanVar(value=False)  # Par défaut, noms des villes masqués
        self.show_country_names = tk.BooleanVar(value=False)  # Par défaut, noms des pays masqués


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
        
        tk.Button(button_frame, text="Réinitialiser biomes", command=self.reset_biomes, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)        
            
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

        tk.Checkbutton(button_frame, text="Afficher Frontières", variable=self.show_borders,
               command=self.update_display,
               font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR, selectcolor=HOVER_COLOR).pack(pady=5, anchor='w')

        tk.Checkbutton(button_frame, text="Afficher Routes", variable=self.show_roads,
               command=self.update_display,
               font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR, selectcolor=HOVER_COLOR).pack(pady=5, anchor='w')

        tk.Checkbutton(button_frame, text="Afficher Villes", variable=self.show_cities,
               command=self.update_display,
               font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR, selectcolor=HOVER_COLOR).pack(pady=5, anchor='w')
        
        tk.Checkbutton(button_frame, text="Afficher Noms Villes", variable=self.show_city_names,
               command=self.update_display,
               font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR, selectcolor=HOVER_COLOR).pack(pady=5, anchor='w')

        tk.Checkbutton(button_frame, text="Afficher Noms Pays", variable=self.show_country_names,
               command=self.update_display,
               font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR, selectcolor=HOVER_COLOR).pack(pady=5, anchor='w')

        tk.Button(button_frame, text="Modifier Nom Ville", command=self.edit_city_name,
          width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT,
          bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)

        tk.Button(button_frame, text="Modifier Nom Pays", command=self.edit_country_name,
          width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT,
          bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)

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
        Met à jour l'affichage selon les options sélectionnées.
        """
        mode = "pays" if self.show_countries.get() else "biome"
        self.render.show_borders = self.show_borders.get()
        self.render.show_roads = self.show_roads.get()
        self.render.show_cities = self.show_cities.get()
        self.render.show_city_names = self.show_city_names.get()  # Nouvel état pour les noms des villes
        self.render.show_country_names = self.show_country_names.get()  # Nouvel état pour les noms des pays
        self.render.toggle_display_mode(mode)
        self.update_canvas()


    def generate_new_map(self):
        """
        Régénère une nouvelle carte.
        """
        self.render.generate_map()
        self.update_canvas()

    def reset_biomes(self):
        """
        Réinitialise les biomes, puis en génère de nouveaux.
        """
        self.render.map.delete_all_biome()
        self.render.map.biomes = self.render.map.generate_biomes_after_deletion()
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

    def edit_city_name(self):
        """
        Permet de modifier le nom d'une ville sélectionnée.
        """
        # Fenêtre popup pour choisir une ville
        popup = tk.Toplevel(self.root)
        popup.title("Modifier le nom de la ville")

        tk.Label(popup, text="Choisissez une ville :", font=BUTTON_FONT).pack(pady=5)

        # Liste déroulante pour les villes
        city_var = tk.StringVar(value=self.render.map.cities[0].name if self.render.map.cities else "")
        city_menu = tk.OptionMenu(popup, city_var, *[city.name for city in self.render.map.cities])
        city_menu.pack(pady=5)

        # Entrée pour le nouveau nom
        tk.Label(popup, text="Nouveau nom :", font=BUTTON_FONT).pack(pady=5)
        new_name_entry = tk.Entry(popup, font=BUTTON_FONT)
        new_name_entry.pack(pady=5)

        # Bouton pour valider
        def update_city_name():
            selected_city = next(city for city in self.render.map.cities if city.name == city_var.get())
            new_name = new_name_entry.get()
            if new_name:
                selected_city.name = new_name
                print(f"[INFO] Nom de la ville modifié : {selected_city.name}")
                self.update_canvas()
            popup.destroy()

        tk.Button(popup, text="Valider", command=update_city_name,
                width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT,
                bg=BG_COLOR, fg=FG_COLOR).pack(pady=10)

        popup.mainloop()

    def edit_country_name(self):
        """
        Permet de modifier le nom d'un pays sélectionné.
        """
        # Fenêtre popup pour choisir un pays
        popup = tk.Toplevel(self.root)
        popup.title("Modifier le nom du pays")

        tk.Label(popup, text="Choisissez un pays :", font=BUTTON_FONT).pack(pady=5)

        # Liste déroulante pour les pays
        country_var = tk.StringVar(value=self.render.map.countries[0].name if self.render.map.countries else "")
        country_menu = tk.OptionMenu(popup, country_var, *[country.name for country in self.render.map.countries])
        country_menu.pack(pady=5)

        # Entrée pour le nouveau nom
        tk.Label(popup, text="Nouveau nom :", font=BUTTON_FONT).pack(pady=5)
        new_name_entry = tk.Entry(popup, font=BUTTON_FONT)
        new_name_entry.pack(pady=5)

        # Bouton pour valider
        def update_country_name():
            selected_country = next(country for country in self.render.map.countries if country.name == country_var.get())
            new_name = new_name_entry.get()
            if new_name:
                selected_country.name = new_name
                print(f"[INFO] Nom du pays modifié : {selected_country.name}")
                self.update_canvas()
            popup.destroy()

        tk.Button(popup, text="Valider", command=update_country_name,
                width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT,
                bg=BG_COLOR, fg=FG_COLOR).pack(pady=10)

        popup.mainloop()


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
