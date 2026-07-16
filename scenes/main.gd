# Main Scene
extends Node

func _ready():
	add_child(GameManager.new())
	GameManager._ready()
