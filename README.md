# Nom du projet : Logiciel d'impresion d'un dessin sur une machine AxiDraw V3 

mindmap : https://simplemindmap.com/mindmap?id=427f35b8-ca57-4905-a7c6-a96b855a4010

## Problematique : 
Comment mettre en place tt les objets pour controler une machine a distance ?

## Introduction : 
Ce programme permet à l'utilisateur de dessiner des formes sur une interface graphique. Il peut envoyer les formes dessinées sur l'ordinateur à une machine AxiDraw par reseau qui elle va dessiner les formes envoyées par l'utilisateur. 

## Aspect théorique : 
Le projet repose sur plusieurs notions théoriques importantes :

-Robot d’écriture : l’AxiDraw est un traceur qui se déplace sur deux axes (X et Y) et permet de dessiner des formes précises à partir de coordonnées.

-Graphisme vectoriel (SVG) : contrairement aux images matricielles, le SVG décrit les formes à l’aide de formules mathématiques (lignes, rectangles, ellipses), ce qui est idéal pour le pilotage d’une machine.

Architecture client / serveur :
-le client est l’application de dessin sur l’ordinateur de l’utilisateur

-le serveur reçoit le fichier SVG et le transmet à la machine AxiDraw.

## Part sociétale :

D’un point de vue sociétal, ce type de logiciel rend accessible la création graphique analogique à un public plus large.

Il permet par exemple :

-de réaliser des affiches personnalisées

-de faire de la calligraphie automatisée

-de produire des dessins précis sans compétences artistiques avancées.

## Partie algorithmique: 

### Pour le réseau :

Pour le client : 
Fonction imprimer_svg_client qui prend en entrée le svg et qui l'envoie au serveur et retourne
le message envoyé

Pour le serveur :

Fonction index instanciant le site web

Fonction recevoir, vérifiant la présence d'un fichier svg afin de l'enregister puis de l'imprimer 
et retourne le message

### Pour le logiciel :
Fonction start_draw qui permet d'enregistrer les coordonnées du premier point de la forme ou le client a cliqué.

Fonction draw qui elle permet de montrer a quoi va resembler la forme en train d'etre dessinée tout cela pendant que le client maintien le clic.

Fonction stop_draw sert quand le clic est relaché a créer la forme faite par le client.

La fonction save_co sert a enregistrer les informations de la forme faite comme ces coordonnées, quelle forme etait faite et son identifiant qui sert a unifié chaques formes crées.

La fonction convertion nous permet d'enregistrer toutes les formes du canvas en code svg.

La fonction imprimer_svg_client sert à envoier le code svg du canvas au serveur qui se chargera de l'imprimer.

Fonction make_button permet de créer un bouton.

## Ressources documentaire :
-GitHub (documentation et exemples de projets similaires)

-Documentation officielle de Tkinter

-Documentation SVG (W3C)

-Documentation de la machine AxiDraw

-Stack Overflow pour utiliser os

-Documentation Cherrypy pour utiliser cherrypy

https://stackoverflow.com/questions/71104397/how-to-convert-svg-string-to-svg-file-using-python

https://www.datacamp.com/fr/tutorial/how-to-check-if-a-file-exists-in-python

https://docs.cherrypy.dev/en/latest/_modules/cherrypy/tutorial/tut09_files.html#FileDemo.download

Source - https://stackoverflow.com/questions/38991286/cherrypy-upload-file

https://www.datacamp.com/fr/tutorial/comprehensive-tutorial-on-using-pathlib-in-python-for-file-system-manipulation

- Utilisation Grok et ChatGPT : n'a pas abouti pour le réseau et le logiciel


## Part projective et part minimal:
-Part minimal:
	- développement d'une application de dessin convertissant en svg
	- développement d'un client et d'un serveur 
-Part projective:
	-Etendre le logiciel a d'autre formes 	
	- imprimer des formes Latex 
	- étendre le logiciel de dessin à des formes géométriques plus complexes
	- étendre la connexion réseau pour internet

## Outils logiciel :
-Tkinter : Bibliotheque qui permet de gerer l'intervace graphique du projet

-AxiDraw : Permet de gerer le moteur de la machine 

- os : pour le traitement des fichiers

- Requests : pour l'envoi en réseau 

Installation de Axidraw : 

code d'installation : 

installer le prebuilt :
``` >> sudo pip install "nom du fichier zip" ``` 

-- dezipper les fichiers --

installer axidraw :
``` >> sudo python setup.py install ``` 

## Matériels nécessaires :
- 2 ordinateurs (client + serveur)

-Une machine AxiDraw V3 


## Méthodologie : 

-Analyse du fonctionnement de l’AxiDraw.

-Création de l’interface graphique de dessin.

-Enregistrement des formes et de leurs coordonnées.

-Conversion du dessin en SVG.

-Mise en place de la communication client / serveur.

-Tests et corrections du programme.


### Voici le fonctionnement en détail :

-Gestion du dessin

-Récupération des coordonnées de la souris.

-Création des formes (ligne, rectangle, ellipse).

-Sauvegarde des coordonnées dans une structure de données (liste de dictionnaires).

-Conversion en SVG

-Transformation des coordonnées du canvas en coordonnées SVG.

-Application d’un facteur d’échelle pour adapter le dessin aux dimensions physiques de l’AxiDraw.

-Communication réseau

-Envoi du code SVG au serveur via une requête HTTP (POST).

-Le serveur se charge ensuite d’interpréter le SVG et de piloter la machine.




## Repartition des tâches au sein du groupe :
Nous avons essayés répartir les tâches équitablement lors de ce projet. Nous avons répartis ce projet en deux. Jean-Batiste c'est occupé de faire la partie reseau qui est donc que l'on peut envoyer notre dessin à distance puis Jules c'est occupé de faire la partie d'intervace graphique plus la transformation en code svg du dessin, cette partie consistait donc de créer un interface graphique où l'on puisse dessiner des formes puis les convertir en code svg pour ensuite les faires dessiner par la machine.
