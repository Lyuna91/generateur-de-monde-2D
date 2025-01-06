# Documentation Technique du Projet de Génération de Cartes 2D

## Introduction

Ce document vise à fournir une vue détaillée sur les aspects techniques du projet de génération aléatoire de cartes en 2D, incluant les classes, fonctions, et modules utilisés dans le code. Il est destiné aux développeurs et autres parties prenantes qui souhaitent comprendre les éléments techniques sans parcourir le code source en détail.

---

## Structure du Projet

Le projet est organisé autour des modules suivants :

### 1. **Modules Principaux**

- **`map.py`** : Gère la création et la gestion de la carte principale.
- **`pixel.py`** : Définit les pixels comme éléments unitaires de la carte.
- **`zone.py`** : Implémente la division en zones basée sur l'algorithme de Voronoi.
- **`river.py`** : Modélise les rivières sur la carte.
- **`road.py`** : Implémente les routes entre les villes.
- **`city.py`** : Gère les villes, incluant leur positionnement et leur nommage.
- **`country.py`** : Regroupe les zones pour former des pays.
- **`biome.py`** : Définit les différents types de biomes (forêts, déserts, montagnes, etc.).
- **`lake.py`** : Gère la création et l'organisation des lacs.
- **`main.py`** : Point d'entrée principal avec une interface utilisateur graphique (Tkinter) pour interagir avec la carte.
- **`Render.py`** : Gère l'affichage graphique des éléments de la carte à l'aide de Pygame.

---

## Détails des Classes et Fonctions

### **1. `map.py`**

Classe principale pour la création et la gestion de la carte.

- **Attributs principaux :**

  - `zones` : Liste des zones Voronoi.
  - `countries` : Liste des pays.
  - `cities` : Liste des villes.
  - `roads` : Liste des routes.
  - `rivers` : Liste des rivières.
  - `lakes` : Liste des lacs.

- **Fonctions principales :**
  - `generate_map()` : Génère les éléments de la carte en fonction des paramètres (biomes, pays, villes, etc.).
  - `delete_all_*()` : Supprime les éléments spécifiés (lacs, rivières, etc.).
  - `assign_biomes()` : Associe des biomes à chaque zone.

### **2. `pixel.py`**

Représente chaque pixel comme unité de base de la carte.

- **Attributs principaux :**

  - `x, y` : Coordonnées du pixel.
  - `color` : Couleur associée au biome ou à l'élément.
  - `altitude` : Altitude du pixel.

- **Fonctions principales :**
  - `set_color()` : Modifie la couleur du pixel.
  - `set_element()` : Associe un élément (rivère, route) au pixel.

### **3. `zone.py`**

Implemente les zones de Voronoi.

- **Attributs principaux :**

  - `id` : Identifiant unique de la zone.
  - `seed` : Centre de la zone.
  - `pixels` : Liste des pixels appartenant à la zone.

- **Fonctions principales :**
  - `generate_voronoi_zones()` : Crée des zones Voronoi sur la carte.
  - `is_adjacent()` : Détermine si une autre zone est adjacente.

### **4. `river.py`**

Représente les rivières sur la carte.

- **Fonctions principales :**
  - `create_rivers_from_oceans()` : Crée des rivières à partir des zones océaniques.
  - `create_route_pixels()` : Génère le tracé de la rivière.

### **5. `road.py`**

Crée et gère les routes connectant les villes.

- **Fonctions principales :**
  - `create_roads_between_cities()` : Crée des routes entre les villes aléatoirement ou suivant un ordre logique.

### **6. `city.py`**

Gère les villes et leur distribution sur la carte.

- **Fonctions principales :**
  - `create_cities_from_countries()` : Crée des villes en fonction des pays.
  - `generate_city_name()` : Génère un nom aléatoire pour une ville.

### **7. `country.py`**

Organise les pays et leurs zones.

- **Fonctions principales :**
  - `create_countries_from_zones()` : Crée des pays en regroupant des zones adjacentes.
  - `get_border_pixels()` : Identifie les pixels à la frontière d'un pays.

### **8. `biome.py`**

Définit les différents types de biomes.

- **Fonctions principales :**
  - `create_random_biome()` : Génère un biome aléatoire.
  - `create_ocean_biome()` : Crée un biome de type océan.

### **9. `lake.py`**

Modélise les lacs.

- **Fonctions principales :**
  - `create_lakes()` : Crée des lacs sur la carte en respectant certaines contraintes.

### **10. `main.py`**

Gère l'interface utilisateur pour configurer et afficher la carte.

- **Fonctions principales :**
  - `create_menu()` : Permet à l'utilisateur de configurer la taille et le mode de la carte.
  - `MapApp` : Classe principale pour gérer l'interface graphique avec des options pour afficher, modifier, et télécharger la carte.

### **11. `Render.py`**

Gère l'affichage graphique de la carte et de ses éléments.

- **Attributs principaux :**

  - `screen` : Surface graphique pour le rendu des éléments.
  - `map` : Instance de la classe `Map` pour gérer les éléments.
  - `display_mode` : Mode d'affichage (« biome » ou « pays »).

- **Fonctions principales :**
  - `generate_map()` : Génère la carte en fonction des paramètres définis.
  - `display_pixels()` : Affiche les éléments de la carte sur la surface graphique.
  - `toggle_display_mode()` : Alterne entre les différents modes d'affichage.
  - `save_image()` : Sauvegarde l'image actuelle de la carte au format PNG.

---

## Interactions entre les Modules

1. **Génération des Pixels :**

   - Les pixels sont créés et attribués à des zones (module `pixel.py` et `zone.py`).

2. **Assemblage des Zones :**

   - Les zones sont regroupées pour former des pays (`zone.py` et `country.py`).

3. **Ajout d'Éléments Naturels :**

   - Les biomes, lacs, rivières et routes sont générés après la création des zones (`biome.py`, `lake.py`, `river.py`, `road.py`).

4. **Affichage Graphique :**

   - Le module `Render.py` gère l'affichage des éléments graphiques à l'aide de Pygame.

5. **Interface Utilisateur :**
   - Le module `main.py` connecte les fonctionnalités de génération de carte à une interface interactive pour l'utilisateur.

---

## Bonnes Pratiques de Développement

1. **Règles de Nommage :**

   - Variables : minuscules avec underscores (`snake_case`).
   - Classes : CamelCase.
   - Fichiers : minuscules avec underscores.

2. **Commentaires :**

   - Chaque fonction est documentée avec une description claire de ses paramètres et de son rôle.

3. **Modularité :**
   - Le projet est divisé en modules indépendants facilitant la maintenance et l'évolutivité.

---

## Conclusion

Ce document technique constitue une référence complète pour comprendre le fonctionnement interne du projet de génération de cartes 2D. Les sections fournissent des explications détaillées sur chaque module, leur rôle, et leurs interactions.
