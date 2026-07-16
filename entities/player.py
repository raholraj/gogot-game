"""Player Character Entity"""

import pygame
from config import *
from utils import get_lane_x_position

class Player:
    """Player character in runner mode"""
    
    def __init__(self, x, y, lane):
        self.x = x
        self.y = y
        self.lane = lane
        self.width = 30
        self.height = 40
        self.health = PLAYER_HEALTH
        self.attack = PLAYER_ATTACK
        self.defense = PLAYER_DEFENSE
        self.squad_size = PLAYER_START_SQUAD
        
        self.animation_frame = 0
        self.animation_speed = 0.1
    
    def move_to_lane(self, lane):
        """Move player to specified lane"""
        self.lane = lane
        self.x = get_lane_x_position(lane)
    
    def update(self):
        """Update player state"""
        self.animation_frame += self.animation_speed
        if self.animation_frame > 10:
            self.animation_frame = 0
    
    def draw(self, screen):
        """Draw player character"""
        # Draw soldier body
        pygame.draw.rect(screen, COLOR_BLUE,
                        (self.x - self.width // 2, self.y - self.height // 2,
                         self.width, self.height))
        
        # Draw helmet
        pygame.draw.circle(screen, (0, 50, 200),
                          (int(self.x), int(self.y - self.height // 2 - 10)), 8)
        
        # Draw gun
        pygame.draw.line(screen, COLOR_GRAY,
                        (self.x + self.width // 2, self.y - 5),
                        (self.x + self.width // 2 + 20, self.y - 5), 3)
        
        # Draw squad size above player
        font = pygame.font.Font(None, 24)
        squad_text = font.render(str(self.squad_size), True, COLOR_WHITE)
        screen.blit(squad_text, (self.x - 15, self.y - 60))
    
    def get_rect(self):
        """Get player rectangle for collision detection"""
        return pygame.Rect(self.x - self.width // 2, self.y - self.height // 2,
                          self.width, self.height)
