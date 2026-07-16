"""Runner Mode - Frontline Breakthrough"""

import pygame
import random
from config import *
from entities.player import Player
from entities.enemy import Enemy
from systems.collision import CollisionSystem
from utils import *

class RunnerMode:
    """Runner/Frontline mode gameplay"""
    
    def __init__(self):
        self.player = Player(get_lane_x_position(1), SCREEN_HEIGHT - 100, 1)  # Middle lane
        self.enemies = []
        self.math_gates = []
        self.projectiles = []
        
        self.wave = 1
        self.wave_progress = 0
        self.boss_health = BOSS_HEALTH
        self.distance_traveled = 0
        self.enemies_killed = 0
        
        self.spawn_timer = 0
        self.spawn_rate = 60  # Spawn enemy every 60 frames
        
        self.collision_system = CollisionSystem()
        
    def move_left(self):
        """Move player to left lane"""
        if self.player.lane > 0:
            self.player.move_to_lane(self.player.lane - 1)
    
    def move_right(self):
        """Move player to right lane"""
        if self.player.lane < NUM_LANES - 1:
            self.player.move_to_lane(self.player.lane + 1)
    
    def update(self, player_data):
        """Update runner mode"""
        # Move player forward
        self.player.y -= RUNNER_SPEED
        self.distance_traveled += RUNNER_SPEED
        
        # Update player
        self.player.update()
        
        # Spawn enemies and gates
        self.spawn_timer += 1
        if self.spawn_timer > self.spawn_rate:
            self.spawn_wave()
            self.spawn_timer = 0
        
        # Update enemies
        for enemy in self.enemies[:]:
            enemy.update()
            enemy.y += ENEMY_SPEED
            
            # Check collision with player
            if self.collision_system.check_collision(self.player, enemy):
                player_data['squad_size'] -= 20
                self.enemies.remove(enemy)
                continue
            
            # Remove if off screen
            if enemy.y > SCREEN_HEIGHT:
                self.enemies.remove(enemy)
                self.enemies_killed += 1
        
        # Update math gates
        for gate in self.math_gates[:]:
            gate['y'] += RUNNER_SPEED * 0.5
            
            # Check collision with player
            if self.collision_system.check_gate_collision(self.player, gate):
                gate_type = gate['type']
                player_data['squad_size'] = apply_math_gate_effect(
                    player_data['squad_size'], 
                    gate_type
                )
                self.math_gates.remove(gate)
            
            # Remove if off screen
            if gate['y'] > SCREEN_HEIGHT:
                self.math_gates.remove(gate)
        
        # Update projectiles (auto-fire)
        for projectile in self.projectiles[:]:
            projectile['y'] -= 15
            
            # Check collision with enemies
            hit = False
            for enemy in self.enemies:
                if self.collision_system.check_projectile_collision(projectile, enemy):
                    self.projectiles.remove(projectile)
                    enemy.health -= player_data['attack']
                    if enemy.health <= 0:
                        self.enemies.remove(enemy)
                        self.enemies_killed += 1
                    hit = True
                    break
            
            if not hit and projectile['y'] < 0:
                self.projectiles.remove(projectile)
        
        # Auto-fire projectiles
        if random.random() < 0.3:  # 30% chance per frame
            self.projectiles.append({
                'x': self.player.x,
                'y': self.player.y,
                'width': 5,
                'height': 15
            })
        
        # Check game over
        if player_data['squad_size'] <= 0:
            player_data['squad_size'] = 0
    
    def spawn_wave(self):
        """Spawn enemies and math gates"""
        # Spawn random enemy
        if random.random() < 0.7:
            lane = random.randint(0, NUM_LANES - 1)
            enemy_type = random.choice([ENEMY_ZOMBIE_SMALL, ENEMY_ZOMBIE_BIG])
            enemy = Enemy(get_lane_x_position(lane), -50, enemy_type)
            self.enemies.append(enemy)
        
        # Spawn math gate
        if random.random() < 0.3:
            lane = random.randint(0, NUM_LANES - 1)
            gate_type = random.choice(['blue', 'red'])
            self.math_gates.append({
                'x': get_lane_x_position(lane),
                'y': -50,
                'width': 40,
                'height': 40,
                'type': gate_type
            })
    
    def draw(self, screen, player_data):
        """Draw runner mode"""
        # Draw background
        screen.fill(COLOR_BLUE)
        
        # Draw lanes
        for i in range(1, NUM_LANES):
            x = i * LANE_WIDTH
            pygame.draw.line(screen, COLOR_WHITE, (x, 0), (x, SCREEN_HEIGHT), 2)
        
        # Draw player
        self.player.draw(screen)
        
        # Draw enemies
        for enemy in self.enemies:
            enemy.draw(screen)
        
        # Draw math gates
        for gate in self.math_gates:
            color = COLOR_BLUE if gate['type'] == 'blue' else COLOR_RED
            pygame.draw.rect(screen, color, 
                            (gate['x'] - 20, gate['y'] - 20, 40, 40))
            
            # Draw text on gate
            font = pygame.font.Font(None, 24)
            text = font.render('+10' if gate['type'] == 'blue' else '-20', 
                              True, COLOR_WHITE)
            screen.blit(text, (gate['x'] - 15, gate['y'] - 10))
        
        # Draw projectiles
        for projectile in self.projectiles:
            pygame.draw.rect(screen, COLOR_YELLOW,
                            (projectile['x'], projectile['y'],
                             projectile['width'], projectile['height']))
        
        # Draw UI
        self.draw_ui(screen, player_data)
    
    def draw_ui(self, screen, player_data):
        """Draw UI for runner mode"""
        font_large = pygame.font.Font(None, UI_FONT_SIZE_LARGE)
        font_medium = pygame.font.Font(None, UI_FONT_SIZE_MEDIUM)
        font_small = pygame.font.Font(None, UI_FONT_SIZE_SMALL)
        
        # Squad size
        squad_text = font_large.render(f"Squad: {player_data['squad_size']}", True, COLOR_WHITE)
        screen.blit(squad_text, (20, 20))
        
        # Distance
        distance_text = font_medium.render(f"Distance: {self.distance_traveled // 100}", True, COLOR_WHITE)
        screen.blit(distance_text, (20, 80))
        
        # Enemies killed
        kills_text = font_medium.render(f"Kills: {self.enemies_killed}", True, COLOR_WHITE)
        screen.blit(kills_text, (20, 130))
        
        # Wave info
        wave_text = font_medium.render(f"Wave: {self.wave}", True, COLOR_YELLOW)
        screen.blit(wave_text, (SCREEN_WIDTH - 300, 20))
        
        # Instructions
        inst_text = font_small.render("A/D to move | ESC to menu", True, COLOR_GRAY)
        screen.blit(inst_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT - 50))
