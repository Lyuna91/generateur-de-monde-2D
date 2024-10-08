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
