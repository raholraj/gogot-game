"""Enemy Entity"""

import pygame
from config import *

class Enemy:
    """Enemy entity (zombies, boss)"""
    
    def __init__(self, x, y, enemy_type):
        self.x = x
        self.y = y
        self.enemy_type = enemy_type
        
        if enemy_type == ENEMY_ZOMBIE_SMALL:
            self.width = 25
            self.height = 35
            self.health = 10
            self.attack = 5
            self.color = COLOR_GREEN
        elif enemy_type == ENEMY_ZOMBIE_BIG:
            self.width = 40
            self.height = 50
            self.health = 30
            self.attack = 15
            self.color = (150, 100, 0)
        else:  # BOSS
            self.width = 60
            self.height = 80
            self.health = 100
            self.attack = 30
            self.color = COLOR_RED
        
        self.animation_frame = 0
        self.animation_speed = 0.1
    
    def update(self):
        """Update enemy state"""
        self.animation_frame += self.animation_speed
        if self.animation_frame > 10:
            self.animation_frame = 0
    
    def draw(self, screen):
        """Draw enemy"""
        # Draw body
        pygame.draw.rect(screen, self.color,
                        (self.x - self.width // 2, self.y - self.height // 2,
                         self.width, self.height))
        
        # Draw head
        head_radius = self.width // 3
        pygame.draw.circle(screen, self.color,
                          (int(self.x), int(self.y - self.height // 2 - head_radius)), head_radius)
        
        # Draw eyes
        eye_color = COLOR_RED if self.enemy_type == ENEMY_BOSS else COLOR_BLACK
        pygame.draw.circle(screen, eye_color,
                          (int(self.x - 3), int(self.y - self.height // 2 - head_radius)), 2)
        pygame.draw.circle(screen, eye_color,
                          (int(self.x + 3), int(self.y - self.height // 2 - head_radius)), 2)
        
        # Draw health bar if damaged
        if self.health < self.health * 1.5:
            pygame.draw.rect(screen, COLOR_RED,
                            (self.x - self.width // 2, self.y - self.height // 2 - 15,
                             self.width, 5))
            pygame.draw.rect(screen, COLOR_GREEN,
                            (self.x - self.width // 2, self.y - self.height // 2 - 15,
                             int(self.width * self.health / (self.health * 1.5)), 5))
    
    def get_rect(self):
        """Get enemy rectangle for collision detection"""
        return pygame.Rect(self.x - self.width // 2, self.y - self.height // 2,
                          self.width, self.height)
