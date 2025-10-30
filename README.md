# 🏝️ Survival Island Game

A console-based survival game developed in Python where you must manage your adventurer's vital resources while stranded on a deserted island.

## 📋 Description

Your adventurer has crashed on a mysterious island. Your mission: survive as long as possible by managing your vital gauges and making the right decisions. Each day brings new challenges and unpredictable events!

### 🎯 Objective

Survive **30 days** to achieve victory, while preventing your vital gauges from reaching critical levels.

## 🎮 Game Mechanics

### Vital Gauges

Your adventurer has 3 gauges to monitor:

- **🍖 Hunger** (0-100): 0 = satisfied, 100 = starving → Game Over
- **💧 Thirst** (0-100): 0 = hydrated, 100 = dehydrated → Game Over
- **⚡ Energy** (0-100): 100 = energetic, 0 = exhausted → Game Over

### Daily Actions

Each day, you can choose one action:

| Action | Effect | Energy Cost |
|--------|--------|-------------|
| 🎣 **Fish** | -20 hunger | -15 energy |
| 🔍 **Find water** | -15 thirst | -10 energy |
| 😴 **Sleep** | +30 energy | +10 hunger, +5 thirst |
| 🧭 **Explore** | Triggers random event | -20 energy |

### Random Events

Events can occur randomly during your adventure:

- **☔ Rain** (20% chance): Automatically reduces thirst by 15
- **🐺 Wild Animal** (15% chance): Choose between fleeing (safe) or hunting (risky but rewarding)
- **📦 Resource Found** (25% chance): Discover food or water sources

### Natural Evolution

Each day, your gauges naturally deteriorate:

- **Hunger**: +5 (you get hungrier)
- **Thirst**: +8 (you get thirstier)
- **Energy**: -10 (you get more tired)

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- No external dependencies required

### Setup

1. Clone the repository:

```bash
git clone https://github.com/zoom26042604/survival_island_game.git
cd survival_island_game
```

1. Run the game:

```bash
python main.py
```

## 🎯 How to Play

1. **Start a new game** or load an existing save
2. **Check your status** - monitor your vital gauges
3. **Choose an action** from the available options
4. **Handle random events** if they occur
5. **Survive for 30 days** to win!

### Game Over Conditions

- **Hunger ≥ 100**: You die of starvation
- **Thirst ≥ 100**: You die of dehydration
- **Energy ≤ 0**: You die of exhaustion

### Victory Condition

- **Survive 30 days**: You escape the island and win!

## 🏗️ Project Structure

```text
survival_island_game/
├── README.md                    # Main documentation
├── main.py                      # Game entry point
├── demo_game.py                 # Game demonstration
├── demo_player.py               # Player demonstration
├── docs/                        # Documentation
│   ├── TASKS.md                 # Development tasks
│   ├── REQUIREMENTS.md          # Project requirements
│   └── class_diagram.json       # System architecture
├── src/                         # Source code
│   ├── models/                  # Data models
│   │   ├── player.py            # Player management
│   │   ├── event.py             # Event system
│   │   └── action.py            # Player actions
│   ├── controllers/             # Business logic
│   │   ├── game.py              # Main game controller
│   │   ├── event_manager.py     # Event management
│   │   └── action_manager.py    # Action management
│   └── views/                   # User interface (coming soon)
│       └── console_ui.py        # Console interface
└── tests/                       # Unit tests
    ├── test_player.py           # Player tests
    ├── test_game.py             # Game tests
    ├── test_event_manager.py    # Event tests
    └── test_simple_actions.py   # Action tests
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
cd tests
python -m unittest discover

# Run specific test files
python test_player.py
python test_game.py
python test_event_manager.py
python test_simple_actions.py
```

### Test Coverage

- **Player System**: 9 unit tests
- **Game Controller**: 8 unit tests
- **Event System**: 6 unit tests
- **Event Manager**: 5 unit tests
- **Action System**: 3 unit tests

**Total: 31 unit tests** ✅

## 🎮 Demo Scripts

Try the demonstration scripts to see the systems in action:

```bash
# Demonstrate Player class
python demo_player.py

# Demonstrate Game class
python demo_game.py
```

## 🏆 Features

✅ **Complete gauge management** (hunger, thirst, energy)  
✅ **Random event system** with player choices  
✅ **Multiple player actions** (fish, find water, sleep, explore)  
✅ **Natural gauge evolution** over time  
✅ **Victory/defeat conditions** (30 days survival goal)  
✅ **Advanced save management** (multi-sauvegarde, choix au lancement)  
✅ **Enhanced user interface** (espaces, couleurs, jauges compactes)  
✅ **Save/load functionality** (par joueur)  
✅ **Comprehensive unit testing** (31 tests)  
✅ **Console-based interface**  

## 📚 Documentation

For detailed development information, see:

- [Development Tasks](docs/TASKS.md) - Current progress and TODO list
- [Project Requirements](docs/REQUIREMENTS.md) - Original specifications
- [Class Diagram](docs/class_diagram.json) - System architecture

## 🤝 Contributing

This is a student project. For development guidelines:

1. Follow conventional commit messages
2. Write unit tests for new features
3. Maintain code documentation
4. Use feature branches for development

### Git Workflow

- **main**: Stable production branch
- **dev**: Active development branch  
- **feature/**: Feature branches for new development

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Happy surviving! 🏝️
