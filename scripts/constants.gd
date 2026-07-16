# Constants for GOGOT Game

# Screen Settings
const SCREEN_WIDTH = 1080
const SCREEN_HEIGHT = 1920
const FPS = 60

# Game States
const STATE_MENU = "menu"
const STATE_RUNNER = "runner"
const STATE_BASE = "base"
const STATE_BATTLE = "battle"
const STATE_PAUSE = "pause"
const STATE_GAMEOVER = "gameover"

# Colors
const COLOR_WHITE = Color.WHITE
const COLOR_BLACK = Color.BLACK
const COLOR_RED = Color.RED
const COLOR_GREEN = Color.GREEN
const COLOR_BLUE = Color(0, 0.4, 1.0)
const COLOR_YELLOW = Color.YELLOW
const COLOR_GRAY = Color(0.5, 0.5, 0.5)
const COLOR_DARK_GREEN = Color(0.13, 0.55, 0.13)
const COLOR_TOXIC_GREEN = Color(0.2, 0.8, 0.2)

# Runner Mode Settings
const RUNNER_SPEED = 400  # pixels per second
const LANE_WIDTH = SCREEN_WIDTH / 3
const NUM_LANES = 3
const ENEMY_SPEED = 300
const BOSS_HEALTH = 100

# Player Settings
const PLAYER_HEALTH = 100
const PLAYER_ATTACK = 10
const PLAYER_DEFENSE = 5
const PLAYER_START_SQUAD = 10

# Resources
const RESOURCE_GOLD = "gold"
const RESOURCE_IRON = "iron"
const RESOURCE_DIAMOND = "diamond"

const START_GOLD = 500
const START_IRON = 300
const START_DIAMOND = 50

# Building Types
const BUILDING_HQ = "hq"
const BUILDING_BARRACKS = "barracks"
const BUILDING_TAVERN = "tavern"
const BUILDING_DEFENSE = "defense"
const BUILDING_MINE = "mine"
const BUILDING_FARM = "farm"

# Math Gates
const BLUE_GATE_BONUS = 10
const BLUE_GATE_MULTIPLIER = 2
const RED_GATE_PENALTY = -20
const RED_GATE_DIVISOR = 2

# Enemy Types
const ENEMY_ZOMBIE_SMALL = "zombie_small"
const ENEMY_ZOMBIE_BIG = "zombie_big"
const ENEMY_BOSS = "boss"

# Difficulty
const DIFFICULTY_EASY = 1.0
const DIFFICULTY_NORMAL = 1.5
const DIFFICULTY_HARD = 2.0
