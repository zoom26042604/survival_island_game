"""Tests for EventManager class."""

import unittest
import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.controllers.event_manager import EventManager
from src.models.player import Player
from src.models.event import Event, EventType


class TestEventManager(unittest.TestCase):
    """Test cases for the EventManager class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.manager = EventManager()
        self.player = Player("Test Player")

    def test_manager_initialization(self):
        """Test that EventManager initializes correctly."""
        self.assertEqual(len(self.manager.events), 3)  # Rain, Animal, Resource
        self.assertEqual(self.manager.daily_chance, 0.6)
        self.assertEqual(self.manager.exploration_chance, 0.8)

    def test_custom_chances(self):
        """Test EventManager with custom event chances."""
        custom_manager = EventManager(daily_chance=0.3, exploration_chance=0.9)
        self.assertEqual(custom_manager.daily_chance, 0.3)
        self.assertEqual(custom_manager.exploration_chance, 0.9)

    def test_daily_event_can_occur(self):
        """Test that daily events can be triggered."""
        # Test multiple times to check for randomness
        event_occurred = False
        for _ in range(20):  # Try 20 times
            result = self.manager.trigger_daily_event(self.player)
            if result is not None:
                event_occurred = True
                break
        
        self.assertTrue(event_occurred, "Daily event should occur at least once in 20 tries")

    def test_exploration_event_can_occur(self):
        """Test that exploration events can be triggered."""
        # Test multiple times to check for randomness
        event_occurred = False
        for _ in range(20):  # Try 20 times
            result = self.manager.trigger_exploration_event(self.player)
            if result is not None:
                event_occurred = True
                break
        
        self.assertTrue(event_occurred, "Exploration event should occur at least once in 20 tries")

    def test_event_effects_applied(self):
        """Test that events actually affect the player."""
        # Try many events to ensure we get one that changes stats
        stats_changed = False
        
        for _ in range(100):  # Try 100 times to get a stat-changing event
            initial_hunger = self.player.hunger
            initial_thirst = self.player.thirst
            initial_energy = self.player.energy
            
            result = self.manager.trigger_daily_event(self.player)
            if result and result.get("success"):
                final_hunger = self.player.hunger
                final_thirst = self.player.thirst  
                final_energy = self.player.energy
                
                # Check if this event changed something
                if (initial_hunger != final_hunger or
                    initial_thirst != final_thirst or
                    initial_energy != final_energy):
                    stats_changed = True
                    break
                    
        self.assertTrue(stats_changed, "At least one event should change player stats")


if __name__ == "__main__":
    unittest.main()