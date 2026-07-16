# Hero Gacha System
class_name HeroGacha

var heroes = [
	{"id": "h_001", "name": "Monica", "rarity": "SSR", "health": 100, "attack": 25, "defense": 10},
	{"id": "h_002", "name": "Gump", "rarity": "SR", "health": 75, "attack": 18, "defense": 8},
	{"id": "h_003", "name": "Kimberly", "rarity": "UR", "health": 85, "attack": 20, "defense": 12},
	{"id": "h_004", "name": "John", "rarity": "R", "health": 60, "attack": 12, "defense": 5},
	{"id": "h_005", "name": "Sarah", "rarity": "SR", "health": 80, "attack": 15, "defense": 9},
]

func get_random_hero():
	return heroes[randi() % heroes.size()]

func get_hero_by_rarity(rarity: String):
	var filtered = heroes.filter(func(h): return h["rarity"] == rarity)
	if filtered.size() > 0:
		return filtered[randi() % filtered.size()]
	return null

func get_all_heroes():
	return heroes
