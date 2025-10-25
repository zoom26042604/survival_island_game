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
    
    def __init__(self, daily_chance=0.6, exploration_chance=0.8):
        """Initialize the EventManager with configurable chances."""
        self.events = get_all_events()
        self.daily_chance = daily_chance
        self.exploration_chance = exploration_chance
        
    def trigger_daily_event(self, player):
        """Try to trigger a daily event."""
        if random.random() < self.daily_chance:
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
        
    def trigger_exploration_event(self, player):
        """Try to trigger an exploration event."""
        if random.random() < self.exploration_chance:
            event = random.choice(self.events)
            result = event.apply_effects(player)
            
            if result.get("requires_choice"):
                choices = list(result["choices"].keys())
                if choices:
                    # For exploration, maybe pick more risky choices
                    choice = choices[-1]  # Pick last choice (often riskier)
                    return event.apply_choice(player, choice)
            
            return result
        return None