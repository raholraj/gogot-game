# Base Mode Scene
extends Node2D

var buildings = []
var camera_offset = Vector2.ZERO
var selected_building: Node = null
var fog_cleared = 0.0
var player_data = {}

var spawn_rate_gold = 0.1
var spawn_rate_iron = 0.1

func _ready():
	initialize_base()

func initialize_base():
	# Create HQ
	var hq = preload("res://scenes/base_mode/building.tscn").instantiate()
	hq.building_type = Constants.BUILDING_HQ
	hq.position = Vector2(Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 2)
	add_child(hq)
	buildings.append(hq)

	# Create other buildings
	var barracks = preload("res://scenes/base_mode/building.tscn").instantiate()
	barracks.building_type = Constants.BUILDING_BARRACKS
	barracks.position = Vector2(Constants.SCREEN_WIDTH / 2 - 150, Constants.SCREEN_HEIGHT / 2 - 150)
	add_child(barracks)
	buildings.append(barracks)

	var tavern = preload("res://scenes/base_mode/building.tscn").instantiate()
	tavern.building_type = Constants.BUILDING_TAVERN
	tavern.position = Vector2(Constants.SCREEN_WIDTH / 2 + 150, Constants.SCREEN_HEIGHT / 2 - 150)
	add_child(tavern)
	buildings.append(tavern)

func set_player_data(data: Dictionary):
	player_data = data.duplicate()

func _process(delta):
	if not player_data:
		return

	# Generate resources
	player_data["gold"] += spawn_rate_gold * delta
	player_data["iron"] += spawn_rate_iron * delta

	# Clear fog
	if fog_cleared < 100:
		fog_cleared += 0.05 * delta

	update_hud()

func _input(event: InputEvent):
	if event is InputEventMouseButton:
		if event.pressed:
			var mouse_pos = get_local_mouse_position()
			for building in buildings:
				if building.get_rect().has_point(mouse_pos):
					selected_building = building
					break

	elif event is InputEventMouseMotion:
		if event.button_mask & MOUSE_BUTTON_MASK_LEFT:
			camera_offset += -event.relative

	elif event.is_action_pressed("menu"):
		get_tree().root.get_child(0).load_main_menu()

func update_hud():
	pass

func get_player_data():
	return player_data
