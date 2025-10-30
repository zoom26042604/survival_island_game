#!/usr/bin/env python3
"""
Quick test script to verify actions work correctly.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.models.player import Player
from src.controllers.action_manager import ActionManager

def test_actions():
    """Test all actions to verify they work."""
    print("=== TESTING ACTIONS ===\n")
    
    # Create player and action manager
    player = Player("Test Player")
    action_manager = ActionManager()
    
    print("Initial Status:")
    print(f"Hunger: {player.hunger}/100 (satisfaction: {100 - player.hunger})")
    print(f"Thirst: {player.thirst}/100 (hydration: {100 - player.thirst})")
    print(f"Energy: {player.energy}/100")
    print()
    
    # Test 1: Fish action
    print("🎣 Testing Fish Action...")
    print("Expected: -20 hunger (more satisfied), -15 energy")
    action_manager.execute_fish_action(player)
    print(f"After fishing:")
    print(f"Hunger: {player.hunger}/100 (satisfaction: {100 - player.hunger}) - Should be 120 satisfaction")
    print(f"Energy: {player.energy}/100 - Should be 85")
    print()
    
    # Test 2: Find water action
    print("💧 Testing Find Water Action...")
    print("Expected: -15 thirst (more hydrated), -10 energy")
    action_manager.execute_find_water_action(player)
    print(f"After finding water:")
    print(f"Thirst: {player.thirst}/100 (hydration: {100 - player.thirst}) - Should be 115 hydration")
    print(f"Energy: {player.energy}/100 - Should be 75")
    print()
    
    # Test 3: Sleep action
    print("😴 Testing Sleep Action...")
    print("Expected: +30 energy, +10 hunger, +5 thirst")
    action_manager.execute_sleep_action(player)
    print(f"After sleeping:")
    print(f"Hunger: {player.hunger}/100 (satisfaction: {100 - player.hunger}) - Should be 110 satisfaction")
    print(f"Thirst: {player.thirst}/100 (hydration: {100 - player.thirst}) - Should be 110 hydration")
    print(f"Energy: {player.energy}/100 - Should be 100 (clamped)")
    print()
    
    # Test survival scenario
    print("=== SURVIVAL SCENARIO TEST ===")
    survivor = Player("Survivor")
    
    # Simulate several days with actions
    for day in range(1, 6):
        print(f"\n--- Day {day} ---")
        print(f"Start: Hunger {survivor.hunger}, Thirst {survivor.thirst}, Energy {survivor.energy}")
        
        # Natural evolution first
        survivor.natural_evolution()
        print(f"After evolution: Hunger {survivor.hunger}, Thirst {survivor.thirst}, Energy {survivor.energy}")
        
        # Take action based on needs
        if survivor.hunger > 80:  # Very hungry
            print("Action: Fishing (desperate for food)")
            action_manager.execute_fish_action(survivor)
        elif survivor.thirst > 80:  # Very thirsty
            print("Action: Finding water (desperate for water)")
            action_manager.execute_find_water_action(survivor)
        elif survivor.energy < 30:  # Very tired
            print("Action: Sleeping (desperate for rest)")
            action_manager.execute_sleep_action(survivor)
        else:
            print("Action: Fishing (maintaining)")
            action_manager.execute_fish_action(survivor)
            
        print(f"End: Hunger {survivor.hunger}, Thirst {survivor.thirst}, Energy {survivor.energy}")
        print(f"Status: {'Alive' if survivor.is_alive else 'Dead'}")
        
        if not survivor.is_alive:
            print("GAME OVER!")
            break
    
    print(f"\nFinal result: Survived {survivor.days_survived} days")

if __name__ == "__main__":
    test_actions()