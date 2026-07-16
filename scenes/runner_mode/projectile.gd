# Projectile
extends Node2D

var speed = 600

func _ready():
	draw_projectile()

func _process(delta):
	position.y -= speed * delta

func draw_projectile():
	var rect = Polygon2D.new()
	var points = PackedVector2Array([
		Vector2(-2, -8),
		Vector2(2, -8),
		Vector2(2, 8),
		Vector2(-2, 8)
	])
	rect.polygon = points
	rect.color = Constants.COLOR_YELLOW
	add_child(rect)

func get_rect() -> Area2D:
	var area = Area2D.new()
	var shape = RectangleShape2D.new()
	shape.size = Vector2(5, 15)
	var collision = CollisionShape2D.new()
	collision.shape = shape
	area.add_child(collision)
	return area
