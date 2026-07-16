"""Game State Manager"""

from config import *

class StateManager:
    """Manages game states and transitions"""
    
    def __init__(self):
        self.current_state = GAME_STATE_MENU
        self.previous_state = None
        self.states = {}
        
    def set_state(self, new_state):
        """Change to a new game state"""
        self.previous_state = self.current_state
        self.current_state = new_state
        
    def get_state(self):
        """Get current game state"""
        return self.current_state
    
    def is_in_state(self, state):
        """Check if currently in a specific state"""
        return self.current_state == state
