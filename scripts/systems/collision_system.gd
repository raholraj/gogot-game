# Collision System
class_name CollisionSystem

static func check_rect_overlap(rect1: Rect2, rect2: Rect2) -> bool:
	return rect1.intersects(rect2)

static func check_circle_overlap(center1: Vector2, radius1: float, center2: Vector2, radius2: float) -> bool:
	var distance = center1.distance_to(center2)
	return distance < (radius1 + radius2)

static func get_distance(point1: Vector2, point2: Vector2) -> float:
	return point1.distance_to(point2)

static func calculate_damage(attacker_attack: int, defender_defense: int) -> int:
	var base_damage = attacker_attack
	var defense_reduction = defender_defense * 0.1
	var final_damage = max(1, base_damage - defense_reduction)
	return int(final_damage)
