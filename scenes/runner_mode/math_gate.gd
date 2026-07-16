# Math Gate
extends Node2D

var gate_type = "blue"
var width = 40
var height = 40
var color = Constants.COLOR_BLUE

func _ready():
	draw_gate()

func _process(_delta):
	if gate_type == "blue":
		color = Constants.COLOR_BLUE
	else:
		color = Constants.COLOR_RED

func draw_gate():
	var rect = RectangleShape2D.new()
	rect.size = Vector2(width, height)

	var rect2d = Polygon2D.new()
	var points = PackedVector2Array([
		Vector2(-width/2, -height/2),
		Vector2(width/2, -height/2),
		Vector2(width/2, height/2),
		Vector2(-width/2, height/2)
	])
	rect2d.polygon = points
	rect2d.color = color
	add_child(rect2d)

	# Add text label
	var label = Label.new()
	label.text = "+10" if gate_type == "blue" else "-20"
	label.add_theme_font_size_override("font_sizes", 24)
	add_child(label)

func get_rect() -> Area2D:
	var area = Area2D.new()
	var shape = RectangleShape2D.new()
	shape.size = Vector2(width, height)
	var collision = CollisionShape2D.new()
	collision.shape = shape
	area.add_child(collision)
	return area
