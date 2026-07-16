# Building
extends Node2D

var building_type = Constants.BUILDING_HQ
var level = 1
var health = 100
var width = 60
var height = 60

var build_time = 60
var upgrade_cost = {"gold": 100, "iron": 50}
var is_upgrading = false
var upgrade_progress = 0

var color = Constants.COLOR_BLUE

func _ready():
	_update_appearance()

func _process(delta):
	if is_upgrading:
		upgrade_progress += delta
		if upgrade_progress >= build_time:
			level += 1
			is_upgrading = false
			upgrade_progress = 0
			_update_appearance()

func _update_appearance():
	# Remove old children
	for child in get_children():
		child.queue_free()

	# Set color based on type
	match building_type:
		Constants.BUILDING_HQ:
			color = Constants.COLOR_BLUE
		Constants.BUILDING_BARRACKS:
			color = Constants.COLOR_RED
		Constants.BUILDING_TAVERN:
			color = Constants.COLOR_YELLOW
		Constants.BUILDING_MINE:
			color = Color(0.39, 0.39, 0.39)
		Constants.BUILDING_DEFENSE:
			color = Color(0.5, 0, 0.5)

	# Draw building
	var polygon = Polygon2D.new()
	var points = PackedVector2Array([
		Vector2(-width/2, -height/2),
		Vector2(width/2, -height/2),
		Vector2(width/2, height/2),
		Vector2(-width/2, height/2)
	])
	polygon.polygon = points
	polygon.color = color
	add_child(polygon)

	# Draw level text
	var label = Label.new()
	label.text = "L%d" % level
	label.add_theme_font_size_override("font_sizes", 16)
	add_child(label)

func upgrade(player_data: Dictionary) -> bool:
	if player_data["gold"] >= upgrade_cost["gold"] and player_data["iron"] >= upgrade_cost["iron"]:
		player_data["gold"] -= upgrade_cost["gold"]
		player_data["iron"] -= upgrade_cost["iron"]
		is_upgrading = true
		upgrade_progress = 0
		return true
	return false

func get_rect() -> Rect2:
	return Rect2(position - Vector2(width/2, height/2), Vector2(width, height))
