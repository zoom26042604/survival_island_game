# Tâches de Développement - Jeu de Survie

## 📊 État du Projet (Mis à jour le 25/10/2025)

### Systèmes Terminés ✅

- **Player** : Gestion complète des jauges, évolution naturelle, conditions de fin
- **Game** : Contrôleur principal, boucle de jeu, sauvegarde/chargement basique
- **Event** : Système d'événements avec choix, types d'événements variés
- **EventManager** : Gestionnaire d'événements aléatoires, probabilités configurables
- **Actions** : Système d'actions joueur (fish, find_water, sleep) avec ActionManager

### Couverture de Tests 🧪

- **Player** : 9 tests unitaires (100% coverage)
- **Game** : 8 tests unitaires (fonctionnalités principales)
- **Event** : 6 tests unitaires (effets et choix)
- **EventManager** : 5 tests unitaires (triggers et probabilités)
- **Actions** : 3 tests unitaires (fish, find_water, sleep actions)

### Prochaines Étapes 🎯

1. **ConsoleUI** - Interface utilisateur en console
2. **SaveManager** - Gestionnaire de sauvegarde avancé  
3. **Intégration finale** - main.py et gameplay complet
4. **Polish & Testing** - Tests d'intégration et finitions

---

## Développement des Classes

### Classe Player ✅ TERMINÉE

- [x] Créer la classe Player avec attributs (faim, soif, énergie, jours_survécus)
- [x] Méthode d'initialisation avec valeurs par défaut
- [x] Méthode update_gauges() pour modifier les jauges
- [x] Méthode natural_evolution() pour l'évolution quotidienne
- [x] Méthode check_game_over() pour vérifier si le joueur est mort
- [x] Méthode get_status() pour retourner l'état du joueur
- [x] Validation des limites des jauges (0-100)
- [x] Tests unitaires complets (9 tests)
- [x] Script de démonstration fonctionnel

### Classe Game ✅ TERMINÉE

- [x] Créer la classe Game comme contrôleur principal
- [x] Méthode start_new_game() pour démarrer une partie
- [x] Méthode load_game() pour charger une sauvegarde
- [x] Méthode game_loop() - boucle principale du jeu
- [x] Méthode process_day() pour traiter une journée
- [x] Méthode check_victory() (30 jours = victoire)
- [x] Méthode end_game() pour terminer la partie
- [x] Tests unitaires complets (8 tests)
- [x] Intégration avec la classe Player

### Classe Event ✅ TERMINÉE

- [x] Créer la classe Event pour les événements aléatoires
- [x] Événement "Pluie" (20% chance) : -15 soif
- [x] Événement "Animal" (15% chance) : choix fuir/chasser
- [x] Événement "Ressource" (25% chance) : -10 faim ou -10 soif
- [x] Méthode apply_effects() pour appliquer les effets
- [x] Système de choix interactifs avec apply_choice()
- [x] Énumérations EventType et EventOutcome
- [x] Tests unitaires complets (6 tests)

### Classe EventManager ✅ TERMINÉE

- [x] Créer la classe EventManager
- [x] Méthode trigger_daily_event() pour événements quotidiens
- [x] Méthode trigger_exploration_event() pour l'action explorer
- [x] Gestion des probabilités d'événements
- [x] Bibliothèque d'événements prédéfinis (events_library.py)
- [x] Système de choix automatique pour les tests
- [x] Tests unitaires complets (5 tests)
- [x] Intégration complète avec Player et Event

### Classe Action ✅ TERMINÉE

- [x] Créer la classe Action pour les actions du joueur
- [x] Action "Pêcher" : -20 hunger, -15 energy (execute_fish_action)
- [x] Action "Chercher eau" : -15 thirst, -10 energy (execute_find_water_action)
- [x] Action "Dormir" : +30 energy, +10 hunger, +5 thirst (execute_sleep_action)
- [x] Méthode execute() pour exécuter l'action
- [x] Méthode can_execute() pour vérifier si possible
- [x] Tests unitaires complets (3 tests)
- [x] Intégration avec système Player

### Classe ActionManager ✅ TERMINÉE

- [x] Créer la classe ActionManager
- [x] Implémenter actions disponibles (fish, find_water, sleep)
- [x] Méthodes execute_*_action() pour chaque action
- [x] Architecture simple et fonctionnelle
- [x] Tests unitaires avec MockPlayer

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

### Structure des fichiers ✅ LARGEMENT TERMINÉE

- [x] Créer le dossier src/
- [x] Créer le dossier src/models/ (Player, Event terminés)
- [x] Créer le dossier src/controllers/ (Game, EventManager terminés)
- [ ] Créer le dossier src/views/ (ConsoleUI)
- [ ] Créer le dossier src/utils/ (SaveManager)
- [ ] Créer le dossier data/ pour les sauvegardes
- [x] Créer le dossier tests/ (tests pour Player, Game, EventManager)
- [ ] Fichier main.py à la racine
- [x] Ajouter les fichiers **init**.py
- [x] Scripts de démonstration pour chaque système

## Intégration et Tests

### Tests ✅ LARGEMENT TERMINÉS

- [x] Tests unitaires pour Player (9 tests)
- [x] Tests unitaires pour Game (8 tests)
- [x] Tests unitaires pour Event (6 tests)
- [x] Tests unitaires pour EventManager (5 tests)
- [ ] Tests d'intégration du gameplay complet
- [x] Tests des conditions de fin (game over, victoire)
- [ ] Tests du système de sauvegarde/chargement
- [ ] Tests de l'interface utilisateur

### Conditions de fin ✅ TERMINÉES

- [x] Game over si faim ≥ 100
- [x] Game over si soif ≥ 100
- [x] Game over si énergie ≤ 0
- [x] Victoire après 30 jours de survie
- [x] Calcul et affichage du score final

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
