"""Base Building Mode"""

import pygame
from config import *
from entities.building import Building
from systems.ui import UIManager
from utils import *

class BaseMode:
    """Base building and management mode"""
    
    def __init__(self):
        self.buildings = []
        self.camera_offset_x = 0
        self.camera_offset_y = 0
        self.selected_building = None
        self.fog_cleared = 0  # Percentage of fog cleared
        self.ui_manager = UIManager()
        
        # Initialize buildings
        self.init_buildings()
    
    def init_buildings(self):
        """Initialize base buildings"""
        # Headquarters (center)
        hq = Building(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BUILDING_HQ, 1)
        self.buildings.append(hq)
        
        # Barracks
        barracks = Building(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 150, BUILDING_BARRACKS, 1)
        self.buildings.append(barracks)
        
        # Tavern
        tavern = Building(SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 - 150, BUILDING_TAVERN, 1)
        self.buildings.append(tavern)
        
        # Defenses
        defense1 = Building(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2, BUILDING_DEFENSE, 1)
        self.buildings.append(defense1)
        
        defense2 = Building(SCREEN_WIDTH // 2 + 300, SCREEN_HEIGHT // 2, BUILDING_DEFENSE, 1)
        self.buildings.append(defense2)
    
    def pan_camera(self, offset):
        """Pan camera"""
        self.camera_offset_x += offset[0]
        self.camera_offset_y += offset[1]
        
        # Clamp camera
        self.camera_offset_x = clamp(self.camera_offset_x, -500, 500)
        self.camera_offset_y = clamp(self.camera_offset_y, -500, 500)
    
    def handle_click(self, x, y):
        """Handle click on building"""
        for building in self.buildings:
            if building.check_click(x - self.camera_offset_x, y - self.camera_offset_y):
                self.selected_building = building
                break
    
    def update(self, player_data):
        """Update base mode"""
        # Update buildings
        for building in self.buildings:
            building.update()
            
            # Generate resources
            if building.building_type == BUILDING_HQ:
                player_data['gold'] += 0.1
            elif building.building_type == BUILDING_MINE:
                player_data['iron'] += 0.1
        
        # Update fog clearing
        if self.fog_cleared < 100:
            self.fog_cleared += 0.01
    
    def draw(self, screen, player_data):
        """Draw base mode"""
        # Draw background (base area)
        screen.fill((50, 100, 50))
        
        # Draw toxic fog
        fog_alpha = int(255 * (1 - self.fog_cleared / 100))
        fog_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        fog_surface.set_alpha(fog_alpha)
        fog_surface.fill(COLOR_TOXIC_GREEN)
        screen.blit(fog_surface, (0, 0))
        
        # Draw grid
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(screen, COLOR_GRAY, 
                            (x + self.camera_offset_x, 0),
                            (x + self.camera_offset_x, SCREEN_HEIGHT), 1)
        
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, COLOR_GRAY,
                            (0, y + self.camera_offset_y),
                            (SCREEN_WIDTH, y + self.camera_offset_y), 1)
        
        # Draw buildings
        for building in self.buildings:
            building.draw(screen, self.camera_offset_x, self.camera_offset_y)
            
            # Highlight selected building
            if building == self.selected_building:
                x = building.x + self.camera_offset_x
                y = building.y + self.camera_offset_y
                pygame.draw.rect(screen, COLOR_YELLOW,
                               (x - 35, y - 35, 70, 70), 3)
        
        # Draw UI
        self.draw_ui(screen, player_data)
    
    def draw_ui(self, screen, player_data):
        """Draw UI for base mode"""
        font_large = pygame.font.Font(None, UI_FONT_SIZE_LARGE)
        font_medium = pygame.font.Font(None, UI_FONT_SIZE_MEDIUM)
        font_small = pygame.font.Font(None, UI_FONT_SIZE_SMALL)
        
        # Resources at top
        resources_text = [
            f"Gold: {int(player_data['gold'])}",
            f"Iron: {int(player_data['iron'])}",
            f"Diamond: {player_data['diamond']}"
        ]
        
        x_pos = 20
        for text in resources_text:
            resource_render = font_medium.render(text, True, COLOR_YELLOW)
            screen.blit(resource_render, (x_pos, 20))
            x_pos += 300
        
        # Fog cleared progress
        progress_text = font_medium.render(f"Fog: {self.fog_cleared:.1f}%", True, COLOR_WHITE)
        screen.blit(progress_text, (20, 80))
        
        # Drawing progress bar
        pygame.draw.rect(screen, COLOR_GRAY, (20, 120, 200, 20))
        pygame.draw.rect(screen, COLOR_GREEN, (20, 120, int(200 * self.fog_cleared / 100), 20))
        
        # Selected building info
        if self.selected_building:
            info_text = f"Selected: {self.selected_building.building_type.upper()} (Lv. {self.selected_building.level})"
            info_render = font_medium.render(info_text, True, COLOR_BLUE)
            screen.blit(info_render, (20, SCREEN_HEIGHT - 100))
            
            # Upgrade button
            upgrade_text = font_small.render("[U] Upgrade | [R] Repair", True, COLOR_WHITE)
            screen.blit(upgrade_text, (20, SCREEN_HEIGHT - 50))
        
        # Instructions
        inst_text = font_small.render("Click to select | Drag to pan | ESC to menu", True, COLOR_GRAY)
        screen.blit(inst_text, (SCREEN_WIDTH - 500, SCREEN_HEIGHT - 30))
