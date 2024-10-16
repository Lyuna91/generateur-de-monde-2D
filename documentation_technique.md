---
updated_at: 2024-10-12T17:13:41.768+02:00
---

# Documentation technique

ici c'est un document qui viendra expliqué les différentes fonctions, les différents éléments, les appels de fonctions, le fonctionnement des algorithmes, etc...
C'est complémentaire au commentaire présents dans le code. C'est pour permettre à quiconque souhaite s'intéresser aux détails techniques de notre projet sans lire le code.

Ici on établis et on explique notamment nos règles de développement.

---

# Règles de nommage

NB : on a decide de tout nommer en anglais.

## Dossier

Majuscule au début des mots avec underscore si nécessaire
Ex : Visualisateur_Affichage
Ex : Générateur

## Fichier .py

Ques des minuscules avec underscore
ex : export_type
ex : panel

## Classes

Le nom d'une Classe commence avec une Majuscule et si le nom est composé de plusieurs mots
(pour plus de précision notamment) on mettra une majuscule au debut de chaque nouveaux mots.

Ex: class GenerateurDeCarte, GenerateurCarte ect...

## Variables

Toutes les lettres en minuscules et l'usage de "\_" pour separer les mots
Ex: couleur_pixel, position_pixel ect...

## Fonctions

Toutes les lettres en minuscules et l'usage de "\_" pour separer les mots
Ex: couleur_pixel, position_pixel ect...

# Consignes de dev

## Séparation des parties du code

On sépare les parties d'un fichier de code avec

- ######################### NOM DE LA PARTIE

Ex: ######################### SETTER

## Dev d'une fonction

On commente toujours l'utilité de la fonction
Ex : def generer_pixels(largeur, hauteur, taille_pixel, color=(200, 200, 200)):
"""
Génère automatiquement une grille de pixels pour remplir une fenêtre.

        :param largeur: Largeur de la fenêtre en pixels
        :param hauteur: Hauteur de la fenêtre en pixels
        :param taille_pixel: Taille de chaque pixel (par exemple 10x10)
        :param color: Couleur par défaut des pixels (facultatif)
        :return: Liste de pixels générés
        """

On mets :
-> une rapide description de ce que fait la fonction
-> les paramètres
-> le return

ça va être long et fastidieux mais au moins pas besoin de lire le code pour savoir ce que fait la fonction

# Explications

## Pixels, Zones et Affichage

### Pixels --> pixel.py

Définit la classe Pixel, représentant chaque pixel avec des attributs comme position, couleur, altitude et ID de zone. Il inclut des méthodes pour modifier la couleur ou l'élément associé au pixel.

### Zone --> zone.py

La classe Zone utilise des diagrammes de Voronoi pour générer des zones avec des pixels. Chaque zone est définie par un ID, des pixels associés et une couleur, et permet de gérer des zones aléatoires.

### Render --> render.py

Utilise pygame pour afficher les zones et les pixels dans une fenêtre. Les pixels sont dessinés sous forme de rectangles colorés, et la méthode display_window permet de maintenir l'affichage actif.

## Affichage des zones avec Voronoi (de maniere vulgariser, pour la version complete voir la partie de Jade)

Les zones sont générées via Voronoi dans zone.py, ce qui divise l'espace en polygones autour de graines. Les pixels de chaque zone sont ensuite affichés avec leurs couleurs respectives dans render.py, créant des sections visuelles distinctes sur la carte.
