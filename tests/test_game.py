"""Tests for the Game class."""

import unittest
import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.controllers.game import Game
from src.models.player import Player


class TestGame(unittest.TestCase):
    """Test cases for the Game class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.game = Game()

    def test_game_initialization(self):
        """Test that a game is initialized correctly."""
        self.assertIsNone(self.game.player)
        self.assertFalse(self.game.is_running)
        self.assertIsNone(self.game.game_over_reason)

    def test_start_new_game(self):
        """Test starting a new game."""
        result = self.game.start_new_game("Test Player")
        
        self.assertTrue(result)
        self.assertIsNotNone(self.game.player)
        self.assertEqual(self.game.player.name, "Test Player")
        self.assertTrue(self.game.is_running)
        self.assertIsNone(self.game.game_over_reason)

    def test_load_game(self):
        """Test loading a game from save data."""
        save_data = {
            "name": "Loaded Player",
            "hunger": 80,
            "thirst": 60,
            "energy": 90,
            "days_survived": 5,
            "is_alive": True
        }
        
        result = self.game.load_game(save_data)
        
        self.assertTrue(result)
        self.assertIsNotNone(self.game.player)
        self.assertEqual(self.game.player.name, "Loaded Player")
        self.assertEqual(self.game.player.hunger, 80)
        self.assertEqual(self.game.player.thirst, 60)
        self.assertEqual(self.game.player.energy, 90)
        self.assertEqual(self.game.player.days_survived, 5)
        self.assertTrue(self.game.is_running)

    def test_load_game_invalid_data(self):
        """Test loading game with invalid save data."""
        invalid_data = {"name": "Test"}  # Missing required fields
        
        result = self.game.load_game(invalid_data)
        self.assertFalse(result)

    def test_check_victory(self):
        """Test victory condition checking."""
        self.game.start_new_game("Victor")
        
        # Not victory yet
        self.assertFalse(self.game.check_victory())
        
        # Set to 30 days
        self.game.player.days_survived = 30
        self.assertTrue(self.game.check_victory())

    def test_end_game(self):
        """Test ending a game."""
        self.game.start_new_game("Test Player")
        self.assertTrue(self.game.is_running)
        
        self.game.end_game("Test reason")
        
        self.assertFalse(self.game.is_running)
        self.assertEqual(self.game.game_over_reason, "Test reason")

    def test_get_game_state(self):
        """Test getting game state for saving."""
        self.game.start_new_game("State Player")
        
        state = self.game.get_game_state()
        
        self.assertEqual(state["name"], "State Player")
        self.assertEqual(state["hunger"], 100)
        self.assertEqual(state["thirst"], 100)
        self.assertEqual(state["energy"], 100)
        self.assertEqual(state["days_survived"], 0)
        self.assertTrue(state["is_alive"])
        self.assertTrue(state["is_running"])

    def test_get_game_state_no_player(self):
        """Test getting game state with no player."""
        state = self.game.get_game_state()
        self.assertEqual(state, {})

    def test_get_player(self):
        """Test getting current player."""
        self.assertIsNone(self.game.get_player())
        
        self.game.start_new_game("Test Player")
        player = self.game.get_player()
        
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Test Player")

    def test_is_game_active(self):
        """Test checking if game is active."""
        self.assertFalse(self.game.is_game_active())
        
        self.game.start_new_game("Active Player")
        self.assertTrue(self.game.is_game_active())
        
        # Kill player
        self.game.player.update_gauges(energy_change=-100)
        self.assertFalse(self.game.is_game_active())

    def test_process_day(self):
        """Test processing a single day."""
        self.game.start_new_game("Day Player")
        
        day_summary = self.game.process_day()
        
        self.assertIn("day", day_summary)
        self.assertIn("player_status", day_summary)
        self.assertIn("events", day_summary)
        self.assertIn("game_over", day_summary)
        self.assertIn("victory", day_summary)

    def test_game_loop_death(self):
        """Test game loop with player death."""
        self.game.start_new_game("Dying Player")
        
        # Drain energy to kill player
        self.game.player.update_gauges(energy_change=-100)
        
        result = self.game.game_loop()
        
        self.assertIsNotNone(result)
        self.assertIn("died", result.lower())
        self.assertFalse(self.game.is_running)

    def test_game_loop_victory(self):
        """Test game loop with victory condition."""
        self.game.start_new_game("Winner")
        
        # Set to 29 days and ensure player has enough resources
        self.game.player.days_survived = 29
        self.game.player.hunger = 90
        self.game.player.thirst = 90
        self.game.player.energy = 50  # Enough to survive one more day
        
        result = self.game.game_loop()
        
        self.assertIsNotNone(result)
        self.assertIn("survived", result.lower())
        self.assertFalse(self.game.is_running)


if __name__ == "__main__":
    unittest.main()