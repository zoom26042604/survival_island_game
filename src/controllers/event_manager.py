"""
EventManager class to handle random events in the survival game.
"""

import random
from typing import Dict, Any, Optional, List

from ..models.event import Event, EventType
from ..models.events_library import get_all_events


class EventManager:
    """
    Manages random events and their triggers in the survival game.
    """
    
    def __init__(self):
        """Initialize the EventManager with basic setup."""
        self.events = get_all_events()
        
    def trigger_daily_event(self, player):
        """Try to trigger a daily event."""
        # Simple random selection for now
        if random.random() < 0.5:  # 50% chance
            event = random.choice(self.events)
            result = event.apply_effects(player)
            
            # Handle choice events differently
            if result.get("requires_choice"):
                # For testing, auto-choose first option
                choices = list(result["choices"].keys())
                if choices:
                    choice = choices[0]  # Pick first choice for now
                    return event.apply_choice(player, choice)
            
            return result
        return None