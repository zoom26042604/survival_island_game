"""
Quick test script for EventManager - student testing
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.controllers.event_manager import EventManager
from src.models.player import Player


def test_basic_events():
    """Test if events work at all."""
    print("=== Testing EventManager ===")
    
    # Create manager and player
    manager = EventManager()
    player = Player("Test Player")
    
    print(f"Available events: {len(manager.events)}")
    print(f"Player initial state: {player.get_status()}")
    
    # Test daily events
    print("\n--- Testing Daily Events ---")
    for i in range(5):
        result = manager.trigger_daily_event(player)
        if result:
            print(f"Day {i+1}: {result}")
        else:
            print(f"Day {i+1}: No event occurred")
    
    print(f"\nPlayer final state: {player.get_status()}")

if __name__ == "__main__":
    test_basic_events()