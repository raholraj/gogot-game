# Combat System
class_name CombatSystem

var battle_log = []

func simulate_battle(attacker: Dictionary, defender: Dictionary) -> Dictionary:
	var attacker_hp = attacker["health"]
	var defender_hp = defender["health"]
	var round_num = 0
	var max_rounds = 100

	while attacker_hp > 0 and defender_hp > 0 and round_num < max_rounds:
		# Attacker attacks
		var damage = CollisionSystem.calculate_damage(attacker["attack"], defender["defense"])
		damage += randi() % 5 - 2
		defender_hp -= damage

		if defender_hp <= 0:
			return {"winner": "attacker", "rounds": round_num, "damage_dealt": damage}

		# Defender counter-attacks
		var counter_damage = CollisionSystem.calculate_damage(defender["attack"], attacker["attack"])
		counter_damage += randi() % 5 - 2
		attacker_hp -= counter_damage

		if attacker_hp <= 0:
			return {"winner": "defender", "rounds": round_num, "damage_dealt": counter_damage}

		round_num += 1

	return {"winner": "draw", "rounds": round_num}

func simulate_squad_battle(squad_size: int, enemy_squad_size: int, player_attack: int, enemy_attack: int) -> String:
	var player_hp = squad_size * 10
	var enemy_hp = enemy_squad_size * 10

	while player_hp > 0 and enemy_hp > 0:
		var damage = player_attack * randf_range(0.8, 1.2)
		enemy_hp -= damage

		if enemy_hp <= 0:
			return "player_win"

		damage = enemy_attack * randf_range(0.8, 1.2)
		player_hp -= damage

		if player_hp <= 0:
			return "enemy_win"

	return "draw"
