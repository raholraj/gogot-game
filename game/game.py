"""Main Game Class"""

import pygame
from config import *
from game.state_manager import StateManager
from game.modes.runner_mode import RunnerMode
from game.modes.base_mode import BaseMode
from systems.ui import UIManager

class Game:
    """Main game controller"""
    
    def __init__(self, screen):
        self.screen = screen
        self.state_manager = StateManager()
        
        # Initialize modes
        self.runner_mode = RunnerMode()
        self.base_mode = BaseMode()
        
        # Initialize UI
        self.ui_manager = UIManager()
        
        # Game data
        self.player_data = {
            'level': 1,
            'squad_size': PLAYER_START_SQUAD,
            'gold': START_GOLD,
            'iron': START_IRON,
            'diamond': START_DIAMOND,
            'health': PLAYER_HEALTH,
            'attack': PLAYER_ATTACK,
            'defense': PLAYER_DEFENSE
        }
        
        self.game_stats = {
            'waves_defeated': 0,
            'enemies_killed': 0,
            'total_damage': 0,
            'accuracy': 100
        }
        
    def handle_event(self, event):
        """Handle pygame events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.state_manager.set_state(GAME_STATE_MENU)
            elif event.key == pygame.K_1:
                self.state_manager.set_state(GAME_STATE_RUNNER)
            elif event.key == pygame.K_2:
                self.state_manager.set_state(GAME_STATE_BASE)
            elif event.key == pygame.K_a:
                if self.state_manager.is_in_state(GAME_STATE_RUNNER):
                    self.runner_mode.move_left()
            elif event.key == pygame.K_d:
                if self.state_manager.is_in_state(GAME_STATE_RUNNER):
                    self.runner_mode.move_right()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_x, mouse_y = event.pos
                self.handle_click(mouse_x, mouse_y)
        
        elif event.type == pygame.MOUSEMOTION:
            if self.state_manager.is_in_state(GAME_STATE_BASE):
                self.base_mode.pan_camera(event.rel)
    
    def handle_click(self, x, y):
        """Handle mouse click"""
        if self.state_manager.is_in_state(GAME_STATE_MENU):
            # Check menu buttons
            if x > 350 and x < 730 and y > 300 and y < 400:
                self.state_manager.set_state(GAME_STATE_RUNNER)
            elif x > 350 and x < 730 and y > 450 and y < 550:
                self.state_manager.set_state(GAME_STATE_BASE)
        
        elif self.state_manager.is_in_state(GAME_STATE_BASE):
            self.base_mode.handle_click(x, y)
    
    def update(self):
        """Update game logic"""
        state = self.state_manager.get_state()
        
        if state == GAME_STATE_RUNNER:
            self.runner_mode.update(self.player_data)
        
        elif state == GAME_STATE_BASE:
            self.base_mode.update(self.player_data)
    
    def draw(self):
        """Draw game"""
        self.screen.fill(COLOR_BLACK)
        
        state = self.state_manager.get_state()
        
        if state == GAME_STATE_MENU:
            self.draw_menu()
        
        elif state == GAME_STATE_RUNNER:
            self.runner_mode.draw(self.screen, self.player_data)
        
        elif state == GAME_STATE_BASE:
            self.base_mode.draw(self.screen, self.player_data)
    
    def draw_menu(self):
        """Draw main menu"""
        font_large = pygame.font.Font(None, UI_FONT_SIZE_LARGE)
        font_medium = pygame.font.Font(None, UI_FONT_SIZE_MEDIUM)
        
        # Title
        title = font_large.render("GOGOT GAME", True, COLOR_BLUE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title, title_rect)
        
        # Subtitle
        subtitle = font_medium.render("Runner + Base Building", True, COLOR_GREEN)
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, 200))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Runner Mode Button
        pygame.draw.rect(self.screen, COLOR_BLUE, (350, 300, 380, 100))
        runner_text = font_medium.render("1. RUNNER MODE", True, COLOR_WHITE)
        runner_rect = runner_text.get_rect(center=(540, 350))
        self.screen.blit(runner_text, runner_rect)
        
        # Base Mode Button
        pygame.draw.rect(self.screen, COLOR_GREEN, (350, 450, 380, 100))
        base_text = font_medium.render("2. BASE MODE", True, COLOR_WHITE)
        base_rect = base_text.get_rect(center=(540, 500))
        self.screen.blit(base_text, base_rect)
        
        # Instructions
        instructions = [
            "Press 1 or Click -> Runner Mode",
            "Press 2 or Click -> Base Mode",
            "Press ESC -> Main Menu",
            "Press A/D -> Move Left/Right (Runner Mode)"
        ]
        
        y_pos = 700
        font_small = pygame.font.Font(None, UI_FONT_SIZE_SMALL)
        for instruction in instructions:
            text = font_small.render(instruction, True, COLOR_GRAY)
            self.screen.blit(text, (50, y_pos))
            y_pos += 40
