"""
Tests for the Action class and actions library.
"""

import unittest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from models.action import Action
from models.actions_library import ACTIONS, get_action


class MockPlayer:
    """Mock player for testing actions."""
    
    def __init__(self):
        self.hunger = 50
        self.thirst = 50  
        self.energy = 50
        self.updates = []
        
    def update_gauges(self, hunger_change=0, thirst_change=0, energy_change=0):
        """Mock update_gauges method."""
        self.hunger += hunger_change
        self.thirst += thirst_change
        self.energy += energy_change
        self.updates.append((hunger_change, thirst_change, energy_change))


class TestAction(unittest.TestCase):
    """Test cases for Action class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.player = MockPlayer()
        self.action = Action(
            name="Test Action",
            description="A test action", 
            effects={'hunger_change': -10, 'energy_change': -5}
        )
    
    def test_action_creation(self):
        """Test action creation."""
        self.assertEqual(self.action.name, "Test Action")
        self.assertEqual(self.action.description, "A test action")
        self.assertEqual(self.action.effects['hunger_change'], -10)
        self.assertEqual(self.action.effects['energy_change'], -5)
    
    def test_action_execute(self):
        """Test action execution."""
        result = self.action.execute(self.player)
        
        self.assertTrue(result)
        self.assertEqual(self.player.hunger, 40)  # 50 + (-10)
        self.assertEqual(self.player.energy, 45)  # 50 + (-5) 
        self.assertEqual(self.player.thirst, 50)  # unchanged
        
    def test_can_execute(self):
        """Test action validation."""
        self.assertTrue(self.action.can_execute(self.player))


class TestActionsLibrary(unittest.TestCase):
    """Test cases for actions library."""
    
    def test_actions_exist(self):
        """Test that expected actions exist."""
        self.assertIn('fish', ACTIONS)
        self.assertIn('find_water', ACTIONS)
        self.assertIn('sleep', ACTIONS)
        self.assertIn('explore', ACTIONS)
    
    def test_get_action(self):
        """Test getting actions by name."""
        fish_action = get_action('fish')
        self.assertIsNotNone(fish_action)
        self.assertEqual(fish_action.name, "Fish")
        
        invalid_action = get_action('invalid')
        self.assertIsNone(invalid_action)
    
    def test_fish_action(self):
        """Test fish action effects."""
        player = MockPlayer()
        fish = get_action('fish')
        
        fish.execute(player)
        
        self.assertEqual(player.hunger, 30)  # 50 + (-20)
        self.assertEqual(player.energy, 35)  # 50 + (-15)
        self.assertEqual(player.thirst, 50)  # unchanged


if __name__ == '__main__':
    unittest.main()