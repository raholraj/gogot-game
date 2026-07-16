# Enemy Entity
extends CharacterBody2D

var enemy_type = Constants.ENEMY_ZOMBIE_SMALL
var health = 10
var attack = 5
var width = 25
var height = 35

var color = Constants.COLOR_GREEN

func _ready():
	draw_enemy()

	# Set properties based on type
	match enemy_type:
		Constants.ENEMY_ZOMBIE_SMALL:
			health = 10
			attack = 5
			width = 25
			height = 35
			color = Constants.COLOR_GREEN
		Constants.ENEMY_ZOMBIE_BIG:
			health = 30
			attack = 15
			width = 40
			height = 50
			color = Color(0.59, 0.39, 0)
		Constants.ENEMY_BOSS:
			health = 100
			attack = 30
			width = 60
			height = 80
			color = Constants.COLOR_RED

func draw_enemy():
	var polygon = Polygon2D.new()
	var points = PackedVector2Array([
		Vector2(0, -height/2),
		Vector2(width/2, height/4),
		Vector2(width/2, height/2),
		Vector2(-width/2, height/2),
		Vector2(-width/2, height/4)
	])
	polygon.polygon = points
	polygon.color = color
	add_child(polygon)

func get_rect() -> Area2D:
	var area = Area2D.new()
	var shape = RectangleShape2D.new()
	shape.size = Vector2(width, height)
	var collision = CollisionShape2D.new()
	collision.shape = shape
	area.add_child(collision)
	return area
