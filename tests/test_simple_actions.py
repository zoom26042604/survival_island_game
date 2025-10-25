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
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from controllers.action_manager import ActionManager


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


if __name__ == '__main__':
    unittest.main()