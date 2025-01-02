---
updated_at: 2024-10-12T17:15:10.623+02:00
edited_seconds: 10
---

# Débrief Réunion 02/01

- Compte rendu + présentation (Jade) + doc technique + manuel
- Correction au niveau de la suppression (route) + Jette un oeil à tout le code + mettre à jour la doc technique
- Faire l'exécutable lundi 06 janvier (Carlos) + Adaptation Ecran + Readme comment utiliser le logiciel

Dernière réunion lundi 6 janvier au soir : lecture complète ensemble de la doc technique + lecture complète du manuel + préparation de la présentation. Cloture avec génération de l'exécutable

# Update Jade 02/01/2024

Petit Commit avec amélioration de l'interface
Je tente de régler cetet affaire de pleins écran

# Up to the date Carlos 28/12

J'ai fait un peu bcp de choses, les sliders pour les lacs et les rivieres, meme si j'ai remarque que les rivieres peuvent parfois se regenerer sur une autre rivieres c'est chelou. Ensuite j'ai arranger l'interfaces pour que tout s'affiche et j'ai ajouter une ligne dans city pour eviter que les villes spawn sur des Lacs.

# Update Réunion 27/12

#### Kifékoi

Carlos : Ajout des curseurs pour les rivières et les lacs deadline lundi/mardi
Yuna : Supprimer à l'unité
Jade : Amélioration de l'interface (bouton / plein écran)

A faire pour le 2 janvier

#### Késeki restera à faire

- Compte rendu
- Présentation
- Exécutable
- Documentation du code
- Documentation technique

# Update Carlos 23/12

Le slider est operationnel et les riviere sont placé sur les pays.
En bonus j'ai trouvé la methode pour transformer notre projet en executable avec toute nos dépendances, il ne reste plus qu'a attendre la version Finale du projet.

# Update Jade 21/12

On peut changer le nom des villes et des pays maintenant ^^ Je vois pour faire la suppression à l'unité plus tard :)

# Update Réunion 20/12

### Trucs qui restent à faire :

- MAJ LAC
- Curseur
- Bonus infrastructure
- Corriger Pangée
- Supprimer à l'unité
- Modification des noms des villes et pays
- Placer rivière au dessus de coloration des pays pour l'affichage en vue pays
- Bonus : faire un executable

Yuna : MAJ lac + Bonus infrastructure + Corigée Pangée
Carlos : Curseur + placer rivière au dessus de pays + Bonus faire exe
Jade : Supprimer à l'unité + Modif noms villes et pays + Bonus : Amélioration de l'interface

# Update Jade 19/12 .ter

J'ai géré l'affaire des pixels.
Pour le moment il y a une variable globale dans CHAQUE fichier ou c'est nécessaire d'avoir un pixel size. Vous pouvez le retrouver en allant dans l'onglet avec la loupe et en tapant "PIXEL_SIZE =" et la vous aurez asccès à tout ça

ça à l'air de fonctionner à une exception près : les pangées

je peux donc effectuée le changement de taille de pixel sans problème et ça modifie correctement la carte pour tous les modes, mais pour la pangée on se retrouve avec un seul pays, une seule parcelle de terre et je sais pas pourquoi

en vrai YUNA si t'as deux minutes pour regarder vu que c'est toi qui t'ai occupé des pangées je suis chaud parce que j'ai pas trouvé le problème :)

Merci et bonne nuit :)

# Update Jade 19/12 .bis

Vu que les arrêts maladie ça me réussi pas, je suis allée un peu plus loin que prévu dans le projet
Donc maintenant on a aussi l'affichage des noms de pays et de ville qui est possible grâce aux boutons sur l'interface
Je commit ça et je me lance dans la taille des pixels comme prévu

# Update Jade 19/12

J'ai pété un cable et j'ai un peu modifié pleins de trucs
On avait dit notamment qu'on ajoutait un bouton pour afficher ou non les frontières sur la vue biome.
Bah je l'ai fais mais j'ai fais mieux que ça !
Maintenant y'a deux vue : vue biome et vue frontière
Et par dessus LES DEUX VUES, on peut choisir d'afficher les frontières, les villes, les routes :)

Comme ça c'est mieux et on est tranquille

# Update Cours 16/12

MAJ des lacs
Affichage frontières dans affichage Biomes
Revoir la taille pixel (potentiellement créer une variable globale)
Reset biome
Créer un affichage des noms de pays et des noms de ville

BONUS :

- Curseur
- Infrastructure (Plage, arbre montagne vague ville)

## Qui fait quoi ?

- Carlos : Bonus Curseur + Reset Biome + Compte rendu
- Yuna : Lac + Bonus infrastructure
- Jade : Affichage des frontières + revoir les pixels

# Update Jade 16/12

J'ai fais l'archipel + j'ai créé les boutons pour selectionner les tailles + modes

# Update Yuna 15/12

J'ai finis le prototype de pangée et corriger le problème avec les biomes.
Maintenant les zones sont générer entièrement sans biomes puis les biomes sont assignés après.
Comme ça, c'est beaucoup plus simple de créer des changements dans la forme des maps (former une grosse ile, plusieurs petites iles) si on a la main sur la façon dont est générer les biomes.

J'ai créer une nouvelle fonction, generate_pangea, qui, en gros, trouve la zone la plus au centre de la map, l'ajoute dans une liste, ajoute à cette liste les zones proches jusqu'à ce que la moitié de la map sois dans cette liste. Une fois la liste prête, assigne des biomes aléatoire à ses zones et le reste de la map devient océan.

J'ai aussi corrigé les routes car je trouve qu'il y en avait trop. Maintenant, chaque ville a au MAXIMUM une route dont elle est l'origine.

Je me souviens pas d'avoir dit ne pas avoir cru en Carlos, mais vu que je suis une meuf chill, je vais pas mentionner que les rivières disparaissent quand on est en affichage mode biome et que j'ai corrigé le fais qu'en mode pays, les zones qui n'avais pas de biome océan ou lac était juste afficher en blanc :D

# Update Carlos 12/12

J'ai fait les checkbox pour les modes d'affichages
je voudrais dedier cette realisation a YUNA qui n'a pas cru en moi. SHE IS A NON-BELIEVER...

# Update Reunion 12/12

## A faire

(j'avais oublié de commit hier sorry)

- archipel - Jade
- pangée - Yuna
- bouton d'affichage - Carlos
  (régler le problème avec les biomes)

# Update Jade 12/12

J'ai ajouté le bouton pour télécharger l'image map, pour l'instant elle se stocke dans le dossier courant et faut juste qu'on reparle des petites fonctionnalités pour voir comme faire le téléchargement.

J'ai pas essayé d'implémenter l'archipel vu que Yuna a dit qu'il y avait un problème -> a voir en réunion

# Update Carlos 11/12

J'ai fais le menu et les bouttons grands moyen petit...
html css js vous me manquez un peu.

# Update Yuna 07/12

J'ai commencé par déplacer toutes les fonctions generate de render.py dans map.py
Le code est plus clair comme ça je trouve et ça décharge pas mal le render.

J'ai fais les modifications nécessaire dans le main aussi car il appelais les fonctions dans render alors qu'elles n'y étaient plus : Tout fonctionne normalement.

J'ai finis les routes, chaque ville en a au moins une.

On va avoir un problème avec la formation de pangée ou d'archipel. De base, il aurait
fallu pouvoir gérer la génération des biomes, mais ils sont directement créer en même temps que les zones ce qui rend impossible d'avoir un controle dessus.
Il faudrait délier les zones et les biomes, de facon qu'ils soient générés indépendament.
On pourrait donc, choisir en fonction de la position des zones, quel biome serait plus approprié.

# DEBRIEF COURS - 04/12

### Il reste à faire :

- des routes pour toute les villes
- Gestion rivieres - Lac
- Transformer un lac en point sur le pays -- donc un Element plutot qu'un biome
- Revoir la taille des pixel

---

Il faut aussi :

- Bouton d'affichage (biome, pays, altitude)
- Taille de la carte (petit, moyen, grand)
- Mode de generation (archipel ,continent, pangee) (3 boutton cliquable)
- Reset (River, road, pays, ville, biome, all)
- Nombre de villes (Cursoeur sous barre)
- Modifier nom de villes et pays
- Télécharger l'image en png

Bonus :

- curseur route
- curseur rivière
- bouton suprresion à l'unité (après avoir selectionné une rivière par exemple)
- faire une plage
- ajouter infrastructure (port, arbre, montagne, vague dans l'eau, etc etc )

### Définitions des éléments

AFFICHAGE
Grand : - Ville (0 et 30) - Rivière (0 et 10) - Zone (100) - Pays (10)
Moyen : - Ville (0 et 20) - Rivière (0 et 6) - Zone (50) - Pays (7)
Petit : - Ville (0 et 10) - Rivière (0 et 3) - Zone (20) - Pays (5)

TYPE
Continent : creer la map
Archipel : créer la fonction
Pangée : créer la fonction

### Qui fait quoi ?

Yuna : Créer_pangée + Ajouter des routes pour chaque ville + compte rendu
Jade : Créer_archipelle + telecharger PNG
Carlos : Bouton_utilisateur + Grand/moyen/petit

# Update Carlos 28/11

J'ai du modifier villes, pour les empeche de spawn sur des lacs, j'ai donc du modifier les pays pour empecher la creation d'un pays avec que des biomes lacs. En parallele j'avance sur l'interface utilisateur, j'ai deux bouttons permets de reinitialiser la map, ou juste les villes (et donc les routes). I feel like Kanye West...

# Update Yuna 28/11

J'ai terminé les routes, enfin du moins entre villes, je ferais le reste demain ou plus tard. Les routes sont désormais segmentées et sont plus aléatoires dans leurs déplacements. Elle ne sont désormais plus afficher quand elles passent sur un biome océan ou lac.

# Debrief réunion 20/11/2024

Attention les routes créent des nouveaux pixels au lieu d'utiliser ceux existants et les placer dans une liste. A modifier.

Gestion des océans : actuellement, la route passe sur le biome océan. Donc on s'est posé la question de comment gérer la route sur le biome. on a trouvé 3 solutions

- Solution 1 : on demande à la route de faire le tour du biome océan et de le contourner.
- Solution 2 : On supprime la liste de pixel de la route qui se trouve sur le biome océan, créant ainsi 2 portions de route qui rejoignent l'océan
- Solution 3 : on implémente les deux

Il a été décidé d'implémenter en priorité la solution 1, et d'essayer d'implémenter la solution 2 en plus si on a le temps.

Il faut ajouter des ramifications entre les routes. Idem pour les rivières. Un peu à la façon d'un réseau véineux ou un arbre.

Pour créer la rivière : on part du biome océan (en vérifiant si il existe des biomes océans) et on crée des rivières à partir du biome océans qui s'étendent sur les alentours.

## REPARTITION DU TRAVAIL

Jade : corriger le problème des listes de pixels de route (point 1) - dealine vendredi soir
Commencer à rédiger le rapport du sprint - deadline mardi soir

Yuna : Implementer la logique des ramifications entre les routes notamment + suppression des routes sur l'eau - deadline dimanche soir

Carlos : Créer les rivières et leur logique + Corriger le print - deadline mardi

# Update Yuna - 19/11 (suite)

J'ai regarder pour que les routes soit afficher en mode pixel et on a un problème, pour l'instant pour créer une route ça créer des nouveaux pixels jaune sur le coup alors qu'on a déjà tout les pixel générer et qu'il faut changer leur couleur.

Je pense qu'il faut en fait, au lieu de passer en paramètre des coordonnées, il faut y passer nos pixel déjà prêt, enfin bref on en discute demain à la réu.

# Update Yuna - 18/11

J'ai vraiment juste ajouter 5 lignes pour que les chemins soit tracés d'une ville à un points aléatoire dans le generate_roads() de jade dans le render. (Merci Rhade)

Pour les routes maintenant il faudrait juste que les routes sois sous forme de pixel et un peu plus d'aléatoire :D

# Update Jade - 16/11

Tracer route est prêt à l'utilisation !

On a un nouvel algorithme : l'ago de Bresenham

Le but de l'algorithme de Bresenham est de tracer une ligne droite la plus proche possible de la trajectoire idéale sur une grille. Comme on ne peut pas dessiner une ligne continue sur une grille de pixels (chaque pixel est une case entière), l'algorithme choisit les pixels qui représentent au mieux cette ligne.

- dans le generate_road_pixel, j'ai ajouté un effet avec des déviations aléatoires pour donner un effet un peu bourré aux chemins. le process c'est ça :

* On calcule des points intermédiaires entre le point de départ et le point d'arrivée.
* On décale aléatoirement et légèrement les points interméditaires de leur origine
* On trace Bresenham

Comme ça on a une impression de vrai chemin ! Parce que j'avais tracé des lignes droites à la base mais c'était vraiment moche.

Donc pour résumé :

- generate_road_pixels génère une route sinueuse avec des points intermédiaires et utilise \_bresenham_line pour connecter ces points.
- \_bresenham_line trace une ligne droite pixel par pixel entre deux points.

Pour tester, j'ai mis un generate_road dans le render qui relie les villes entre elles. Je l'ai copié collé dans la class Road pour voir ce que j'en fais plus tard après que Yuna ait regardé un peu et fait un retour. En tout cas c'est pas la version définitive et ça peut être supprimé pour les test, c'était juste pour voir la gueule des routes :)

VOILAAAA

# Update 13/11/2024 apres la reunion

## Update Carlos

J'ai décidé de faire mon travail dès ce soir et il consistait à :

- finir l'implementation des villes
- effectuer la liaison entre les villes et les pays

J'ai realier mes deux taches :

- la creation des villes
- l'assignation des villes a des pays
- la repartition de villes de maniere pseudo aleatoire en fonction du nombre de pays
- Vu que les villes sont crees en fonction des pays, j'ai pas eu besoin d'établir une regle pour les biome ocean.

# Debrief Reunion 13/11/2024

A ce jour, ce qui a été fiat

- Les frontières sont fonctionnelles
- Les pays sont fonctionnels
- les noms de villes sont quasi fonctionnelles (juste un problème d'import à régler mais sinon ça fonctionnait jusqu'ici)

## A FAIRE

- Création de l'objet ville et placement sur la carte (les noms sont déjà fait)

  - Une ville est un objet indépendant avec son ID, son nom, sa position et le pays dans lequel elle se trouve. En cas de modification par l'utilisateur des frontières du pays, c'est à la ville de recalculer son attribution si besoin.
  - la ville prends en paramètre le pays dans lequel elle doit se placer
  - Un nombre aléatoire de ville entre 0 et x pour déterminer les villes dans les pays
  - Attribution des villes dans tous les pays créés

- Création des routes et placement sur la carte. 2 types de routes

  - Les routes qui relient des villes entre elles
  - Les routes "esthétiques"

  Une route = ID, une liste de pixel, ville_arrive, ville_depart

  CARLOS RAJOUTE TON CODE ICI POUR EXPLIQUER LA DIFF

## REPARTITION DES TACHES

Carlos : s'occupe de la création des villes
Yuna : genere_route (pas entre deux villes)
Jade : tracer route + generate_route_entre_deux_villes

- Jade : Tracer Route - Samedi Soir
- Carlos : Création Ville + Generate Ville - Dimanche soir
- Jade : generate_route_entre_deux_villes - Mercredi
- Yuna : genere_route - Mercredi

# 12/11/2024

Le retour du cahier de suivi !!!! je l'ai réimplémenté à l'envers comme je vous avez expliqué la dernière fois. Donc la première entrée est en réalité la dernière entrée faite dans le cahier !

Mise à jours et implémentation correcte des pays :

- Les pays regroupent plusieurs zones
- les pays peuvent actuellement posséder entre 1 et 5 zones
- les pays ne peuvent pas posséder de zones océans

Dans le test on peut actuellement lire :

- le pays ID
- le pays NOM (avec l'algo de Carlos qui est incroyable merci)
- Le nombre de zone
  - et par zone : ID, Seed, Biome

Je remets la documentation technique quand j'aurai un peu plus de temps <3

---

# Update Yuna 12/11/2024

J'ai mis en place les frontières, c'est dans country
get_border_pixels, qui calcule les bordures à chaque création de pays et qui créer une liste de pixels. La liste est ensuite afficher après les pays dans display_pixels :D

Note pour pas oublier:

- pitié utilisez les fonctions repr si vous voulez afficher un ou plusieurs objets (c'est fait pour ça)
- Avoir une variable pour stocker la taille des pixels sur l'écran et pas avoir a la retaper partout, pour le zoom ce sera plus simple après

# Debrief Reunion 08/11/2024

Pour le 13 Novembre 2024 :
Jade devras avoir finis l'implémentation des pays avant le 9 novembre à 23h59.
Yuna devras avoir finis l'implementation des frontieres avant le 13 à 18h
Carlos devra commencer l'implémentation des villes et avoir une idée claire de la manières dont les villes interagissent avec les pays.

---

# Update Yuna 05/11/2024

Yuna a tenté de faire son travail mais le code créé par Jade était visiblement cassé.
Impossible d'aller plus loin sans en avoir discuté ensemble donc attente de la prochaine réunion

---

# Update Carlos 03/11/2024

Carlos a fait son travail (générateur de nom)

---

# Debrief Réunion 30/10/2024

Le format ipnyb est illisible pour les autres via GitHub -> Trouver une solution

Ajouter la fonction de génération de nom aléatoire d'un pays

Faire fonction : Ajouter zone a pays + pays plus grand + pas pays sur océean

frontières : tracer ligne noire sur l'extérieur d'un pays

Une fronyière : modifier la structure des pays pour inclure dans l'objet pays, l'objet frontière. Ce sera plus simple pour redéfinir une frontitière en cas d'agrandissement de zone ou de modifications

## Programme prochaine semaine

Finir les pays
Générateur de nom de pays
Créer les frontières et les inclure dans le pays
Cloturer le problème de fichier

## Organisation

Jade : Terminer les pays + Problème de fichier (vendredi - soir)
Carlos : Générateur de nom (inclure le fichier test.py dans le country.py) (samedi - soir)
Yuna : Frontière et inclure le pays (dimanche - lundi)

---

# Update Jade 30/10/2024

J'ai refais le cahier de suivi ici en ipynb comme ce que l'ont fait en Proba. C'est plus lisible et ça nous permettra d'inserer des bout de code si on en a besoin. On réléchira ce soir en réunion si on étends ce type de fichier à d'autres suivi/documentation qu'on a (ça peut être pertinent pour la doc technique notamment). J'ai aussi mis le cahier dans le sens inverse d'écriture, comme ça les news récente sont en haut du document. Pus besoin de scroll pour avoir les infos, c'est directement sous vos yeux à l'ouverture du doc. Donc quand vous ajoutez une update, vous la faites en haut du document
🙂

Finalement j'ai fais aussi la documentation technique en ipynb. Y'a surement moyen de le rendre plus lisible et joli que ce que j'ai fais la mais c'est un bon début. L'explication de Voronoi a également été ajoutée dans la doc.

La fonction generate_pixel doit elle être dans map.py ou dans pixel.py ?

J'ai créé un truc qui fais des pays (quand vous faites le test, les zones blanches sont les zones sans pays / pas assigné à des pays).

Donc ça marche pour l'instant, mais il me reste 2.3 détails que je ferais ce soir avant/apès la réunion
empêcher les pays sur les biomes océans
voir pour faire des pays avec davantages de zones parce que je trouve les pays petits, faut que je regarde ou ça bloque

A suivre ce soir

Si vous voulez essayer :
le nombre de pays sur la carte se règle dans le main.py

---

# 28/10/2024

### Update Carlos :

It was a hard day to be honest. I searched a lot of libraries to generate countries names randomly but they didn't work at all. So I decided to use a manual creation based on list of characters, titles and random library and i think is a really good work.

je parle bien anglais en vrai.

---

# Debrief réunion 23/10

Un pays :

- Un regroupement de zone
- un pays ne peut pas se former sur les océans
- Générateur de nom

Un pays :

- id
- nom
- liste des zones

Important : la création de la fonction create_pays : dedans il faut implémenter la logique de création (à savoir que c'est des regroupement de zone qui sont frontalières.) Faire ça en fonction des graines

## Déroulement de la semaine

- Jade : create_country
- Yuna : Biome en dico
- Carlos : générateur de nom

### Update Yuna :

- J'ai enlevé une fonction en double de la classe biome (get_info_biome)
- J'ai créer la fonction pour créer un dictionnaire de biomes (create_biomes())
- J'ai créer la fonction **repr** pour afficher les infos d'un biome et display_biomes pour afficher un biome
- J'ai retirer le paramètre cls (équivalent à self) pour le remplacer par self car c'est ce qui avait été ajouté jusque là.
- La fonction get_biome_info permet de récupérer les infos d'un biome sous forme de dico, le **repr** permet de les afficher seulement.

- En plus j'ai fais la mise à jour de tout les fichiers en fonction de la doc technique, plus ajouter un **repr** pour toute les classes.

---

# Cours 18/10

## Trouver ce qu'on fait pendant le cours

- On revoit les bugs et problèmes rencontré actuellement (15min)
- On revoit classe par classe les différents éléments à implémenter (45min)
- On détermine 'ordre dans lequel on développe nos éléments (30min) + déterminer calendrier de la semaine à venir

## Ordre de développement du sprint (Du 18 octobre au 26 novembre)

- Revoir les biomes (deadline mercredi 23 octobre )
- Devélopper d'abord les pays (deadline mercredi 30 octobre ) - Un pays se forme en selectionnant une liste de zone
- Développer les frontières (deadline mercredi 6 novembre) - Représente l'extérieur du pays créé en sélectionnant la liste de zone
- Développer les villes (deadline mercredi 13 novembre ) - les villes sont des points à placer aléatoirement - Tous les biomes sauf les lacs et océans
- Développer les routes (deadline mercredi 20 novembre)
- Développer les rivières (deadline mardi 26 novembre)

## On se mets d'accord sur l'orga de la semaine qui arrive

- Changer les biomes pour les passer en dictionnaire
  biome = { "Desert" : Biome (.......), }

## Carlos s'occupe d'envoyer le sprint ce soir (18/10)

Répartition des points :

- Yuna : 40
- Carlos : 30
- Jade : 30

---

# Update Carlos 16/10/2024 - apres la reunion

J'ai pris de l'avance, j'ai lier le biome et les zones.

Mais lors de la réalisation de mon plan tres original, j'ai remarqué que nous avons fait une petite erreur
lors de la creation des biome. On assigne le meme ID à tous les biomes du meme type. Je pense que nous devrons creer un ID perso a chaque zone meme si elle on un ID de zone Commun.

A reflechir.

---

# Debrief Reunion 16/10

Yuna - Aider Carlos avec pygame et le lancement du programme
Carlos - Lier les biomes avec les zones
Jade - S'occuper du test de la liaison (insérant print - biome dans zone)

---

# Update Carlos 16/10/2024

J'ai réaliser mes tâches notamment la vérification du code en fonction de la doc technique. AU niveau de l'explication j'en ai faite une MAIS je suis pas sûr et j'attends des retours.

---

# Update Yuna 12/10/2024

J'ai rédiger les tests qu'on avait effectué le 8 octobre de la création de l'algorithme voronoï
dans le fichier test_debogage.

---

# COURS 08/10

-> refaire le diagramme de classe avec ce qu'on a vu en cours UML
-> attention sur road et river qui sont identique dans le diagramme de classe

https://www.mathweb.fr/euclide/2024/05/02/diagrammes-de-voronoi-point-de-vue-mathematiques-et-python/

Vérifier la gestion des pixels et des zones ensemble : on suspecte que les zones soient créées et affichées mais les pixels n'ont pas l'information de la zone à laquelle ils sont affectés.

## Update Voronoi

-> Algorithme de Voronoi implémantée pendant le cours.

On a actuellement un algorithme qui crée des zones selon Voronoi, dans chacune de ces zones un pixel est attribué et chaque pixel recupere en parametre de zone, l'identifiant de sa zone.

Dans un soucis de test et debuggage:

- Nous avons rajouté un point noir qui correspond à la "seed" pour visualiser son emplacement.
- Nous avons attribué une couleur aléatoire aux zones.

## Trucs à faire

- Remplir le fichier de test_debogage avec les tests que l'on a éffectué aujourd'hui.
- Expliquer en détail la fonction "génerer_zone_voronoi" + expliquer l'algorithme en détail dans la documentation technique.
- Vérifier la syntaxe a TETE reposée du code qu'on a fait aujourd'hui (Bien respecter la doc technique)
- Vérifier la hierarchisation, vérifier la localisation des fonctions(les fonctions zones sont bien dans le fichier "Zone")
- Commencer a reflechir à l'implementation des biomes

## Repartition du travail de la semaine

YNZA : remplir le fichier de test debogage (Expliquer tous les tests qui ont pas fonctionnés, les prints inserés et les modifs mis en place)

RHADE : Expliquer Voronoi dans la doc technique

My GLORIOUS KING CARLOS : Vérification du code en fonction de la doc technique et modifs + expliquer l'affichages des pixels et des zones.

TOUS : Réfléchir à l'implémentation des biômes

## A noter

PAS DE REUNION LE MERCREDI 9 OCTOBRE 2024 : car le travail a été effectuer après le cours du 8 la veille.

---

# Update Yuna 06/10/2024

J'ai retirer les dossiers qui contenait qu'un seul fichier

---

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

---

# Update Jade - 05/10/2024

1er point : Quand vous faites une entrée dans le cahier de suivi, faites de la forme suivante pour qu'on soit cohérent svp :

- # Update NOM - DATE - Potentiellement HEURE si c'est pertinent

2e point : Commenter votre code un maximum ! J'ai rajouter dans la doc technique des consignes à suivre sur le dev

3e point : n"hésitez pas à supprimer ce qui n'est plus utile pour éviter de pourir notre dossier. En l'occurence, après avoir refais toutes les classes dans des nouveaux fichiers, le fonction.py aurait pu être supprimé. Je m'en suis chargé

4e point : je me suis rendu compte que j'arrivais pas à lire les fonctions GenerateEmptyRoad (surement ma vue qui me joue des tours, ou alors je suis trop toqué) donc pour éviter de trop fatiguer à décrypter j'ai changé la règle de nomage pour les fonctions pour du generate_empty_road. De toute façon la moitié du projet était dev de cette manière la, on était pas raccord la dessus visiblement. J'ai modifié le map.py qui correspondait à l'ancienne règle de nommage

5e point : J'ai crée les éléments de pixels et de biome principalement. Je peux pas trop toucher au zone pour l'instant vu que c'est un travail à faire avec l'algo de voronoi qui attendra le sprint 2. J'ai créé une fonction de génération de pixel sur une map que @yuna tu pourras utiliser dans la créa de generate_map et generat_empty_map je pense. Hésite pas à regarder et modifier si besoin.

@YunaVu

---

# Update Carlos - 3/10/2024

Gestion de la hiérarchisation + création des fichiers + init Faite
Les modifications ne sont pas definitives...

@JadeVu
@YunaVu

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

---

# Update Carlos - 29/09/2024

On a décidé de tout creer en anglais, donc j'ai mis à jour les fonctions (fonctions.py) avec les derniers modifications du cahier des charges. J'ai aussi mis à jour la documentation technique.

@YunaVu
@JadeVu
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

# Update Jade - 25//09/2024 - 22h

J'ai créé le cahier de suivi, la documentation technique et le doc qui répertorie nos tests pour le debogage
On en reparle en détail vendredi, en attendant pensez à bien mettre vos updates des missions qu'on s'est assigné aujourd'hui

@YunaVu
@CarlosVu

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

---
