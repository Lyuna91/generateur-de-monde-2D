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

BUTTON_WIDTH = 20
BUTTON_HEIGHT = 2
BUTTON_FONT = ('Helvetica', 12, 'bold')
BG_COLOR = '#4a90e2'  # Blue
HOVER_COLOR = '#357abd'  # Darker blue
FG_COLOR = 'white'

def set_parameter(size):
    global COUNTRIES, CITIES, RIVERS, ZONES
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
    
    print(f"Parametres de la Carte : {size}")

def on_enter(e):
    e.widget['background'] = HOVER_COLOR

def on_leave(e):
    e.widget['background'] = BG_COLOR

def create_menu():
    root = tk.Tk()
    root.title("Select Map Size")

    small_button = tk.Button(root,text="Petite",command=lambda: [set_parameter('Petit'), root.destroy()],width=BUTTON_WIDTH,height=BUTTON_HEIGHT,font=BUTTON_FONT,bg=BG_COLOR,fg=FG_COLOR,relief='flat',cursor='hand2')
    small_button.pack(pady=10)
    small_button.bind("<Enter>", on_enter)
    small_button.bind("<Leave>", on_leave)

    medium_button = tk.Button(root,text="Moyenne",command=lambda: [set_parameter('Moyen'), root.destroy()],width=BUTTON_WIDTH,height=BUTTON_HEIGHT,font=BUTTON_FONT,bg=BG_COLOR,fg=FG_COLOR,relief='flat',cursor='hand2')
    medium_button.pack(pady=10)
    medium_button.bind("<Enter>", on_enter)
    medium_button.bind("<Leave>", on_leave)

    large_button = tk.Button(root,text="Grande",command=lambda: [set_parameter('Grand'), root.destroy()],width=BUTTON_WIDTH,height=BUTTON_HEIGHT,font=BUTTON_FONT,bg=BG_COLOR,fg=FG_COLOR,relief='flat',cursor='hand2')
    large_button.pack(pady=10)
    large_button.bind("<Enter>", on_enter)
    large_button.bind("<Leave>", on_leave)

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
        self.render = Render(CANVAS_WIDTH, CANVAS_HEIGHT, "Carte", num_countries=COUNTRIES, num_cities=CITIES, num_rivers=RIVERS, num_zones=ZONES)

        # Créer les widgets Tkinter
        self.create_widgets()
        self.update_canvas()  # Affiche la première carte

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

        # Create canvas on the right
        self.canvas = tk.Canvas(main_container, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

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
