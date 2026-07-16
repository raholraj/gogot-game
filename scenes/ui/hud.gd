# HUD - Heads Up Display for Runner Mode
extends CanvasLayer

var player_data = {}

func _ready():
	pass

func set_player_data(data: Dictionary):
	player_data = data

func _process(_delta):
	queue_redraw()

func _draw():
	if not player_data:
		return

	# Squad size
	draw_string(load("res://assets/fonts/default_font.tres"), Vector2(20, 60), "Squad: %d" % player_data["squad_size"], HORIZONTAL_ALIGNMENT_LEFT, -1, 36, Constants.COLOR_WHITE)

	# Resources
	draw_string(load("res://assets/fonts/default_font.tres"), Vector2(20, 120), "Gold: %d | Iron: %d | Diamond: %d" % [player_data["gold"], player_data["iron"], player_data["diamond"]], HORIZONTAL_ALIGNMENT_LEFT, -1, 24, Constants.COLOR_YELLOW)
