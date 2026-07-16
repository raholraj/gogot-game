# Game Manager - Main controller for the entire game
extends Node

var state_manager: Node
var current_state = "menu"
var player_data = {}
var game_stats = {}

func _ready():
	state_manager = StateManager.new()
	initialize_player_data()
	initialize_game_stats()
	load_main_menu()

func initialize_player_data():
	player_data = {
		"level": 1,
		"squad_size": Constants.PLAYER_START_SQUAD,
		"gold": Constants.START_GOLD,
		"iron": Constants.START_IRON,
		"diamond": Constants.START_DIAMOND,
		"health": Constants.PLAYER_HEALTH,
		"attack": Constants.PLAYER_ATTACK,
		"defense": Constants.PLAYER_DEFENSE,
		"experience": 0
	}

func initialize_game_stats():
	game_stats = {
		"waves_defeated": 0,
		"enemies_killed": 0,
		"total_damage": 0,
		"accuracy": 100,
		"distance_traveled": 0
	}

func load_main_menu():
	state_manager.change_state(Constants.STATE_MENU)
	current_state = Constants.STATE_MENU
	var menu = preload("res://scenes/ui/main_menu.tscn").instantiate()
	add_child(menu)

func load_runner_mode():
	state_manager.change_state(Constants.STATE_RUNNER)
	current_state = Constants.STATE_RUNNER
	clear_scene()
	var runner = preload("res://scenes/runner_mode/runner_scene.tscn").instantiate()
	runner.set_player_data(player_data)
	add_child(runner)

func load_base_mode():
	state_manager.change_state(Constants.STATE_BASE)
	current_state = Constants.STATE_BASE
	clear_scene()
	var base = preload("res://scenes/base_mode/base_scene.tscn").instantiate()
	base.set_player_data(player_data)
	add_child(base)

func clear_scene():
	for child in get_children():
		if child.name != "AudioStreamPlayer":
			child.queue_free()

func get_player_data():
	return player_data

func update_player_data(key, value):
	if player_data.has(key):
		player_data[key] = value

func get_current_state():
	return current_state
