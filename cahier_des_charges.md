---
updated_at: 2024-10-12T17:13:41.726+02:00
---
# Cahier des charges - Création d’un logiciel de génération aléatoire de maps (cartes) en 2D

**Version 1 - 29/09/2024**

**Équipe :**

- Yuna Laurency
- Carlos Okinda
- Jade Delebecque

---

## I - Présentation du projet :

### A) Objectifs

Dans le cadre de notre cours de conception logicielle, nous devons développer un générateur de mondes 2D procédural. Ce projet vise à appliquer les principes d'algorithmes de génération aléatoire et d'affichage graphique en utilisant des outils comme Pygame. Le projet est réalisé en équipe avec trois membres : Yuna Laurency, Jade Delebecque, et Carlos Okinda.

### B) Contraintes

#### a) Contraintes techniques

- **Langage** : Python avec la bibliothèque Pygame.
- **Système cible** : Windows.
- **Durée de développement** : 4 mois, divisés en plusieurs sprints.

#### b) Contraintes humaines

- Réunions hebdomadaires sur l’avancée du projet et la répartition des tâches.
- Cahier de suivi mis à jour à chaque push.

---

## II - Description du logiciel

### A) Affichage

La carte sera visualisée en 2D. L’utilisateur pourra zoomer et se déplacer dans la carte pour l'explorer en détail. Chaque biome et région aura une couleur spécifique pour faciliter la différenciation visuelle.

### B) Gameplay/Utilisation

Le logiciel générera une carte de taille variable selon les préférences de l'utilisateur, comprenant différents biomes et éléments naturels :

- **5 Biomes** : Forêts, montagnes, déserts, plaines, lacs.
- **Routes et rivières** : Lignes continues et aléatoires sur le terrain.
- **Frontières** : Entre les différentes régions ou pays générés.
- **Océans** : L'environnement autour de la carte générée (profond ou léger).
- **Villes** : Génération aléatoire de noms de villes, avec possibilité de les renommer.

L'utilisateur pourra personnaliser les cartes via l'interface en définissant :

- La taille de la carte (petite, moyenne, grande).
- Le type de génération (archipel, continent, pangée).
- Le nombre de villes à générer.
- L'existence de routes, rivières et frontières entre les zones.
- Changer l’affichage de la carte selon le mode (pays, biomes, altitude).
- Personnaliser les noms des pays et des régions générées aléatoirement.

### C) Interactions utilisateur

| Fonctionnalité                                   | Interface utilisateur                                                               |
| ------------------------------------------------ | ----------------------------------------------------------------------------------- |
| Taille de la carte (petite, moyenne, grande)     | 3 boutons cliquables avec les 3 options                                             |
| Mode de génération (archipel, continent, pangée) | 3 boutons cliquables avec les 3 options                                             |
| Nombre de villes                                 | Curseur (barre) pour 0-10 (petite carte), 0-20 (carte moyenne), 0-30 (grande carte) |
| Placer et modifier les rivières                  | Modifiable via l’interface utilisateur                                              |
| Placer et modifier les routes                    | Modifiable via l’interface utilisateur                                              |
| Placer et modifier les frontières                | Modifiable via l’interface utilisateur                                              |

---

## III - Déroulement du projet

### Sprint 1 : Du 23 septembre au 8 octobre 2024 (2 semaines)

- **Réunion de groupe** : Mercredi 25 septembre, Mercredi 2 octobre.
- **Tâches** : Création du fichier de code, base de quadrillage de la carte, éléments et fonctions associées.

### Sprint 2 : Du 8 octobre au 18 novembre 2024 (2 semaines)

- **Réunion de groupe** : Mercredi 9 octobre, Mercredi 16 octobre.
- **Tâches** : Création des zones et des biomes, implémentation de l’algorithme de Voronoï pour la création de zones.

### Sprint 3 : Du 18 octobre au 26 novembre 2024 (1 mois)

- **Réunions de groupe** : Mercredi 23 octobre, Mercredi 30 octobre, Mercredi 6 novembre, Mercredi 13 octobre, Mercredi 20 novembre.
- **Tâches** : Implémentation des frontières, routes, rivières et villes.

### Sprint 4 : Du 26 novembre au 04 décembre 2024 (1 semaine)

- **Réunion de groupe** : Mercredi 27 novembre.
- **Tâches** : Création de l’interface utilisateur et liaison avec les éléments existants.

### Sprint 5 : Du 04 décembre au 17 décembre 2024 (2 semaines)

- **Réunions de groupe** : Mercredi 4 décembre, Mercredi 11 décembre, Lundi 16 décembre.
- **Tâches** : Création des fonctions de modifications des éléments (déplacement, modification des villes, frontières, etc.).

### Sprint final : Du 17 décembre au 07 janvier 2025 (3 semaines)

- **Réunions de groupe** : Mercredi 18 décembre, Vendredi 27 décembre, Vendredi 3 janvier.
- **Tâches** : Finaliser l’esthétique du logiciel, corriger les éventuels bugs, préparer la présentation du projet (7 min max).

---

## IV - Développement technique

### 4.1 Package Génération

Ce package contient la logique principale de génération des éléments du monde (biomes, rivières, routes, frontières, villes) et de la carte en général.

- **Classe Map** : Génère une carte, les pixels, biomes, pays, frontières, rivières, routes, et villes.
- **Classe Biome** : Contient les informations relatives aux biomes.
- **Classe River** : Gère la création des rivières.
- **Classe Road** : Gère la création des routes.
- **Classe Border** : Génère les frontières.
- **Classe Zone** : Gère les zones créées par l'algorithme de Voronoi.
- **Classe Pixel** : Gère chaque pixel de la carte.
- **Classe City** : Gère les villes générées aléatoirement.
- **Classe Country** : Gère les pays regroupant plusieurs zones.
- **Enumération biomeName** : Noms des différents biomes.

### 4.2 Package Affichage

Gère tout l'aspect graphique en utilisant Pygame.

- **Classe Visualization** : Gère le zoom et déplacement de la carte.
- **Classe Render** : Gère l’affichage de la carte sur Pygame.
- **Classe Menu** : Interface utilisateur pour la génération et modification de la carte.
- **Classe Panel** : Gère les modifications en direct de la carte.

### 4.3 Gestion des données et algorithmes

- **Algorithme de Bruit de Perlin** : Génère des altitudes réalistes.
- **Division de Voronoi** : Crée les frontières entre les différentes régions ou pays.
- **Gestion des événements Pygame** : Gère les interactions utilisateur.

### 4.4 Documentation

- Commentaires explicites dans le code.
- Documentation utilisateur et technique.
- Cahier de suivi pour l’avancement du projet.

---

## V - Diagramme de Gantt

Un diagramme de Gantt est utilisé pour planifier les tâches à réaliser, réparties sur 16 semaines. Le diagramme sera mis à jour au fur et à mesure de l'avancée du projet.

---
