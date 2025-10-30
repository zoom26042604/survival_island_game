"""
Demo script to showcase the Player class functionality.
"""

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from models.player import Player


def main():
    """Demonstrate the Player class functionality."""
    print("=== Survival Island Game - Player Demo ===\n")
    
    # Create a new player
    player = Player("Alex")
    print(f"Created player: {player}")
    print(f"Initial status:\n{player.get_status()}\n")
    
    # Simulate some days
    print("Simulating survival days...\n")
    
    for day in range(1, 6):
        print(f"--- Day {day} ---")
        
        # Natural evolution (hunger/thirst increase, energy decreases)
        player.natural_evolution()
        
        print(f"After natural evolution:")
        print(f"  Hunger: {player.hunger}/100 ({player.get_gauge_status('hunger')})")
        print(f"  Thirst: {player.thirst}/100 ({player.get_gauge_status('thirst')})")
        print(f"  Energy: {player.energy}/100 ({player.get_gauge_status('energy')})")
        
        # Check game over
        game_over = player.check_game_over()
        if game_over:
            print(f"\n{game_over}")
            break
            
        # Simulate some action (finding food/water/rest)
        if day == 2:
            print("  -> Found some berries! (+20 hunger)")
            player.update_gauges(hunger_change=20)
        elif day == 3:
            print("  -> Found a water source! (+30 thirst)")
            player.update_gauges(thirst_change=30)
        elif day == 4:
            print("  -> Took a good rest! (+25 energy)")
            player.update_gauges(energy_change=25)
            
        print(f"  Status: {'Alive' if player.is_alive else 'Dead'}")
        print()
    
    print(f"\nFinal player status:\n{player.get_status()}")
    
    # Test death scenario
    print("\n=== Testing Death Scenario ===")
    doomed_player = Player("TestSubject")
    print(f"Created test player: {doomed_player}")
    
    # Drain all energy
    doomed_player.update_gauges(energy_change=-100)
    print(f"Drained all energy...")
    print(f"Player alive: {doomed_player.is_alive}")
    print(f"Game over: {doomed_player.check_game_over()}")


if __name__ == "__main__":
    main()