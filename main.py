"""Main Game Entry Point"""

import pygame
import sys
from config import *
from game.game import Game

def main():
    """Main function to run the game"""
    pygame.init()
    
    # Create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("GOGOT GAME - Runner + Base Building")
    
    # Create clock for FPS
    clock = pygame.time.Clock()
    
    # Create game instance
    game = Game(screen)
    
    # Main game loop
    running = True
    while running:
        clock.tick(FPS)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)
        
        # Update game
        game.update()
        
        # Draw game
        game.draw()
        
        # Update display
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
