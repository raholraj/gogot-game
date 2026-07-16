# GOGOT GAME - Godot Edition

## Complete Game Overview

Gogot is a **hybrid casual game** with:

### 🏃 Runner Mode (Frontline Breakthrough)
- **Auto-running** character moving forward
- **3-lane system** with lane changing (A/D keys)
- **Math gates**: Blue (+10, x2) and Red (-20, ÷2)
- **Enemies**: Zombies and boss battles
- **Squad size management** - starts at 10
- **Auto-fire projectiles** against enemies
- **Progressive waves** with increasing difficulty

### 🏰 Base Building Mode
- **5 Main Buildings**:
  - Headquarters (Gold generation)
  - Barracks (Troop training)
  - Tavern (Hero recruitment - Gacha)
  - Defense Tower (Protection)
  - Mine (Iron generation)

- **Resource Management**:
  - Gold (Currency)
  - Iron (Materials)
  - Diamonds (Premium)

- **Progression System**:
  - Clear toxic fog to expand base
  - Upgrade buildings for better production
  - Visual progression with fog clearing

### ⚔️ Combat System
- **Auto-battle mechanics**
- **Character stats**: HP, Attack, Defense
- **Squad multiplier system**
- **Hero gacha** with rarities (SSR, SR, UR, R)

## Project Structure

```
gogot-game/
├── project.godot
├── assets/
│   ├── sprites/
│   │   ├── player.png
│   │   ├── enemies/
│   │   └── buildings/
│   ├── sounds/
│   └── fonts/
├── scenes/
│   ├── main.tscn
│   ├── runner_mode/
│   │   ├── runner_scene.tscn
│   │   ├── player.tscn
│   │   ├── enemy.tscn
│   │   └── math_gate.tscn
│   ├── base_mode/
│   │   ├── base_scene.tscn
│   │   ├── building.tscn
│   │   └── resource_panel.tscn
│   ├── ui/
│   │   ├── main_menu.tscn
│   │   ├── hud.tscn
│   │   └── pause_menu.tscn
│   └── battle/
│       └── battle_scene.tscn
├── scripts/
│   ├── constants.gd
│   ├── game_manager.gd
│   ├── state_manager.gd
│   ├── runner/
│   │   ├── runner_mode.gd
│   │   ├── player.gd
│   │   ├── enemy.gd
│   │   └── math_gate.gd
│   ├── base/
│   │   ├── base_mode.gd
│   │   ├── building.gd
│   │   └── resource_manager.gd
│   ├── battle/
│   │   └── combat_system.gd
│   ├── ui/
│   │   ├── main_menu.gd
│   │   ├── hud.gd
│   │   └── ui_manager.gd
│   └── systems/
│       ├── collision_system.gd
│       └── hero_gacha.gd
└── README.md
```

## How to Run

1. Open Godot 4.1+
2. Import this project
3. Press F5 or click "Run"

## Controls

### Runner Mode
- **A** / **←** - Move left lane
- **D** / **→** - Move right lane
- **ESC** - Back to menu
- **Auto-fire** - Automatic

### Base Mode
- **Click** - Select building
- **Drag** - Pan camera
- **ESC** - Back to menu
- **U** - Upgrade selected building
- **R** - Repair building

## Features Implemented

✅ State Management System
✅ Runner Mode with lane changing
✅ Math gates with multiplier system
✅ Enemy spawning and waves
✅ Auto-fire projectile system
✅ Base building mode
✅ Resource generation
✅ Building upgrades
✅ Fog clearing progression
✅ UI/HUD system
✅ Main menu
✅ Pause system
✅ Score tracking
✅ Hero gacha system
✅ Combat mechanics
✅ Collision detection

## Future Enhancements

- Sound effects and music
- Animation system
- Particle effects
- More hero types
- Multiplayer battles
- Level system
- Achievements
- Leaderboard

## License

MIT License
