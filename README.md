# GOGOT GAME - Complete Game Project

## Game Overview
Gogot is a hybrid casual game featuring:
- **Runner Mode (Frontline Breakthrough)**: Auto-running with lane changing and math gates
- **Base Building Mode**: Resource management, building upgrades, fog clearing
- **Combat System**: Auto-battle with squad management

## Project Structure
```
gogot-game/
├── main.py                 # Main game entry point
├── config.py               # Game configuration and constants
├── utils.py                # Utility functions
├── assets/
│   ├── sprites/            # Character and enemy sprites
│   ├── sounds/             # Audio files
│   └── fonts/              # Font files
├── game/
│   ├── __init__.py
│   ├── game.py             # Main game class
│   ├── state_manager.py    # Game state management
│   └── modes/
│       ├── runner_mode.py  # Runner/Frontline mode
│       └── base_mode.py    # Base building mode
├── entities/
│   ├── __init__.py
│   ├── player.py           # Player character
│   ├── enemy.py            # Enemy entities
│   ├── hero.py             # Hero characters
│   └── building.py         # Base buildings
├── systems/
│   ├── __init__.py
│   ├── collision.py        # Collision detection
│   ├── resource.py         # Resource management
│   ├── combat.py           # Combat system
│   └── ui.py               # UI rendering
└── requirements.txt        # Dependencies
```

## Installation & Running

### Requirements
- Python 3.8+
- Pygame

### Setup
```bash
pip install -r requirements.txt
python main.py
```

## Controls

### Runner Mode (Phone/Tablet)
- **Left Swipe / A Key**: Move left lane
- **Right Swipe / D Key**: Move right lane
- **Auto-Fire**: Automatic shooting

### Base Mode
- **Click/Tap**: Select buildings or buttons
- **Drag**: Pan the map
- **Upgrade/Build**: Tap building then confirm

## Game Features

### Runner Mode
- Auto-running character
- 3-lane system with enemies
- Blue gates (+10, x2 multiplier)
- Red gates (-20, ÷2 multiplier)
- Squad size management
- Boss battles

### Base Mode
- Headquarters (resource generation)
- Barracks (troop training)
- Tavern (hero recruitment)
- Defenses against fog
- Resource management (Gold, Iron, Diamonds)
- Building upgrades and repairs

### Combat System
- Character stats (HP, Attack, Defense)
- Auto-battle mechanics
- Squad multiplier system
- Loot and rewards

## Game Logic

### Math Gates
- **Blue Gates**: Multiply squad by 2 (bonus +10)
- **Red Gates**: Divide squad by 2 (penalty -20)
- **Collision with Enemies**: -20 damage
- **Game Over**: When squad size reaches 0

### Resource System
- **Gold**: Currency for upgrades
- **Iron**: Building material
- **Diamonds**: Premium currency
- **Time-based generation** from buildings

### Base Progression
- Clear toxic fog (green mist)
- Expand playable area
- Unlock new buildings
- Increase resource generation

## Asset Requirements
- Character sprites (soldiers, heroes)
- Enemy sprites (zombies, boss)
- Building sprites
- UI elements
- Sound effects and music

## Future Enhancements
- Multiplayer battles
- More hero types and rarities
- Advanced AI for enemies
- Animation system
- Particle effects
- Sound and music integration

## License
MIT License - Feel free to modify and distribute
