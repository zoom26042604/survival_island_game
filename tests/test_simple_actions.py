"""
Simple test for ActionManager.
"""

import unittest


class MockPlayer:
    """Simple mock player."""
    def __init__(self):
        self.hunger = 50
        self.thirst = 50
        self.energy = 50
        
    def update_gauges(self, hunger_change=0, thirst_change=0, energy_change=0):
        self.hunger += hunger_change
        self.thirst += thirst_change
        self.energy += energy_change


# Import after mock to avoid circular imports
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.controllers.action_manager import ActionManager


class TestActionManager(unittest.TestCase):
    """Simple tests for ActionManager."""
    
    def test_fish_action(self):
        """Test fishing action."""
        manager = ActionManager()
        player = MockPlayer()
        
        result = manager.execute_fish_action(player)
        
        self.assertTrue(result)
        self.assertEqual(player.hunger, 30)  # 50 - 20
        self.assertEqual(player.energy, 35)  # 50 - 15
        
    def test_find_water_action(self):
        """Test find water action."""
        manager = ActionManager()
        player = MockPlayer()
        
        result = manager.execute_find_water_action(player)
        
        self.assertTrue(result)
        self.assertEqual(player.thirst, 35)  # 50 - 15
        self.assertEqual(player.energy, 40)  # 50 - 10
        
    def test_sleep_action(self):
        """Test sleep action."""
        manager = ActionManager()
        player = MockPlayer()
        
        result = manager.execute_sleep_action(player)
        
        self.assertTrue(result)
        self.assertEqual(player.energy, 80)  # 50 + 30 - should restore energy!
        self.assertEqual(player.hunger, 60)  # 50 + 10
        self.assertEqual(player.thirst, 55)  # 50 + 5


if __name__ == '__main__':
    unittest.main()