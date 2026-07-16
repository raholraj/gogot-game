# Runner Mode Main Scene
extends Node2D

var player: Node2D
var enemies = []
var math_gates = []
var projectiles = []

var wave = 1
var distance_traveled = 0
var enemies_killed = 0
var spawn_timer = 0
var spawn_rate = 1.0  # seconds
var player_data = {}

var collision_system: Node

func _ready():
	collision_system = Node.new()
	initialize_runner()

# Initialize runner mode
func initialize_runner():
	# Create player
	var player_scene = preload("res://scenes/runner_mode/player.tscn")
	player = player_scene.instantiate()
	player.position = Vector2(Constants.LANE_WIDTH * 1.5, get_viewport_rect().size.y - 150)
	add_child(player)

func set_player_data(data: Dictionary):
	player_data = data.duplicate()

func _process(delta):
	if not player_data:
		return

	# Move player forward
	player.position.y -= Constants.RUNNER_SPEED * delta
	distance_traveled += Constants.RUNNER_SPEED * delta

	# Spawn enemies
	spawn_timer += delta
	if spawn_timer >= spawn_rate:
		spawn_wave()
		spawn_timer = 0.0

	# Update enemies
	for enemy in enemies:
		enemy.position.y += Constants.ENEMY_SPEED * delta

		# Check collision with player
		if player.get_rect().overlaps_area(enemy.get_rect()):
			player_data["squad_size"] -= 20
			enemy.queue_free()
			enemies.erase(enemy)

		# Remove if off screen
		if enemy.position.y > get_viewport_rect().size.y:
			enemy.queue_free()
			enemies.erase(enemy)
			enemies_killed += 1

	# Update math gates
	for gate in math_gates:
		gate.position.y += Constants.RUNNER_SPEED * 0.5 * delta

		# Check collision with player
		if player.get_rect().overlaps_area(gate.get_rect()):
			apply_gate_effect(gate)
			gate.queue_free()
			math_gates.erase(gate)

		# Remove if off screen
		if gate.position.y > get_viewport_rect().size.y:
			gate.queue_free()
			math_gates.erase(gate)

	# Update projectiles
	for projectile in projectiles:
		projectile.position.y -= 600 * delta

		var hit = false
		for enemy in enemies:
			if projectile.get_rect().overlaps_area(enemy.get_rect()):
				enemy.health -= player_data["attack"]
				if enemy.health <= 0:
					enemy.queue_free()
					enemies.erase(enemy)
					enemies_killed += 1
					player_data["gold"] += 10
				projectile.queue_free()
				projectiles.erase(projectile)
				hit = true
				break

		if not hit and projectile.position.y < 0:
			projectile.queue_free()
			projectiles.erase(projectile)

	# Auto-fire
	if randf() < 0.3 * delta:
		auto_fire()

	# Update UI
	update_hud()

	# Check game over
	if player_data["squad_size"] <= 0:
		game_over()

func apply_gate_effect(gate: Node):
	if gate.gate_type == "blue":
		player_data["squad_size"] = int(player_data["squad_size"] * Constants.BLUE_GATE_MULTIPLIER) + Constants.BLUE_GATE_BONUS
		player_data["gold"] += 50
	elif gate.gate_type == "red":
		player_data["squad_size"] = max(0, int(player_data["squad_size"] / Constants.RED_GATE_DIVISOR) + Constants.RED_GATE_PENALTY)

func spawn_wave():
	# Spawn enemy
	if randf() < 0.7:
		var lane = randi() % Constants.NUM_LANES
		var enemy_type = [Constants.ENEMY_ZOMBIE_SMALL, Constants.ENEMY_ZOMBIE_BIG].pick_random()
		var enemy_scene = preload("res://scenes/runner_mode/enemy.tscn")
		var enemy = enemy_scene.instantiate()
		enemy.enemy_type = enemy_type
		enemy.position = Vector2((lane + 0.5) * Constants.LANE_WIDTH, -100)
		add_child(enemy)
		enemies.append(enemy)

	# Spawn math gate
	if randf() < 0.3:
		var lane = randi() % Constants.NUM_LANES
		var gate_type = ["blue", "red"].pick_random()
		var gate_scene = preload("res://scenes/runner_mode/math_gate.tscn")
		var gate = gate_scene.instantiate()
		gate.gate_type = gate_type
		gate.position = Vector2((lane + 0.5) * Constants.LANE_WIDTH, -100)
		add_child(gate)
		math_gates.append(gate)

func auto_fire():
	var projectile_scene = preload("res://scenes/runner_mode/projectile.tscn")
	var projectile = projectile_scene.instantiate()
	projectile.position = player.position
	add_child(projectile)
	projectiles.append(projectile)

func update_hud():
	pass

func move_left():
	if player.lane > 0:
		player.move_to_lane(player.lane - 1)

func move_right():
	if player.lane < Constants.NUM_LANES - 1:
		player.move_to_lane(player.lane + 1)

func game_over():
	print("Game Over! Final Squad: ", player_data["squad_size"])

# Input handling
func _input(event: InputEvent):
	if event.is_action_pressed("move_left"):
		move_left()
	elif event.is_action_pressed("move_right"):
		move_right()
	elif event.is_action_pressed("menu"):
		get_tree().root.get_child(0).load_main_menu()
