"""Building Entity for Base Mode"""

import pygame
from config import *

class Building:
    """Building entity for base construction"""
    
    def __init__(self, x, y, building_type, level=1):
        self.x = x
        self.y = y
        self.building_type = building_type
        self.level = level
        self.width = 60
        self.height = 60
        self.health = 100
        
        # Building properties
        self.build_time = 60  # frames
        self.upgrade_cost = {'gold': 100 * level, 'iron': 50 * level}
        self.resource_production = {
            BUILDING_HQ: {'gold': 0.5},
            BUILDING_BARRACKS: {'troops': 1},
            BUILDING_TAVERN: {'heroes': 0.1},
            BUILDING_MINE: {'iron': 0.5},
            BUILDING_FARM: {'food': 0.5},
            BUILDING_DEFENSE: {'defense': 1}
        }
        
        self.colors = {
            BUILDING_HQ: COLOR_BLUE,
            BUILDING_BARRACKS: COLOR_RED,
            BUILDING_TAVERN: COLOR_YELLOW,
            BUILDING_MINE: (100, 100, 100),
            BUILDING_FARM: COLOR_GREEN,
            BUILDING_DEFENSE: (128, 0, 128)
        }
        
        self.is_upgrading = False
        self.upgrade_progress = 0
    
    def upgrade(self, player_data):
        """Upgrade the building"""
        cost = self.upgrade_cost
        if player_data['gold'] >= cost['gold'] and player_data['iron'] >= cost['iron']:
            player_data['gold'] -= cost['gold']
            player_data['iron'] -= cost['iron']
            self.is_upgrading = True
            self.upgrade_progress = 0
            return True
        return False
    
    def repair(self, player_data):
        """Repair the building"""
        repair_cost = int(50 * (1 - self.health / 100))
        if player_data['iron'] >= repair_cost:
            player_data['iron'] -= repair_cost
            self.health = 100
            return True
        return False
    
    def update(self):
        """Update building state"""
        if self.is_upgrading:
            self.upgrade_progress += 1
            if self.upgrade_progress >= self.build_time:
                self.level += 1
                self.is_upgrading = False
                self.health = 100
                self.upgrade_cost['gold'] *= 1.2
                self.upgrade_cost['iron'] *= 1.2
    
    def draw(self, screen, camera_offset_x, camera_offset_y):
        """Draw building"""
        x = int(self.x + camera_offset_x)
        y = int(self.y + camera_offset_y)
        
        # Get building color
        color = self.colors.get(self.building_type, COLOR_WHITE)
        
        # Draw building
        pygame.draw.rect(screen, color,
                        (x - self.width // 2, y - self.height // 2,
                         self.width, self.height))
        
        # Draw upgrade progress
        if self.is_upgrading:
            progress = int(self.width * self.upgrade_progress / self.build_time)
            pygame.draw.rect(screen, COLOR_YELLOW,
                            (x - self.width // 2, y - self.height // 2 - 10,
                             progress, 5))
        
        # Draw level
        font = pygame.font.Font(None, 20)
        level_text = font.render(f"L{self.level}", True, COLOR_WHITE)
        screen.blit(level_text, (x - 10, y - 10))
        
        # Draw health bar if damaged
        if self.health < 100:
            pygame.draw.rect(screen, COLOR_RED,
                            (x - self.width // 2, y + self.height // 2 + 5,
                             self.width, 5))
            pygame.draw.rect(screen, COLOR_GREEN,
                            (x - self.width // 2, y + self.height // 2 + 5,
                             int(self.width * self.health / 100), 5))
    
    def check_click(self, x, y):
        """Check if building was clicked"""
        return (self.x - self.width // 2 < x < self.x + self.width // 2 and
                self.y - self.height // 2 < y < self.y + self.height // 2)
