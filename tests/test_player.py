"""Tests for the Player class."""

import unittest
import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.models.player import Player


class TestPlayer(unittest.TestCase):
    """Test cases for the Player class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.player = Player("Test Player")

    def test_player_initialization(self):
        """Test that a player is initialized correctly."""
        self.assertEqual(self.player.name, "Test Player")
        self.assertEqual(self.player.hunger, 100)
        self.assertEqual(self.player.thirst, 100)
        self.assertEqual(self.player.energy, 100)
        self.assertEqual(self.player.days_survived, 0)
        self.assertTrue(self.player.is_alive)

    def test_update_gauges(self):
        """Test updating player gauges."""
        self.player.update_gauges(hunger_change=-10, thirst_change=-5, energy_change=10)
        
        self.assertEqual(self.player.hunger, 90)
        self.assertEqual(self.player.thirst, 95)
        self.assertEqual(self.player.energy, 100)  # Clamped to max
        self.assertTrue(self.player.is_alive)

    def test_gauge_clamping(self):
        """Test that gauges are properly clamped between 0 and 100."""
        # Test upper bounds
        self.player.update_gauges(hunger_change=50, thirst_change=50, energy_change=50)
        self.assertEqual(self.player.hunger, 100)
        self.assertEqual(self.player.thirst, 100)
        self.assertEqual(self.player.energy, 100)

        # Test lower bounds
        self.player.update_gauges(hunger_change=-150, thirst_change=-150, energy_change=-150)
        self.assertEqual(self.player.hunger, 0)
        self.assertEqual(self.player.thirst, 0)
        self.assertEqual(self.player.energy, 0)

    def test_death_conditions(self):
        """Test that player dies when gauges reach zero."""
        # Test hunger death
        player_hunger = Player("Hungry Player")
        player_hunger.update_gauges(hunger_change=-100)
        self.assertFalse(player_hunger.is_alive)

        # Test thirst death
        player_thirst = Player("Thirsty Player")
        player_thirst.update_gauges(thirst_change=-100)
        self.assertFalse(player_thirst.is_alive)

        # Test energy death
        player_energy = Player("Tired Player")
        player_energy.update_gauges(energy_change=-100)
        self.assertFalse(player_energy.is_alive)

    def test_natural_evolution(self):
        """Test the natural evolution of gauges over time."""
        initial_hunger = self.player.hunger
        initial_thirst = self.player.thirst
        initial_energy = self.player.energy

        self.player.natural_evolution()

        # Gauges should decrease
        self.assertLess(self.player.hunger, initial_hunger)
        self.assertLess(self.player.thirst, initial_thirst)
        self.assertLess(self.player.energy, initial_energy)

        # Days survived should increase
        self.assertEqual(self.player.days_survived, 1)

    def test_check_game_over(self):
        """Test game over conditions."""
        # Player alive
        result = self.player.check_game_over()
        self.assertIsNone(result)

        # Player dead
        self.player.update_gauges(hunger_change=-100)
        result = self.player.check_game_over()
        self.assertIn("died", result.lower())

        # Player survives 30 days
        survivor = Player("Survivor")
        survivor.days_survived = 30
        result = survivor.check_game_over()
        self.assertIn("won", result.lower())

    def test_get_status(self):
        """Test the status string representation."""
        status = self.player.get_status()
        self.assertIn(self.player.name, status)
        self.assertIn("Day 0", status)
        self.assertIn("Hunger: 100", status)
        self.assertIn("Thirst: 100", status)
        self.assertIn("Energy: 100", status)

    def test_get_gauge_status(self):
        """Test individual gauge status descriptions."""
        # Test perfect health
        hunger_status = self.player.get_gauge_status("hunger")
        self.assertIn("Satisfied", hunger_status)

        # Test low health
        self.player.update_gauges(hunger_change=-80)
        hunger_status = self.player.get_gauge_status("hunger")
        self.assertIn("Starving", hunger_status)

    def test_string_representations(self):
        """Test __str__ and __repr__ methods."""
        str_repr = str(self.player)
        self.assertIn("Test Player", str_repr)
        
        repr_str = repr(self.player)
        self.assertIn("Player", repr_str)
        self.assertIn("Test Player", repr_str)


if __name__ == "__main__":
    unittest.main()