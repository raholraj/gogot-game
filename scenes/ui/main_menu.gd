# Main Menu
extends CanvasLayer

func _ready():
	draw_menu()

func _input(event: InputEvent):
	if event is InputEventMouseButton:
		if event.pressed:
			var mouse_pos = get_global_mouse_position()
			# Runner mode button
			if Rect2(350, 300, 380, 100).has_point(mouse_pos):
				get_tree().root.get_child(0).load_runner_mode()
			# Base mode button
			if Rect2(350, 450, 380, 100).has_point(mouse_pos):
				get_tree().root.get_child(0).load_base_mode()

func draw_menu():
	var panel = Panel.new()
	panel.size = Vector2(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT)
	var bg = StyleBoxFlat.new()
	bg.bg_color = Constants.COLOR_BLACK
	panel.add_theme_stylebox_override("panel", bg)
	add_child(panel)

	# Title
	var title = Label.new()
	title.text = "GOGOT GAME"
	title.position = Vector2(Constants.SCREEN_WIDTH / 2 - 150, 100)
	title.add_theme_font_size_override("font_sizes", 64)
	add_child(title)

	# Subtitle
	var subtitle = Label.new()
	subtitle.text = "Runner + Base Building"
	subtitle.position = Vector2(Constants.SCREEN_WIDTH / 2 - 200, 200)
	subtitle.add_theme_font_size_override("font_sizes", 32)
	subtitle.modulate = Constants.COLOR_GREEN
	add_child(subtitle)

	# Runner Mode Button
	var runner_btn = Button.new()
	runner_btn.text = "1. RUNNER MODE"
	runner_btn.position = Vector2(350, 300)
	runner_btn.size = Vector2(380, 100)
	add_child(runner_btn)

	# Base Mode Button
	var base_btn = Button.new()
	base_btn.text = "2. BASE MODE"
	base_btn.position = Vector2(350, 450)
	base_btn.size = Vector2(380, 100)
	base_btn.modulate = Constants.COLOR_GREEN
	add_child(base_btn)

	# Instructions
	var inst_label = Label.new()
	inst_label.text = "Press A/D or Arrow Keys to move in Runner Mode\nClick buildings in Base Mode\nPress ESC to return to menu"
	inst_label.position = Vector2(50, 700)
	inst_label.add_theme_font_size_override("font_sizes", 18)
	inst_label.modulate = Constants.COLOR_GRAY
	add_child(inst_label)
