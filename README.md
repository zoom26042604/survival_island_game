# 🏝️ Jeu de Survie sur une Île

Un jeu de survie en console développé en Python où vous devez gérer les ressources vitales de votre aventurier bloqué sur une île déserte.

## 📋 Description

Votre aventurier s'est échoué sur une île mystérieuse. Votre mission : survivre le plus longtemps possible en gérant vos jauges vitales et en prenant les bonnes décisions. Chaque jour apporte de nouveaux défis et des événements imprévisibles !

### 🎯 Objectif

Survivre **30 jours** pour remporter la victoire, tout en évitant que vos jauges vitales atteignent des niveaux critiques.

## 🎮 Mécaniques de Jeu

### Jauges Vitales

Votre aventurier possède 3 jauges à surveiller :

- **🍖 Faim** (0-100) : 0 = rassasié, 100 = affamé → Game Over
- **💧 Soif** (0-100) : 0 = hydraté, 100 = déshydraté → Game Over  
- **⚡ Énergie** (0-100) : 100 = en forme, 0 = épuisé → Game Over

### Actions Quotidiennes

Chaque jour, vous pouvez choisir une action :

| Action | Effet | Coût en énergie |
|--------|-------|-----------------|
| 🎣 **Pêcher** | -20 faim | -15 énergie |
| 🔍 **Chercher de l'eau** | -15 soif | -10 énergie |
| 😴 **Dormir** | +30 énergie | +10 faim, +5 soif |
| 🗺️ **Explorer** | Événement aléatoire | Variable |

### Événements Aléatoires

Des événements peuvent survenir chaque jour :

- **🌧️ Pluie** (20% de chance) : -15 soif
- **🐺 Rencontre animale** (15% de chance) : Choix entre fuir ou chasser
- **🍇 Découverte de ressource** (25% de chance) : -10 faim ou -10 soif

### Évolution Naturelle

Chaque jour, vos jauges évoluent naturellement :

- Faim : +5
- Soif : +3  
- Énergie : -10

## 🏆 Conditions de Fin

### 💀 Game Over

- Faim ≥ 100
- Soif ≥ 100  
- Énergie ≤ 0

### 🎉 Victoire

- Survivre 30 jours complets

## 🚀 Installation et Lancement

### Prérequis

- Python 3.7 ou supérieur
- Aucune dépendance externe requise

### Installation

```bash
# Cloner le repository
git clone https://github.com/zoom26042604/survival_island_game.git
cd survival_island_game

# Lancer le jeu
python main.py
```

### Lancement rapide

```bash
python main.py
```

## 📁 Structure du Projet

```text
survival_island_game/
├── src/
│   ├── models/
│   │   ├── player.py          # Classe Player avec jauges vitales
│   │   ├── event.py           # Classe Event pour événements
│   │   └── action.py          # Classe Action pour actions
│   ├── controllers/
│   │   ├── game.py            # Contrôleur principal du jeu
│   │   ├── event_manager.py   # Gestionnaire d'événements
│   │   └── action_manager.py  # Gestionnaire d'actions
│   ├── views/
│   │   └── console_ui.py      # Interface utilisateur console
│   ├── utils/
│   │   └── save_manager.py    # Système de sauvegarde
│   └── __init__.py
├── data/
│   └── saves/                 # Fichiers de sauvegarde
├── tests/
│   ├── test_player.py
│   ├── test_game.py
│   └── ...
├── docs/
│   ├── SUJET.md              # Sujet détaillé du projet
│   ├── TACHES.md             # Liste des tâches
│   └── class_diagram.json    # Diagramme de classes
├── main.py                   # Point d'entrée du jeu
├── README.md                 # Ce fichier
└── LICENSE
```

## 🎯 Fonctionnalités

### ✅ Implémentées

- [ ] Système de jauges vitales
- [ ] Actions du joueur (pêcher, eau, dormir, explorer)
- [ ] Événements aléatoires
- [ ] Interface console avec barres de progression
- [ ] Système de sauvegarde/chargement JSON
- [ ] Boucle de jeu complète
- [ ] Conditions de fin (game over/victoire)

### 🔮 Fonctionnalités futures

- [ ] Système d'inventaire
- [ ] Craft d'objets
- [ ] Différents biomes sur l'île
- [ ] Saisons et météo
- [ ] Système de compétences

## 🎮 Guide de Jeu

### Démarrage

1. Lancez le jeu avec `python main.py`
2. Choisissez "Nouvelle partie" ou "Charger partie"
3. Entrez le nom de votre aventurier

### Interface

```text
=== Jour 1 ===
Aventurier: Alex

Faim:    30/100
Soif:    20/100  
Énergie: 80/100

Que voulez-vous faire ?
1. 🎣 Pêcher
2. 💧 Chercher de l'eau  
3. 😴 Dormir
4. 🗺️ Explorer
5. 💾 Sauvegarder et quitter
```

### Conseils de Survie

- 🎯 **Équilibrez** vos actions selon vos jauges
- 💤 **Dormez** régulièrement pour récupérer de l'énergie
- 🎲 **Explorez** pour des événements bonus (mais attention aux risques !)
- 💾 **Sauvegardez** souvent votre progression
- 📊 **Surveillez** l'évolution naturelle de vos jauges

## 🧪 Tests

```bash
# Lancer tous les tests
python -m pytest tests/

# Tests avec couverture
python -m pytest tests/ --cov=src/

# Tests d'une classe spécifique
python -m pytest tests/test_player.py -v
```

## 🤝 Contribution

Ce projet est développé dans le cadre d'un projet étudiant.

### Développeurs

- **Étudiant 1** : Système de joueur, événements, interface
- **Étudiant 2** : Boucle de jeu, sauvegarde, actions

### Workflow Git

- `main` : Version stable de production
- `dev` : Branche de développement
- `feature/*` : Branches pour chaque fonctionnalité

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🏷️ Version

**Version actuelle** : 1.0.0-dev

## 📞 Support

En cas de problème :

1. Vérifiez que Python 3.7+ est installé
2. Consultez la documentation dans `/docs`
3. Créez une issue sur le repository GitHub

---

🎮 **Bonne survie sur l'île !** 🏝️
