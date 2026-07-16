"""Combat System"""

import random
from utils import calculate_damage

class CombatSystem:
    """Handles battle mechanics"""
    
    def __init__(self):
        self.battle_log = []
    
    def calculate_battle_outcome(self, attacker_stats, defender_stats):
        """Calculate battle outcome"""
        attacker_hp = attacker_stats['health']
        defender_hp = defender_stats['health']
        
        round_num = 0
        max_rounds = 100
        
        while attacker_hp > 0 and defender_hp > 0 and round_num < max_rounds:
            # Attacker attacks
            damage = calculate_damage(attacker_stats['attack'], defender_stats['defense'])
            damage += random.randint(-2, 2)  # Add variance
            defender_hp -= damage
            
            self.battle_log.append(f"Round {round_num}: Attacker deals {damage} damage")
            
            if defender_hp <= 0:
                return {'winner': 'attacker', 'rounds': round_num}
            
            # Defender counter-attacks
            counter_damage = calculate_damage(defender_stats['attack'], attacker_stats['defense'])
            counter_damage += random.randint(-2, 2)
            attacker_hp -= counter_damage
            
            self.battle_log.append(f"Round {round_num}: Defender deals {counter_damage} damage")
            
            if attacker_hp <= 0:
                return {'winner': 'defender', 'rounds': round_num}
            
            round_num += 1
        
        # Draw if max rounds reached
        return {'winner': 'draw', 'rounds': round_num}
    
    def simulate_squad_battle(self, squad_size, enemy_squad_size, player_attack, enemy_attack):
        """Simulate battle between squads"""
        player_hp = squad_size * 10  # Each soldier has 10 HP
        enemy_hp = enemy_squad_size * 10
        
        while player_hp > 0 and enemy_hp > 0:
            # Player attacks
            damage = player_attack * random.uniform(0.8, 1.2)
            enemy_hp -= damage
            
            if enemy_hp <= 0:
                return 'player_win'
            
            # Enemy attacks
            damage = enemy_attack * random.uniform(0.8, 1.2)
            player_hp -= damage
            
            if player_hp <= 0:
                return 'enemy_win'
        
        return 'draw'
    
    def get_battle_log(self):
        """Get battle log"""
        return self.battle_log
    
    def clear_battle_log(self):
        """Clear battle log"""
        self.battle_log = []
