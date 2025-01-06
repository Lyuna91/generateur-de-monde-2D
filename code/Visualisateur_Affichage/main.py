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
R_MAX = 5 # Nombre de rivières pour le slider
ZONES = 100
LAKES = random.randint(3, 6)
MAP_MODE = "Pangea"
MIN_VILLE = COUNTRIES
MAX_VILLE = 15
L_MAX = 5 # Nombre de lacs pour le slider
L_MIN_SIZE = 10
L_MAX_SIZE = 50
PIXEL_SIZE = 5


BUTTON_WIDTH = 20
BUTTON_HEIGHT = 2
BUTTON_FONT = ('Helvetica', 12, 'bold')
# Couleurs générales
BG_COLOR = "#4a90e2"  # Bleu par défaut
HOVER_COLOR = "#357abd"  # Hover bleu foncé
FG_COLOR = "white"

# Couleurs pour les boutons jaunes (modification)
MODIFY_BUTTON_COLOR = "#ffcc00"
MODIFY_HOVER_COLOR = "#ffd700"

# Couleurs pour les boutons rouges (suppression)
DELETE_BUTTON_COLOR = "#ff4444"
DELETE_HOVER_COLOR = "#ff6666"

# Couleurs pour les boutons verts (téléchargement)
DOWNLOAD_BUTTON_COLOR = "#4CAF50"
DOWNLOAD_HOVER_COLOR = "#45A049"


def set_parameters(size, mode):
    """
    Configure les paramètres globaux en fonction de la taille et du mode sélectionnés.
    """
    global COUNTRIES, CITIES, RIVERS, ZONES, MAP_MODE, MIN_VILLE, MAX_VILLE, LAKES

    # Mettre à jour le mode de génération
    MAP_MODE = mode

    # Configurer les paramètres en fonction de la taille
    if size == 'Petit':
        if mode == "Pangea" :
            COUNTRIES = 5
            CITIES = random.randint(7, 10)
            RIVERS = random.randint(1, 3)
            MIN_VILLE = COUNTRIES
            MAX_VILLE = 10
            ZONES = 20
            LAKES = random.randint(0, 2)
            R_MAX = 3
            L_MAX = 2
        if mode == "Archipel" :
            COUNTRIES = 5
            CITIES = random.randint(2, 5)
            RIVERS = random.randint(0, 2)
            MIN_VILLE = COUNTRIES
            MAX_VILLE = 5
            ZONES = 20
            LAKES = random.randint(0, 2)
            R_MAX = 2
            L_MAX = 2
        if mode == "Continent" :
            COUNTRIES = 5
            CITIES = random.randint(5, 10)
            RIVERS = random.randint(0, 3)
            MIN_VILLE = COUNTRIES
            MAX_VILLE = 10
            ZONES = 20
            LAKES = random.randint(0, 2)
            R_MAX = 3
            L_MAX = 2
    elif size == 'Moyen':
        if mode == "Pangea" :
            COUNTRIES = 7
            CITIES = random.randint(10, 20)
            RIVERS = random.randint(1, 6)
            MIN_VILLE = COUNTRIES
            MAX_VILLE = 20
            ZONES = 50
            LAKES = random.randint(3, 6)
            R_MAX = 6
            L_MAX = 5
        if mode == "Archipel" :
            COUNTRIES = 5
            CITIES = random.randint(2, 15)
            RIVERS = random.randint(0, 5)
            MIN_VILLE = COUNTRIES
            MAX_VILLE = 15
            ZONES = 50
            LAKES = random.randint(3, 6)
            R_MAX = 5
            L_MAX = 6
        if mode == "Continent" :
            COUNTRIES = 7
            CITIES = random.randint(7, 20)
            RIVERS = random.randint(0, 6)
            MIN_VILLE = COUNTRIES
            MAX_VILLE = 20
            ZONES = 50
            LAKES = random.randint(3, 6)
            R_MAX = 6
            L_MAX = 6
    elif size == 'Grand':
        if mode == "Pangea" :
            COUNTRIES = 10
            CITIES = random.randint(7, 30)
            RIVERS = random.randint(2, 10)
            MIN_VILLE = COUNTRIES
            MAX_VILLE = 30
            ZONES = 100
            LAKES = random.randint(6, 10)
            R_MAX = 10
            L_MAX = 10
        if mode == "Archipel" :
            COUNTRIES = 10
            CITIES = random.randint(0, 20)
            RIVERS = random.randint(0, 7)
            MIN_VILLE = COUNTRIES
            MAX_VILLE = 20
            ZONES = 100
            LAKES = random.randint(6, 10)
            R_MAX = 7
            L_MAX = 10
        if mode == "Continent" :
            COUNTRIES = 10
            CITIES = random.randint(7, 30)
            RIVERS = random.randint(0, 10)
            MIN_VILLE = COUNTRIES
            MAX_VILLE = 30
            ZONES = 100
            LAKES = random.randint(6, 10)
            R_MAX = 10
            L_MAX = 10

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

    # Fonction pour valider les choix
    def validate_and_close():
        """
        Valider les paramètres sélectionnés et fermer la fenêtre.
        """
        selected_size = size_var.get()
        selected_mode = mode_var.get()
        root.destroy()
        return selected_size, selected_mode

    # Bouton Valider
    tk.Button(
        root, text="Valider", command=validate_and_close,
        width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
        font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR
    ).pack(pady=20)

    root.mainloop()
    return size_var.get(), mode_var.get()  # Retourne les choix



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
            num_rivers=RIVERS, num_zones=ZONES, mode=MAP_MODE, num_lakes=LAKES
        )

        # Initialiser les variables de contrôle
        self.show_borders = tk.BooleanVar(value=False)  # Ajouter cette ligne avant create_widgets
        self.show_countries = tk.BooleanVar(value=True)
        self.show_biomes = tk.BooleanVar(value=False)
        self.show_roads = tk.BooleanVar(value=False)  # Par défaut, routes masquées
        self.show_cities = tk.BooleanVar(value=False)  # Par défaut, villes masquées
        self.show_city_names = tk.BooleanVar(value=False)  # Par défaut, noms des villes masqués
        self.show_country_names = tk.BooleanVar(value=False)  # Par défaut, noms des pays masqués
        
        #Initialiser les sliders des villes , rivières et lacs
        self.city_slider = None
        self.river_slider = None
        self.lake_slider = None

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

        # Conteneur pour les boutons (gauche)
        button_frame_left = tk.Frame(main_container)
        button_frame_left.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

        # Conteneur pour la carte
        map_frame = tk.Frame(main_container)
        map_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Conteneur pour les boutons (droite)
        button_frame_right = tk.Frame(main_container)
        button_frame_right.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

        # Effet hover pour les boutons
        def on_enter(e, widget, hover_color): 
            widget.config(bg=hover_color)

        def on_leave(e, widget, default_color): 
            widget.config(bg=default_color)

        ### Boutons à gauche : Actions principales et curseurs ###

        tk.Label(button_frame_left, text="Actions principales", font=("Helvetica", 14, "bold")).pack(anchor="w", pady=5)

        btn_change_mode = tk.Button(button_frame_left, text="Changer de mode", command=self.restart_generation, 
                            width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR)
        btn_change_mode.pack(pady=5)
        btn_change_mode.bind("<Enter>", lambda e: on_enter(e, btn_change_mode, HOVER_COLOR))
        btn_change_mode.bind("<Leave>", lambda e: on_leave(e, btn_change_mode, BG_COLOR))

        btn_generate = tk.Button(button_frame_left, text="Régénérer la carte", command=self.generate_new_map, 
                                width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR)
        btn_generate.pack(pady=5)
        btn_generate.bind("<Enter>", lambda e: on_enter(e, btn_generate, HOVER_COLOR))
        btn_generate.bind("<Leave>", lambda e: on_leave(e, btn_generate, BG_COLOR))

        tk.Label(button_frame_left, text="Réinitialisations", font=("Helvetica", 14, "bold")).pack(anchor="w", pady=10)

        btn_reset_biomes = tk.Button(button_frame_left, text="Réinitialiser biomes", command=self.reset_biomes, 
                                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR)
        btn_reset_biomes.pack(pady=5)
        btn_reset_biomes.bind("<Enter>", lambda e: on_enter(e, btn_reset_biomes, HOVER_COLOR))
        btn_reset_biomes.bind("<Leave>", lambda e: on_leave(e, btn_reset_biomes, BG_COLOR))

        btn_reset_cities = tk.Button(button_frame_left, text="Réinitialiser villes/routes", command=self.reset_cities_and_roads, 
                                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR)
        btn_reset_cities.pack(pady=5)
        btn_reset_cities.bind("<Enter>", lambda e: on_enter(e, btn_reset_cities, HOVER_COLOR))
        btn_reset_cities.bind("<Leave>", lambda e: on_leave(e, btn_reset_cities, BG_COLOR))

        btn_reset_rivers = tk.Button(button_frame_left, text="Réinitialiser rivières", command=self.reset_rivers, 
                                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR)
        btn_reset_rivers.pack(pady=5)
        btn_reset_rivers.bind("<Enter>", lambda e: on_enter(e, btn_reset_rivers, HOVER_COLOR))
        btn_reset_rivers.bind("<Leave>", lambda e: on_leave(e, btn_reset_rivers, BG_COLOR))

        tk.Label(button_frame_left, text="Nombre d'éléments", font=("Helvetica", 14, "bold")).pack(anchor="w", pady=10)

        tk.Label(button_frame_left, text="Nombre de villes :", font=BUTTON_FONT).pack(pady=5)
        self.city_slider = tk.Scale(button_frame_left, from_=MIN_VILLE, to=MAX_VILLE, orient=tk.HORIZONTAL, command=lambda x: print(f"[DEBUG] Slider changé: {x}"))
        self.city_slider.pack(pady=5)

        tk.Label(button_frame_left, text="Nombre de rivières :", font=BUTTON_FONT).pack(pady=5)
        self.river_slider = tk.Scale(button_frame_left, from_=0, to=R_MAX, orient=tk.HORIZONTAL, command=lambda x: print(f"[DEBUG] Slider changé: {x}"))
        self.river_slider.pack(pady=5)

        tk.Label(button_frame_left, text="Nombre de lacs :", font=BUTTON_FONT).pack(pady=5)
        self.lake_slider = tk.Scale(button_frame_left, from_=0, to=L_MAX, orient=tk.HORIZONTAL, command=lambda x: print(f"[DEBUG] Slider changé: {x}"))
        self.lake_slider.pack(pady=5)

        btn_validate_sliders = tk.Button(button_frame_left, text="Valider les Sliders", command=self.validate_sliders, 
                                        width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT, bg=BG_COLOR, fg=FG_COLOR)
        btn_validate_sliders.pack(pady=5)
        btn_validate_sliders.bind("<Enter>", lambda e: on_enter(e, btn_validate_sliders, HOVER_COLOR))
        btn_validate_sliders.bind("<Leave>", lambda e: on_leave(e, btn_validate_sliders, BG_COLOR))

        ### Boutons à droite : Affichages, modifications, et suppressions ###
        tk.Label(button_frame_right, text="Affichages", font=("Helvetica", 14, "bold")).pack(anchor="w", pady=5)

        tk.Checkbutton(button_frame_right, text="Afficher Pays", variable=self.show_countries,
                    command=lambda: self.handle_checkbox_change("pays"), font=BUTTON_FONT).pack(anchor="w", pady=5)
        tk.Checkbutton(button_frame_right, text="Afficher Biomes", variable=self.show_biomes,
                    command=lambda: self.handle_checkbox_change("biome"), font=BUTTON_FONT).pack(anchor="w", pady=5)
        tk.Checkbutton(button_frame_right, text="Afficher Frontières", variable=self.show_borders,
                    command=self.update_display, font=BUTTON_FONT).pack(anchor="w", pady=5)
        tk.Checkbutton(button_frame_right, text="Afficher Routes", variable=self.show_roads,
                    command=self.update_display, font=BUTTON_FONT).pack(anchor="w", pady=5)
        tk.Checkbutton(button_frame_right, text="Afficher Villes", variable=self.show_cities,
                    command=self.update_display, font=BUTTON_FONT).pack(anchor="w", pady=5)
        tk.Checkbutton(button_frame_right, text="Afficher Noms Villes", variable=self.show_city_names,
                    command=self.update_display, font=BUTTON_FONT).pack(anchor="w", pady=5)
        tk.Checkbutton(button_frame_right, text="Afficher Noms Pays", variable=self.show_country_names,
                    command=self.update_display, font=BUTTON_FONT).pack(anchor="w", pady=5)

        tk.Label(button_frame_right, text="Modifications", font=("Helvetica", 14, "bold")).pack(anchor="w", pady=10)

        btn_edit_city = tk.Button(button_frame_right, text="Modifier Nom Ville", command=self.edit_city_name, 
                                width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT, bg=MODIFY_BUTTON_COLOR, fg="black")
        btn_edit_city.pack(pady=5)
        btn_edit_city.bind("<Enter>", lambda e: on_enter(e, btn_edit_city, MODIFY_HOVER_COLOR))
        btn_edit_city.bind("<Leave>", lambda e: on_leave(e, btn_edit_city, MODIFY_BUTTON_COLOR))

        btn_edit_country = tk.Button(button_frame_right, text="Modifier Nom Pays", command=self.edit_country_name, 
                                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT, bg=MODIFY_BUTTON_COLOR, fg="black")
        btn_edit_country.pack(pady=5)
        btn_edit_country.bind("<Enter>", lambda e: on_enter(e, btn_edit_country, MODIFY_HOVER_COLOR))
        btn_edit_country.bind("<Leave>", lambda e: on_leave(e, btn_edit_country, MODIFY_BUTTON_COLOR))

        tk.Label(button_frame_right, text="Suppressions", font=("Helvetica", 14, "bold")).pack(anchor="w", pady=10)

        btn_delete_city = tk.Button(button_frame_right, text="Supprimer Ville", command=self.delete_city, 
                                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT, bg=DELETE_BUTTON_COLOR, fg="white")
        btn_delete_city.pack(pady=5)
        btn_delete_city.bind("<Enter>", lambda e: on_enter(e, btn_delete_city, DELETE_HOVER_COLOR))
        btn_delete_city.bind("<Leave>", lambda e: on_leave(e, btn_delete_city, DELETE_BUTTON_COLOR))

        btn_delete_country = tk.Button(button_frame_right, text="Supprimer Pays", command=self.delete_country, 
                                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT, bg=DELETE_BUTTON_COLOR, fg="white")
        btn_delete_country.pack(pady=5)
        btn_delete_country.bind("<Enter>", lambda e: on_enter(e, btn_delete_country, DELETE_HOVER_COLOR))
        btn_delete_country.bind("<Leave>", lambda e: on_leave(e, btn_delete_country, DELETE_BUTTON_COLOR))

        btn_delete_road = tk.Button(button_frame_right, text="Supprimer Route", command=self.delete_road, 
                                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT, bg=DELETE_BUTTON_COLOR, fg="white")
        btn_delete_road.pack(pady=5)
        btn_delete_road.bind("<Enter>", lambda e: on_enter(e, btn_delete_road, DELETE_HOVER_COLOR))
        btn_delete_road.bind("<Leave>", lambda e: on_leave(e, btn_delete_road, DELETE_BUTTON_COLOR))

        ### Nouveau bouton pour télécharger l'image ###
        btn_download_image = tk.Button(button_frame_right, text="Télécharger l'image", command=self.download_image, 
                                    width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT, bg=DOWNLOAD_BUTTON_COLOR, fg="white")
        btn_download_image.pack(pady=5)
        btn_download_image.bind("<Enter>", lambda e: on_enter(e, btn_download_image, DOWNLOAD_HOVER_COLOR))
        btn_download_image.bind("<Leave>", lambda e: on_leave(e, btn_download_image, DOWNLOAD_BUTTON_COLOR))


        # Canvas pour afficher la carte
        self.canvas = tk.Canvas(map_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack(expand=True, fill=tk.BOTH)
        


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

    def validate_cities(self):
        nb_cities = self.city_slider.get()
        self.render.map.delete_all_city()
        self.render.map.delete_all_road()
        self.render.map.cities = self.render.map.generate_cities(nb_cities)
        self.render.map.roads = self.render.map.generate_roads()


    def validate_rivers(self):
        nb_rivers = self.river_slider.get()
        self.render.map.delete_all_river()
        self.render.map.rivers = self.render.map.generate_rivers(nb_rivers)
        
    
    def validate_lakes(self):
        nb_lakes = self.lake_slider.get()
        self.render.map.delete_all_lake()
        self.render.map.lakes = self.render.map.generate_lakes(L_MIN_SIZE, L_MAX_SIZE, nb_lakes)
        

    def validate_sliders(self):
        """
        Valide les valeurs des sliders et met à jour la carte.
        """
        self.validate_cities()
        self.validate_rivers()
        self.validate_lakes()
        self.update_canvas()
        
        
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

    def delete_city(self):
        """
        Permet de supprimer une ville sélectionnée et toutes les routes associées.
        """
        # Fenêtre popup pour choisir une ville
        popup = tk.Toplevel(self.root)
        popup.title("Supprimer une ville")
    
        tk.Label(popup, text="Choisissez une ville à supprimer :", font=BUTTON_FONT).pack(pady=5)
    
        # Liste déroulante pour les villes
        city_var = tk.StringVar(value=self.render.map.cities[0].name if self.render.map.cities else "")
        city_menu = tk.OptionMenu(popup, city_var, *[city.name for city in self.render.map.cities])
        city_menu.pack(pady=5)
    
        # Bouton pour valider
        def delete_selected_city():
            selected_city = next(city for city in self.render.map.cities if city.name == city_var.get())
            self.render.map.cities.remove(selected_city)
            
            # Supprimer les routes associées à la ville
            roads_to_remove = [road for road in self.render.map.roads if road.start_city == selected_city or road.end_city == selected_city]
            for road in roads_to_remove:
                self.render.map.roads.remove(road)
                print(f"[INFO] Route supprimée : {road.start_city.name} -> {road.end_city.name}")
    
            print(f"[INFO] Ville supprimée : {selected_city.name}")
            self.update_canvas()
            popup.destroy()
    
        tk.Button(popup, text="Supprimer", command=delete_selected_city,
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

    def delete_country(self):
        """
        Permet de supprimer un pays sélectionné et toutes les villes associées.
        """
        # Fenêtre popup pour choisir un pays
        popup = tk.Toplevel(self.root)
        popup.title("Supprimer un pays")

        tk.Label(popup, text="Choisissez un pays à supprimer :", font=BUTTON_FONT).pack(pady=5)

        # Liste déroulante pour les pays
        country_var = tk.StringVar(value=self.render.map.countries[0].name if self.render.map.countries else "")
        country_menu = tk.OptionMenu(popup, country_var, *[country.name for country in self.render.map.countries])
        country_menu.pack(pady=5)

        # Bouton pour valider
        def delete_selected_country():
            selected_country = next(country for country in self.render.map.countries if country.name == country_var.get())
            self.render.map.countries.remove(selected_country)
            cities_to_remove = [city for city in self.render.map.cities if city.country == selected_country]
            for city in cities_to_remove:
                self.render.map.cities.remove(city)
            print(f"[INFO] Pays supprimé : {selected_country.name}")
            self.update_canvas()
            popup.destroy()

        tk.Button(popup, text="Supprimer", command=delete_selected_country,
                  width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT,
                  bg=BG_COLOR, fg=FG_COLOR).pack(pady=10)

        popup.mainloop()

    def delete_road(self):
        """
        Permet de supprimer une route sélectionnée.
        """
        # Fenêtre popup pour choisir une route
        popup = tk.Toplevel(self.root)
        popup.title("Supprimer une route")

        tk.Label(popup, text="Choisissez une route à supprimer :", font=BUTTON_FONT).pack(pady=5)

        # Liste déroulante pour les routes
        road_var = tk.StringVar(value=f"{self.render.map.roads[0].start_city.name} -> {self.render.map.roads[0].end_city.name}" if self.render.map.roads else "")
        road_menu = tk.OptionMenu(popup, road_var, *[f"{road.start_city.name} -> {road.end_city.name}" for road in self.render.map.roads])
        road_menu.pack(pady=5)

        # Bouton pour valider
        def delete_selected_road():
            selected_road = next(road for road in self.render.map.roads if f"{road.start_city.name} -> {road.end_city.name}" == road_var.get())
            self.render.map.roads.remove(selected_road)
            print(f"[INFO] Route supprimée : {selected_road.start_city.name} -> {selected_road.end_city.name}")
            self.update_canvas()
            popup.destroy()

        tk.Button(popup, text="Supprimer", command=delete_selected_road,
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
    
    def restart_generation(self):
        """
        Redémarre le processus de génération en rouvrant le menu principal.
        """
        self.root.destroy()  # Ferme la fenêtre actuelle

        # Récupérer les nouveaux paramètres
        size, mode = create_menu()

        # Met à jour les paramètres globaux
        set_parameters(size, mode)

        # Relancer l'application principale
        new_root = tk.Tk()
        MapApp(new_root)
        new_root.mainloop()




# Lancer l'application principale
root = tk.Tk()
app = MapApp(root)
root.mainloop()
