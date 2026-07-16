# State Manager for game state transitions
class_name StateManager

var current_state: String = Constants.STATE_MENU
var previous_state: String = ""
var state_data = {}

func change_state(new_state: String, data = null):
	previous_state = current_state
	current_state = new_state
	if data:
		state_data = data

func get_current_state() -> String:
	return current_state

func get_previous_state() -> String:
	return previous_state

func is_in_state(state: String) -> bool:
	return current_state == state

func get_state_data():
	return state_data
