# Projet Python – Jeu de survie sur une île

## Objectif
Réaliser en binôme une application en Python en console simulant la survie d'un aventurier bloqué sur une île.

Le joueur devra gérer ses ressources vitales, faire des choix stratégiques et tenter de survivre plusieurs jours.

## Description du jeu

### Jauges du joueur
Votre aventurier possède plusieurs jauges :
- **Faim** (0 = rassasié, 100 = affamé → game over)
- **Soif** (0 = hydraté, 100 = déshydraté → game over)  
- **Énergie** (0 = épuisé → game over)

### Mécaniques de jeu quotidiennes
Chaque jour de survie :
- Les jauges évoluent naturellement
- Des événements aléatoires peuvent se produire :
  - **Pluie** → réduit la soif
  - **Rencontre animale** → fuir ou chasser
  - **Découverte de fruit/ressource** → améliore les jauges

### Actions disponibles
Le joueur choisit une action par jour :
- **Pêcher** → diminue la faim mais consomme de l'énergie
- **Chercher de l'eau** → réduit la soif, consomme de l'énergie
- **Dormir** → remonte l'énergie, mais augmente faim/soif
- **Explorer** → événement aléatoire (parfois bénéfique, parfois dangereux)

### Conditions de fin
La partie se termine si :
- Une jauge atteint une valeur critique
- Le joueur survit un nombre de jours fixé (victoire)

## Spécifications techniques

### Contraintes
- Programme en console (CLI)
- Boucle de jeu avec système de jours et affichage des jauges
- Gestion des jauges dans un objet (classe ou dictionnaire)
- Mise à jour des jauges et des événements à chaque tour
- Conditions de game over ou de victoire
- Sauvegarde/chargement de la partie (fichier texte ou JSON)

### Livrables
- Un dépôt Git commun au binôme :
  - Code Python
  - Fichier README.md avec :
    - Présentation du projet
    - Règles du jeu  
    - Instructions pour lancer le programme
- Un jeu fonctionnel et une courte démo

## Technologies utilisées
- **Langage** : Python 3.x
- **Interface** : Console/CLI
- **Sauvegarde** : JSON
- **Gestion de version** : Git/GitHub