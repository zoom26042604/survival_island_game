"""
Demo script to showcase the Game class functionality.
"""

import sys
import os

# Add the project root to the path so 'src' is an importable package
sys.path.insert(0, os.path.dirname(__file__))

from src.controllers.game import Game


def main():
    """Demonstrate the Game class functionality."""
    print("=== Survival Island Game - Game Controller Demo ===\n")
    
    # Create a new game instance
    game = Game()
    print("Created new game instance")
    print(f"Game active: {game.is_game_active()}\n")
    
    # Start a new game
    print("Starting new game...")
    success = game.start_new_game("Demo Player")
    print(f"Game started successfully: {success}")
    print(f"Game active: {game.is_game_active()}")
    print(f"Player: {game.get_player()}\n")
    
    # Show initial game state
    print("Initial game state:")
    state = game.get_game_state()
    for key, value in state.items():
        print(f"  {key}: {value}")
    print()
    
    # Simulate several days
    print("Simulating days of survival...\n")
    
    day_count = 0
    while game.is_game_active() and day_count < 10:
        day_count += 1
        print(f"--- Day {day_count} ---")
        
        # Process the day
        day_summary = game.process_day()
        print(f"Day summary: {day_summary['day']}")
        print(f"Player status: {day_summary['player_status']}")
        
        # Run game loop to check for end conditions
        result = game.game_loop()
        if result:
            print(f"\nGame Over: {result}")
            break
            
        print(f"Game continues... (Active: {game.is_game_active()})\n")
    
    # Final game state
    print("\nFinal game state:")
    final_state = game.get_game_state()
    for key, value in final_state.items():
        print(f"  {key}: {value}")
    
    # Test save/load functionality
    print("\n=== Testing Save/Load Functionality ===")
    
    # Get save data
    save_data = game.get_game_state()
    print("Save data created")
    
    # Create new game and load data
    new_game = Game()
    print("Created new game instance")
    
    load_success = new_game.load_game(save_data)
    print(f"Load successful: {load_success}")
    
    if load_success:
        print("Loaded game state:")
        loaded_state = new_game.get_game_state()
        for key, value in loaded_state.items():
            print(f"  {key}: {value}")
    
    # Test victory scenario
    print("\n=== Testing Victory Scenario ===")
    victory_game = Game()
    victory_game.start_new_game("Victor")
    
    # Set player to day 29 with good stats
    victor = victory_game.get_player()
    victor.days_survived = 29
    victor.hunger = 80
    victor.thirst = 80
    victor.energy = 60
    
    print(f"Set up victory scenario: Day {victor.days_survived}")
    print(f"Victor status: {victor.get_status()}")
    
    # Process final day
    result = victory_game.game_loop()
    print(f"Victory result: {result}")
    print(f"Victory achieved: {victory_game.check_victory()}")


if __name__ == "__main__":
    main()