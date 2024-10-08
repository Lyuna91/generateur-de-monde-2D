# Cahier de suivi

Ce document sert de suivi sur l'avancée du projet. On abandonne le projet du Trello, on centralise tout ici pour être tranquile

Du coups on aura :

# Update Carlos

# Update Jade

# Update Yuna

Vous devez faire une update a chaque fois que vous pushez pour expliquer ce que vous avez push
Vous devez également noter quand vous avez vu l'update de quelqu'un d'autre avec @CarlosVu, @YunaVu, @JadeVu
Dès que vous avez push quelque chose, vous le notifiez sur Discord

On aura aussi :

# Débrief Réunion

Je ferais un recap à chaque fin de réunion des missions assignées et des conclusions qui ont été faites

Je crée également un fichier Debogage/Test dans lequel vous notez le moindre test que vous avez fait.

---

# Débrief Réunion 25/09/2024

Récap du cahier des charges : On a regardé en détail le cahier des charges pour établir correctement les futurs sprints du projet.
Etablissement des missions spécifiques par membre pour le sprint 1 :

- Yuna : Création de la base de quadrillage de la map
- Jade : Création des éléments de la map
- Carlos : Création des fonctions et des briefs associés
  Réunion pour ces pushs prévu pour le vendredi 27 septembre pour s'assurer du bon fonctionnement de Github

@JadeVu
@YunaVu
@CarlosVu

---

# Update Jade - 25//09/2024 - 22h

J'ai créé le cahier de suivi, la documentation technique et le doc qui répertorie nos tests pour le debogage
On en reparle en détail vendredi, en attendant pensez à bien mettre vos updates des missions qu'on s'est assigné aujourd'hui

@YunaVu
@CarlosVu

---

# Update Carlos - 26/09/2024

Euhhh JE devais creer le cahier de suivis de base...

Bref, j'ai ajouté fonctions.py dans lequel se trouve les fonctions que l'on va réaliser, avec les classes que l'on va utilisé. Je vous invite a aller tchequer et a ajouter ce que vous voulez.

@JadeVu (Yep sorry pour le cahier de suivi, je l'ai fais pour pouvoir noter le debrief de réunion tout de suite pour pas oublier)
@YunaVu
@CarlosVu

# Update Yuna - 26/09/2024

J'ai d'abord créer un dossier _code_ pour y mettre le code de l'application, j'ai ensuite créer
créer un autre dossier _visualiseur_ à l'intérieur. J'y ai mis une classe fenêtre, pour ouvrir une fenêtre pygame et de quoi afficher un quadrillage pour avoir une meilleure idée de la façon dont les
pixels seront affichés.

@JadeVu
@CarlosVu

---

# Update Carlos - 29/09/2024

On a décidé de tout creer en anglais, donc j'ai mis à jour les fonctions (fonctions.py) avec les derniers modifications du cahier des charges. J'ai aussi mis à jour la documentation technique.

@YunaVu
@JadeVu
@CarlosVu

---

# Débrief Réunion 2/10/2024

Débrief des différents commit sur le projet

### Hierarchisation du projet

Dossiers différents à créer entre les différents packages : en l'occurence Generation et affichage
Fichiers différents à créer entre les classes : en l'occurence, biome, river, road, etc...

### Cahier des charges

Ajouter le cahier des charges (et notamment la partie sur les sprints) en format Markdown

### Missions de la semaine

Création des fichiers et gestion de la hierarchisation
Créer tous les .init dans tous les fichiers ( minima le pack génération )
Création approfondie de la classe pixel pour ensuite créer les fonctions de création de la map AVEC les pixels et en fonction de la taille

### Répartition des tâches

Carlos : Gestion de la hiérarchisation + création des fichiers + init
Deadline : jeudi 03/10/2024 - minuit

Jade : Developpement de la classe pixel + dev des éléments restants
Deadline : Samedi 05/10/2024 - minuit
Prérequis : Carlos doit avoir créé les fichiers

Yuna : Dev de la fonction generateMap et generateEmptyMap
Deadline : Lundi 07/10/2024 - minuit
Prérequis : Jade doit avoir créé les pixels

@JadeVu
@CarlosVu
@YunaVu

# Update Carlos - 3/10/2024

Gestion de la hiérarchisation + création des fichiers + init Faite
Les modifications ne sont pas definitives...

@JadeVu
@YunaVu

---

# Update Jade - 05/10/2024

1er point : Quand vous faites une entrée dans le cahier de suivi, faites de la forme suivante pour qu'on soit cohérent svp :

- # Update NOM - DATE - Potentiellement HEURE si c'est pertinent

2e point : Commenter votre code un maximum ! J'ai rajouter dans la doc technique des consignes à suivre sur le dev

3e point : n"hésitez pas à supprimer ce qui n'est plus utile pour éviter de pourir notre dossier. En l'occurence, après avoir refais toutes les classes dans des nouveaux fichiers, le fonction.py aurait pu être supprimé. Je m'en suis chargé

4e point : je me suis rendu compte que j'arrivais pas à lire les fonctions GenerateEmptyRoad (surement ma vue qui me joue des tours, ou alors je suis trop toqué) donc pour éviter de trop fatiguer à décrypter j'ai changé la règle de nomage pour les fonctions pour du generate_empty_road. De toute façon la moitié du projet était dev de cette manière la, on était pas raccord la dessus visiblement. J'ai modifié le map.py qui correspondait à l'ancienne règle de nommage

5e point : J'ai crée les éléments de pixels et de biome principalement. Je peux pas trop toucher au zone pour l'instant vu que c'est un travail à faire avec l'algo de voronoi qui attendra le sprint 2. J'ai créé une fonction de génération de pixel sur une map que @yuna tu pourras utiliser dans la créa de generate_map et generat_empty_map je pense. Hésite pas à regarder et modifier si besoin.

@YunaVu

# Update Yuna - 05/10/2024

Dans le diagramme de classe, j'avais oublier de parler de la fenêtre. J'hésite à la laisser comme ça ou à l'intégrer directement dans
la classe visualisation. Je déplace juste ma classe fenêtre et le main dans le package Visualisateur_Affichage et je laisse comme ça pour l'instant.

J'ai du ajouter le chemin pour aller récupérer la classe Pixel sinon on y a pas accès et j'ai enlever le
chemin vers la classe Zone de la classe Pixel car on en a pas besoin tout de suite.

Depuis la fonction generate_pixel de Jade, je peux récupérer une liste de pixel toute faite dans la fenêtre et
je les affiches sur l'écran de la fenêtre avec la fonction afficher_pixel.

/!\ Je viens de me rendre compte que certains nom de fonction sont en français, je vais changer ça.

J'ai aussi changer ta fonction @jade pour générer les pixels avec une couleur blue qui varient un peu pour qu'on
puisse mieux les voir

# Update Yuna 06/10/2024

J'ai retirer les dossiers qui contenait qu'un seul fichier

# COURS 08/10

-> refaire le diagramme de classe avec ce qu'on a vu en cours UML
-> attention sur road et river qui sont identique dans le diagramme de classe
