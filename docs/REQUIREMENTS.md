# Python Project – Survival Island Game

## Objective

Create a Python console application simulating the survival of an adventurer stranded on an island.

The player must manage their vital resources, make strategic choices and try to survive for several days.

## Game Description

### Player Gauges

Your adventurer has several gauges:

- **Hunger** (0 = satisfied, 100 = starving → game over)
- **Thirst** (0 = hydrated, 100 = dehydrated → game over)
- **Energy** (0 = exhausted → game over)

### Daily Game Mechanics

Each survival day:

1. **Natural evolution** of gauges (they worsen over time)
2. **Random event** may occur (20% chance)
3. **Player chooses an action** to perform
4. **Check victory/defeat conditions**

### Available Actions

| Action | Effect | Energy Cost |
|--------|--------|-------------|
| 🎣 **Fish** | -20 hunger | -15 energy |
| 🔍 **Find water** | -15 thirst | -10 energy |
| 😴 **Sleep** | +30 energy | +10 hunger, +5 thirst |
| 🧭 **Explore** | Triggers random event | -20 energy |

### Random Events

- **Rain** (20% chance): Automatically reduces thirst by 15
- **Wild animal** (15% chance): Choice between flee (safe) or hunt (risky but rewarding)
- **Resource found** (25% chance): Find food or water source

### Victory/Defeat Conditions

- **Victory**: Survive 30 consecutive days
- **Defeat**: Any gauge reaches critical level
  - Hunger ≥ 100
  - Thirst ≥ 100  
  - Energy ≤ 0

## Technical Requirements

### Classes to Implement

1. **Player**: Gauge management, status, evolution
2. **Game**: Main controller, game loop
3. **Event**: Random events with effects
4. **EventManager**: Event triggering and management
5. **Action**: Player actions
6. **ActionManager**: Action execution management
7. **ConsoleUI**: User interface and display
8. **SaveManager**: Save/load functionality

### Project Structure

```text
survival_island_game/
├── src/
│   ├── models/
│   │   ├── player.py
│   │   ├── event.py
│   │   └── action.py
│   ├── controllers/
│   │   ├── game.py
│   │   ├── event_manager.py
│   │   └── action_manager.py
│   ├── views/
│   │   └── console_ui.py
│   └── utils/
│       └── save_manager.py
├── tests/
├── docs/
├── main.py
└── README.md
```

### Features

- ✅ Console-based interface
- ✅ Player gauge management (hunger, thirst, energy)
- ✅ Daily natural evolution of gauges
- ✅ Random events with player choices
- ✅ Multiple player actions
- ✅ Victory/defeat conditions
- ✅ Save/load game functionality
- ✅ Comprehensive unit testing

## Evaluation Criteria

- **Code quality**: Clean, well-structured, documented code
- **Object-oriented design**: Proper use of classes and methods
- **Functionality**: All game mechanics working correctly
- **Testing**: Unit tests for core functionalities
- **User experience**: Clear interface and smooth gameplay
- **Documentation**: Clear README and code comments

---

## Project Specification

Survival Island Game
