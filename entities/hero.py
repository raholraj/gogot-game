"""Hero Character Entity"""

import pygame
from config import *

class Hero:
    """Hero character for gacha system and base"""
    
    def __init__(self, hero_id, name, rarity, stats):
        self.hero_id = hero_id
        self.name = name
        self.rarity = rarity  # SSR, SR, UR, R
        
        self.health = stats.get('health', 50)
        self.attack = stats.get('attack', 10)
        self.defense = stats.get('defense', 5)
        self.speed = stats.get('speed', 5)
        
        self.level = 1
        self.experience = 0
        self.experience_to_level = 100
        
        # Rarity colors
        self.rarity_colors = {
            'SSR': (255, 215, 0),  # Gold
            'SR': (192, 192, 192),  # Silver
            'UR': (0, 150, 255),   # Blue
            'R': (150, 150, 150)   # Gray
        }
    
    def add_experience(self, amount):
        """Add experience to hero"""
        self.experience += amount
        if self.experience >= self.experience_to_level:
            self.level_up()
    
    def level_up(self):
        """Level up the hero"""
        self.level += 1
        self.experience = 0
        self.experience_to_level = int(self.experience_to_level * 1.2)
        
        # Increase stats
        self.health += 10
        self.attack += 3
        self.defense += 2
    
    def draw(self, screen, x, y):
        """Draw hero"""
        # Draw portrait circle
        color = self.rarity_colors.get(self.rarity, COLOR_WHITE)
        pygame.draw.circle(screen, color, (int(x), int(y)), 40)
        
        # Draw level
        font = pygame.font.Font(None, 20)
        level_text = font.render(f"Lv.{self.level}", True, COLOR_BLACK)
        screen.blit(level_text, (x - 15, y - 10))
    
    def get_info(self):
        """Get hero information dictionary"""
        return {
            'id': self.hero_id,
            'name': self.name,
            'rarity': self.rarity,
            'level': self.level,
            'health': self.health,
            'attack': self.attack,
            'defense': self.defense,
            'experience': self.experience
        }


# Predefined heroes for gacha
HEROES_POOL = [
    Hero('h_001', 'Monica', 'SSR', {'health': 100, 'attack': 25, 'defense': 10, 'speed': 8}),
    Hero('h_002', 'Gump', 'SR', {'health': 75, 'attack': 18, 'defense': 8, 'speed': 6}),
    Hero('h_003', 'Kimberly', 'UR', {'health': 85, 'attack': 20, 'defense': 12, 'speed': 7}),
    Hero('h_004', 'John', 'R', {'health': 60, 'attack': 12, 'defense': 5, 'speed': 5}),
    Hero('h_005', 'Sarah', 'SR', {'health': 80, 'attack': 15, 'defense': 9, 'speed': 7}),
]
