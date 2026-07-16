"""Collision Detection System"""

import pygame
from utils import distance

class CollisionSystem:
    """Handles collision detection"""
    
    def __init__(self):
        pass
    
    def check_collision(self, player, enemy):
        """Check collision between player and enemy"""
        player_rect = player.get_rect()
        enemy_rect = enemy.get_rect()
        return player_rect.colliderect(enemy_rect)
    
    def check_gate_collision(self, player, gate):
        """Check collision between player and math gate"""
        player_rect = player.get_rect()
        gate_rect = pygame.Rect(gate['x'] - gate['width'] // 2, gate['y'] - gate['height'] // 2,
                                gate['width'], gate['height'])
        return player_rect.colliderect(gate_rect)
    
    def check_projectile_collision(self, projectile, enemy):
        """Check collision between projectile and enemy"""
        dist = distance(projectile['x'], projectile['y'],
                       enemy.x, enemy.y)
        return dist < (projectile['width'] / 2 + enemy.width / 2)
    
    def check_point_in_rect(self, x, y, rect_x, rect_y, rect_w, rect_h):
        """Check if point is inside rectangle"""
        return (rect_x < x < rect_x + rect_w and
                rect_y < y < rect_y + rect_h)
    
    def get_collision_distance(self, x1, y1, x2, y2):
        """Get distance between two points"""
        return distance(x1, y1, x2, y2)
