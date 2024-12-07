import tkinter as tk
import sys
import os
from PIL import Image, ImageTk
import pygame


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Generateur.map import Map
from Render import Render

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

class MapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Carte avec interface utilisateur")

        # Initialiser Pygame
        pygame.init()
        pygame.display.init()

        # Créer l'instance Render
        self.render = Render(CANVAS_WIDTH, CANVAS_HEIGHT, "Carte", num_countries=5)

        # Créer les widgets Tkinter
        self.create_widgets()
        self.update_canvas()  # Affiche la première carte

    def create_widgets(self):
        # Previous widgets remain the same
        self.canvas = tk.Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Generate map button
        self.generate_button = tk.Button(button_frame, text="Régénérer la carte", 
                                       command=self.generate_new_map)
        self.generate_button.pack(side=tk.LEFT, padx=5)

        # Reset cities and roads button
        self.reset_button = tk.Button(button_frame, text="Réinitialiser villes/routes", 
                                    command=self.reset_cities_and_roads)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # Reset rivers button
        self.reset_button = tk.Button(button_frame, text="Réinitialiser rivières", 
                                    command=self.reset_rivers)
        self.reset_button.pack(side=tk.LEFT, padx=5)

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
