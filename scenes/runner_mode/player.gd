# Player Character
extends CharacterBody2D

var lane = 1
var squad_size = Constants.PLAYER_START_SQUAD
var health = Constants.PLAYER_HEALTH
var attack = Constants.PLAYER_ATTACK
var defense = Constants.PLAYER_DEFENSE
var lane_width = Constants.LANE_WIDTH

var target_x = 0
var move_speed = 500

func _ready():
	target_x = get_lane_x(lane)
	draw_player()

func _process(delta):
	# Smooth lane movement
	if abs(position.x - target_x) > 5:
		position.x = lerp(position.x, target_x, delta * 5)

func move_to_lane(new_lane: int):
	lane = clampi(new_lane, 0, Constants.NUM_LANES - 1)
	target_x = get_lane_x(lane)

func get_lane_x(lane_num: int) -> float:
	return (lane_num + 0.5) * lane_width

func draw_player():
	var polygon = Polygon2D.new()
	var points = PackedVector2Array([
		Vector2(0, -20),
		Vector2(15, 10),
		Vector2(0, 25),
		Vector2(-15, 10)
	])
	polygon.polygon = points
	polygon.color = Constants.COLOR_BLUE
	add_child(polygon)

func get_rect() -> Area2D:
	var area = Area2D.new()
	var shape = RectangleShape2D.new()
	shape.size = Vector2(30, 40)
	var collision = CollisionShape2D.new()
	collision.shape = shape
	area.add_child(collision)
	return area
