"""Utility Functions"""

import math
import random
from config import *

def distance(x1, y1, x2, y2):
    """Calculate distance between two points"""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def clamp(value, min_val, max_val):
    """Clamp value between min and max"""
    return max(min_val, min(max_val, value))

def lerp(a, b, t):
    """Linear interpolation"""
    return a + (b - a) * t

def random_choice(items):
    """Select random item from list"""
    return random.choice(items)

def get_lane_x_position(lane):
    """Get X position for a lane (0, 1, 2)"""
    return (lane + 0.5) * LANE_WIDTH

def check_collision_rect(rect1, rect2):
    """Check collision between two rectangles"""
    return rect1.colliderect(rect2)

def check_collision_circle(x1, y1, r1, x2, y2, r2):
    """Check collision between two circles"""
    dist = distance(x1, y1, x2, y2)
    return dist < (r1 + r2)

def apply_math_gate_effect(squad_size, gate_type):
    """Apply math gate effect to squad size"""
    if gate_type == "blue":
        squad_size = int(squad_size * BLUE_GATE_MULTIPLIER) + BLUE_GATE_BONUS
    elif gate_type == "red":
        squad_size = max(0, int(squad_size / RED_GATE_DIVISOR) + RED_GATE_PENALTY)
    return squad_size

def calculate_damage(attacker_attack, defender_defense):
    """Calculate damage dealt"""
    base_damage = attacker_attack
    defense_reduction = defender_defense * 0.1
    final_damage = max(1, base_damage - defense_reduction)
    return int(final_damage)

def calculate_battle_winner(hero1_hp, hero1_attack, hero1_defense,
                           hero2_hp, hero2_attack, hero2_defense):
    """Simulate battle and return winner"""
    h1_hp = hero1_hp
    h2_hp = hero2_hp
    
    while h1_hp > 0 and h2_hp > 0:
        # Hero 1 attacks
        damage = calculate_damage(hero1_attack, hero2_defense)
        h2_hp -= damage
        
        if h2_hp <= 0:
            return 1
        
        # Hero 2 attacks
        damage = calculate_damage(hero2_attack, hero1_defense)
        h1_hp -= damage
        
        if h1_hp <= 0:
            return 2
    
    return 0

def format_number(num):
    """Format number with K, M suffix"""
    if num >= 1000000:
        return f"{num / 1000000:.1f}M"
    elif num >= 1000:
        return f"{num / 1000:.1f}K"
    return str(num)

def get_resource_color(resource_type):
    """Get color for resource type"""
    colors = {
        RESOURCE_GOLD: COLOR_YELLOW,
        RESOURCE_IRON: (192, 192, 192),
        RESOURCE_DIAMOND: (0, 150, 255)
    }
    return colors.get(resource_type, COLOR_WHITE)
