# Resource Manager
class_name ResourceManager

var resources = {}

func _init(starting_resources: Dictionary = {}):
	resources = {
		Constants.RESOURCE_GOLD: starting_resources.get(Constants.RESOURCE_GOLD, Constants.START_GOLD),
		Constants.RESOURCE_IRON: starting_resources.get(Constants.RESOURCE_IRON, Constants.START_IRON),
		Constants.RESOURCE_DIAMOND: starting_resources.get(Constants.RESOURCE_DIAMOND, Constants.START_DIAMOND)
	}

func add_resource(resource_type: String, amount: float):
	if resource_type in resources:
		resources[resource_type] += amount

func remove_resource(resource_type: String, amount: float) -> bool:
	if resource_type in resources:
		if resources[resource_type] >= amount:
			resources[resource_type] -= amount
			return true
	return false

func get_resource(resource_type: String) -> float:
	return resources.get(resource_type, 0)

func can_afford(cost: Dictionary) -> bool:
	for resource_type in cost:
		if get_resource(resource_type) < cost[resource_type]:
			return false
	return true

func spend_resources(cost: Dictionary) -> bool:
	if can_afford(cost):
		for resource_type in cost:
			remove_resource(resource_type, cost[resource_type])
		return true
	return false

func get_all_resources() -> Dictionary:
	return resources.duplicate()
