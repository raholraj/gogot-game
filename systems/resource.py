"""Resource Management System"""

from config import *

class ResourceManager:
    """Manages game resources"""
    
    def __init__(self):
        self.resources = {
            RESOURCE_GOLD: START_GOLD,
            RESOURCE_IRON: START_IRON,
            RESOURCE_DIAMOND: START_DIAMOND
        }
    
    def add_resource(self, resource_type, amount):
        """Add resource"""
        if resource_type in self.resources:
            self.resources[resource_type] += amount
    
    def remove_resource(self, resource_type, amount):
        """Remove resource if available"""
        if resource_type in self.resources:
            if self.resources[resource_type] >= amount:
                self.resources[resource_type] -= amount
                return True
        return False
    
    def get_resource(self, resource_type):
        """Get resource amount"""
        return self.resources.get(resource_type, 0)
    
    def can_afford(self, cost_dict):
        """Check if can afford cost"""
        for resource, amount in cost_dict.items():
            if self.get_resource(resource) < amount:
                return False
        return True
    
    def spend_resources(self, cost_dict):
        """Spend resources if affordable"""
        if self.can_afford(cost_dict):
            for resource, amount in cost_dict.items():
                self.remove_resource(resource, amount)
            return True
        return False
