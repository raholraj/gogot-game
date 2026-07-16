"""UI System"""

import pygame
from config import *

class UIManager:
    """Manages all UI rendering and interaction"""
    
    def __init__(self):
        self.buttons = []
        self.text_elements = []
    
    def draw_button(self, screen, x, y, width, height, text, color=COLOR_BLUE, text_color=COLOR_WHITE):
        """Draw a button"""
        pygame.draw.rect(screen, color, (x, y, width, height))
        pygame.draw.rect(screen, COLOR_WHITE, (x, y, width, height), 2)
        
        font = pygame.font.Font(None, UI_FONT_SIZE_MEDIUM)
        text_render = font.render(text, True, text_color)
        text_rect = text_render.get_rect(center=(x + width // 2, y + height // 2))
        screen.blit(text_render, text_rect)
    
    def draw_progress_bar(self, screen, x, y, width, height, progress, 
                         bg_color=COLOR_GRAY, fg_color=COLOR_GREEN):
        """Draw progress bar"""
        # Background
        pygame.draw.rect(screen, bg_color, (x, y, width, height))
        
        # Progress
        progress_width = int(width * progress)
        pygame.draw.rect(screen, fg_color, (x, y, progress_width, height))
        
        # Border
        pygame.draw.rect(screen, COLOR_WHITE, (x, y, width, height), 2)
    
    def draw_text(self, screen, text, x, y, size=UI_FONT_SIZE_MEDIUM, color=COLOR_WHITE):
        """Draw text on screen"""
        font = pygame.font.Font(None, size)
        text_render = font.render(text, True, color)
        screen.blit(text_render, (x, y))
    
    def draw_resource_panel(self, screen, gold, iron, diamond):
        """Draw resource panel"""
        panel_height = 60
        pygame.draw.rect(screen, (50, 50, 50), (0, 0, SCREEN_WIDTH, panel_height))
        pygame.draw.rect(screen, COLOR_WHITE, (0, 0, SCREEN_WIDTH, panel_height), 2)
        
        self.draw_text(screen, f"Gold: {int(gold)}", 20, 15, color=COLOR_YELLOW)
        self.draw_text(screen, f"Iron: {int(iron)}", 300, 15, color=(192, 192, 192))
        self.draw_text(screen, f"Diamond: {int(diamond)}", 600, 15, color=(0, 150, 255))
    
    def draw_menu_item(self, screen, x, y, width, height, title, description, color=COLOR_BLUE):
        """Draw menu item"""
        pygame.draw.rect(screen, color, (x, y, width, height))
        pygame.draw.rect(screen, COLOR_WHITE, (x, y, width, height), 2)
        
        font_large = pygame.font.Font(None, 32)
        font_small = pygame.font.Font(None, 20)
        
        title_render = font_large.render(title, True, COLOR_WHITE)
        desc_render = font_small.render(description, True, COLOR_GRAY)
        
        screen.blit(title_render, (x + 20, y + 20))
        screen.blit(desc_render, (x + 20, y + 60))
