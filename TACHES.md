# Tâches de Développement - Jeu de Survie

## Développement des Classes

### Classe Player

- [ ] Créer la classe Player avec attributs (faim, soif, énergie, jours_survécus)
- [ ] Méthode d'initialisation avec valeurs par défaut
- [ ] Méthode update_gauges() pour modifier les jauges
- [ ] Méthode natural_evolution() pour l'évolution quotidienne
- [ ] Méthode check_game_over() pour vérifier si le joueur est mort
- [ ] Méthode get_status() pour retourner l'état du joueur
- [ ] Validation des limites des jauges (0-100)

### Classe Game

- [ ] Créer la classe Game comme contrôleur principal
- [ ] Méthode start_new_game() pour démarrer une partie
- [ ] Méthode load_game() pour charger une sauvegarde
- [ ] Méthode game_loop() - boucle principale du jeu
- [ ] Méthode process_day() pour traiter une journée
- [ ] Méthode check_victory() (30 jours = victoire)
- [ ] Méthode end_game() pour terminer la partie

### Classe Event

- [ ] Créer la classe Event pour les événements aléatoires
- [ ] Événement "Pluie" (20% chance) : -15 soif
- [ ] Événement "Animal" (15% chance) : choix fuir/chasser
- [ ] Événement "Ressource" (25% chance) : -10 faim ou -10 soif
- [ ] Méthode apply_effects() pour appliquer les effets

### Classe EventManager

- [ ] Créer la classe EventManager
- [ ] Méthode trigger_daily_event() pour événements quotidiens
- [ ] Méthode trigger_exploration_event() pour l'action explorer
- [ ] Gestion des probabilités d'événements

### Classe Action

- [ ] Créer la classe Action pour les actions du joueur
- [ ] Action "Pêcher" : -20 faim, -15 énergie
- [ ] Action "Chercher eau" : -15 soif, -10 énergie
- [ ] Action "Dormir" : +30 énergie, +10 faim, +5 soif
- [ ] Action "Explorer" : déclenche événement aléatoire
- [ ] Méthode execute() pour exécuter l'action
- [ ] Méthode can_execute() pour vérifier si possible

### Classe ActionManager

- [ ] Créer la classe ActionManager
- [ ] Initialiser toutes les actions disponibles
- [ ] Méthode get_available_actions() selon l'état du joueur
- [ ] Méthode execute_action() pour exécuter une action

## Interface Utilisateur

### Classe ConsoleUI

- [ ] Créer la classe ConsoleUI pour l'affichage
- [ ] Méthode display_main_menu() (Nouveau, Charger, Quitter)
- [ ] Méthode display_player_status() avec barres de progression ASCII
- [ ] Méthode display_action_menu() pour choisir une action
- [ ] Méthode display_event() pour afficher les événements
- [ ] Méthode display_game_over() pour l'écran de fin
- [ ] Méthode _draw_gauge_bar() pour les barres ASCII
- [ ] Gestion des entrées utilisateur avec validation

## Système de Sauvegarde

### Classe SaveManager

- [ ] Créer la classe SaveManager
- [ ] Méthode save_game() pour sauvegarder en JSON
- [ ] Méthode load_game() pour charger depuis JSON
- [ ] Méthode list_saves() pour lister les sauvegardes
- [ ] Structure JSON : jauges, jour, nom du joueur
- [ ] Gestion des erreurs (fichier inexistant, JSON invalide)
- [ ] Création automatique du dossier de sauvegarde

## Structure du Projet

### Organisation des fichiers

- [ ] Créer le dossier src/
- [ ] Créer le dossier src/models/ (Player, Event, Action)
- [ ] Créer le dossier src/controllers/ (Game, EventManager, ActionManager)
- [ ] Créer le dossier src/views/ (ConsoleUI)
- [ ] Créer le dossier src/utils/ (SaveManager)
- [ ] Créer le dossier data/ pour les sauvegardes
- [ ] Créer le dossier tests/
- [ ] Fichier main.py à la racine
- [ ] Ajouter les fichiers __init__.py

## Intégration et Tests

### Boucle de jeu principale

- [ ] Intégrer toutes les classes dans Game
- [ ] Séquence complète : Affichage → Événement → Action → Évolution → Nouveau jour
- [ ] Gestion fluide des transitions
- [ ] Sauvegarde automatique chaque jour

### Tests

- [ ] Tests unitaires pour chaque classe
- [ ] Tests d'intégration du gameplay complet
- [ ] Tests des conditions de fin (game over, victoire)
- [ ] Tests du système de sauvegarde/chargement
- [ ] Tests de l'interface utilisateur

### Conditions de fin

- [ ] Game over si faim ≥ 100
- [ ] Game over si soif ≥ 100
- [ ] Game over si énergie ≤ 0
- [ ] Victoire après 30 jours de survie
- [ ] Calcul et affichage du score final

## Documentation et Finalisation

### Documentation

- [ ] README.md avec présentation du projet
- [ ] README.md avec règles du jeu détaillées
- [ ] README.md avec instructions d'installation et lancement
- [ ] Commentaires dans le code
- [ ] Documentation des classes et méthodes

### Démo et présentation

- [ ] Préparer un scénario de démonstration
- [ ] Tester tous les chemins de gameplay
- [ ] Vérifier l'équilibrage des jauges
- [ ] S'assurer de la fluidité du jeu
