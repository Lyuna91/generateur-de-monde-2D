---
edited_seconds: 10
updated_at: 2024-10-12T17:15:44.776+02:00
---
# Cahier de suivi des tests effectués

## 09/10/2024

### Affichage des zones voronoï et les biomes

- **Objectif** : Afficher dans une fenêtre les zones voronoïs liées a des zones
- **Status du test** : Réussi

Note : Le test a réussis, cependant on s'est rendu compte qu'on allait trop vite et qu'on devrait mieux commencer
par assignés les pixels aux zones avant les biomes.

### Afficher les zones voronoï avec les pixels

- **Objectif** : Afficher le voronoi avec des pixels
- **Status du test** : Echouer

Note : Le voronoi ne prenait pas en compte la taille des pixels et affichais seulement les zones. Pour mieux se
rendre compte de ce qu'il se passait mal, on a décider d'afficher les informations des zones et du quadrillage

### Afficher les informations des zones

- **Objectif** : Afficher les informations des zones, ID, couleur, nombre de pixels
- **Status du test** : Réussi

### Afficher le quadrillage

- **Objectif** : Afficher le quadrillage qui permet de voir ou sont censés être positionner les pixels
- **Status du test** : Réussi

Note : Le test a réussi mais on a remarqué qu'effectivement les pixels ne sont pas afficher. On veut donc vérifier
si ils sont bien liés aux zones

### Affichage des informations des pixels

- **Objectif** : Afficher les informations des pixels (ID, ID de la zone à laquelle il appartient, couleur...)
- **Status du test** : Réussi

Note : Les pixels sont bien liés au zone, c'est un problème d'affichage

### Afficher les zones voronoï avec les pixels 2

- **Objectif** : Afficher les zones voronoï avec les pixels correctement
- **Status du test** : Réussi
