"""
Game controller class - main game logic and flow management.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.models.player import Player


class Game:
    """
    Main game controller managing the game state and flow.
    
    Attributes:
        player (Player): The player instance
        is_running (bool): Whether the game is currently running
        game_over_reason (str): Reason for game over if applicable
    """
    
    def __init__(self):
        """Initialize a new game instance."""
        self.player = None
        self.is_running = False
        self.game_over_reason = None
        
    def start_new_game(self, player_name: str) -> bool:
        """
        Start a new game with the given player name.
        
        Args:
            player_name (str): Name for the new player
            
        Returns:
            bool: True if game started successfully, False otherwise
        """
        try:
            self.player = Player(player_name)
            self.is_running = True
            self.game_over_reason = None
            return True
        except Exception as e:
            print(f"Error starting new game: {e}")
            return False
            
    def load_game(self, save_data: dict) -> bool:
        """
        Load a game from save data.
        
        Args:
            save_data (dict): Dictionary containing saved game state
            
        Returns:
            bool: True if game loaded successfully, False otherwise
        """
        try:
            # Create player from save data
            self.player = Player(save_data['name'])
            self.player.hunger = save_data['hunger']
            self.player.thirst = save_data['thirst']
            self.player.energy = save_data['energy']
            self.player.days_survived = save_data['days_survived']
            self.player.is_alive = save_data['is_alive']
            
            self.is_running = True
            self.game_over_reason = None
            return True
        except Exception as e:
            print(f"Error loading game: {e}")
            return False
            
    def game_loop(self) -> str:
        """
        Main game loop - processes one complete day cycle.
        
        Returns:
            str: Status message or None if game continues
        """
        if not self.is_running or not self.player:
            return "Game not initialized"
            
        # Process daily evolution
        self.player.natural_evolution()
        
        # Check for victory condition FIRST (before death check)
        if self.check_victory():
            self.is_running = False
            self.game_over_reason = "Congratulations! You survived 30 days on the island!"
            return self.game_over_reason
            
        # Check for game over conditions
        if self.player.check_game_over():
            self.is_running = False
            self.game_over_reason = "You died from lack of vital resources!"
            return self.game_over_reason
            
        return None  # Game continues
        
    def process_day(self) -> dict:
        """
        Process a single day and return day summary.
        
        Returns:
            dict: Summary of the day's events and player status
        """
        if not self.player:
            return {"error": "No player initialized"}
            
        day_summary = {
            "day": self.player.days_survived,
            "player_status": self.player.get_status(),
            "events": [],
            "game_over": False,
            "victory": False
        }
        
        # Check game status after natural evolution
        if self.player.check_game_over():
            day_summary["game_over"] = True
            day_summary["game_over_reason"] = self.game_over_reason
            
        if self.check_victory():
            day_summary["victory"] = True
            
        return day_summary
        
    def check_victory(self) -> bool:
        """
        Check if the player has achieved victory (30 days survived).
        
        Returns:
            bool: True if player has won, False otherwise
        """
        return self.player and self.player.days_survived >= 30
        
    def end_game(self, reason: str = None):
        """
        End the current game.
        
        Args:
            reason (str): Optional reason for ending the game
        """
        self.is_running = False
        if reason:
            self.game_over_reason = reason
            
    def get_game_state(self) -> dict:
        """
        Get the current game state for saving.
        
        Returns:
            dict: Complete game state data
        """
        if not self.player:
            return {}
            
        return {
            "name": self.player.name,
            "hunger": self.player.hunger,
            "thirst": self.player.thirst,
            "energy": self.player.energy,
            "days_survived": self.player.days_survived,
            "is_alive": self.player.is_alive,
            "is_running": self.is_running,
            "game_over_reason": self.game_over_reason
        }
        
    def get_player(self) -> Player:
        """
        Get the current player instance.
        
        Returns:
            Player: Current player or None if no game active
        """
        return self.player
        
    def is_game_active(self) -> bool:
        """
        Check if the game is currently active.
        
        Returns:
            bool: True if game is running, False otherwise
        """
        return self.is_running and self.player and self.player.is_alive