"""
Event class to represent random events in the survival game.
"""

from enum import Enum
from typing import Dict, Any, Optional
import random


class EventType(Enum):
    """Types of events that can occur in the game."""
    RAIN = "rain"
    ANIMAL = "animal" 
    RESOURCE = "resource"


class EventOutcome(Enum):
    """Possible outcomes for events that require player choice."""
    FLEE = "flee"
    HUNT = "hunt"
    FOOD = "food"
    WATER = "water"


class Event:
    """
    Represents a random event that can affect the player.
    
    Attributes:
        event_type (EventType): Type of the event
        name (str): Display name of the event
        description (str): Description of what happens
        effects (Dict[str, int]): Effects on player gauges
        requires_choice (bool): Whether event requires player input
        choices (Dict[str, Any]): Available choices and their outcomes
        probability (float): Chance of this event occurring (0.0-1.0)
    """
    
    def __init__(self, event_type: EventType, name: str, description: str, 
                 effects: Dict[str, int], probability: float = 0.0,
                 requires_choice: bool = False, choices: Optional[Dict[str, Any]] = None):
        """
        Initialize a new event.
        
        Args:
            event_type (EventType): Type of the event
            name (str): Display name of the event
            description (str): Description of what happens
            effects (Dict[str, int]): Effects on player gauges
            probability (float): Chance of this event occurring
            requires_choice (bool): Whether event requires player input
            choices (Dict[str, Any]): Available choices and their outcomes
        """
        self.event_type = event_type
        self.name = name
        self.description = description
        self.effects = effects.copy()
        self.probability = probability
        self.requires_choice = requires_choice
        self.choices = choices.copy() if choices else {}
        
    def __str__(self):
        """String representation of the event."""
        return f"{self.name}: {self.description}"
        
    def __repr__(self):
        """Debug representation of the event."""
        return f"Event(type={self.event_type.value}, name='{self.name}', probability={self.probability})"
        
    def apply_effects(self, player) -> Dict[str, Any]:
        """
        Apply the event's effects to a player.
        
        Args:
            player: Player instance to affect
            
        Returns:
            Dict with event results and effect summary
        """
        if self.requires_choice:
            return {
                "success": False,
                "message": "Event requires player choice",
                "requires_choice": True,
                "choices": self.choices,
                "effects_applied": {}
            }
            
        # Apply direct effects
        effects_applied = {}
        for stat, change in self.effects.items():
            if hasattr(player, stat):
                old_value = getattr(player, stat)
                player.update_gauges(**{f"{stat}_change": change})
                new_value = getattr(player, stat)
                effects_applied[stat] = {
                    "old": old_value,
                    "change": change,
                    "new": new_value
                }
                
        return {
            "success": True,
            "message": f"{self.name} occurred! {self.description}",
            "requires_choice": False,
            "effects_applied": effects_applied
        }
        
    def apply_choice(self, player, choice: str) -> Dict[str, Any]:
        """
        Apply the effects of a player's choice for this event.
        
        Args:
            player: Player instance to affect
            choice (str): Player's choice
            
        Returns:
            Dict with choice results and effect summary
        """
        if not self.requires_choice:
            return {
                "success": False,
                "message": "This event does not require a choice"
            }
            
        if choice not in self.choices:
            return {
                "success": False,
                "message": f"Invalid choice '{choice}'. Available: {list(self.choices.keys())}"
            }
            
        choice_data = self.choices[choice]
        effects = choice_data.get("effects", {})
        
        # Apply choice effects
        effects_applied = {}
        for stat, change in effects.items():
            if hasattr(player, stat):
                old_value = getattr(player, stat)
                player.update_gauges(**{f"{stat}_change": change})
                new_value = getattr(player, stat)
                effects_applied[stat] = {
                    "old": old_value,
                    "change": change,
                    "new": new_value
                }
                
        return {
            "success": True,
            "message": choice_data.get("message", f"You chose to {choice}"),
            "choice": choice,
            "effects_applied": effects_applied
        }
        
    def get_choice_descriptions(self) -> Dict[str, str]:
        """
        Get descriptions of available choices.
        
        Returns:
            Dict mapping choice keys to their descriptions
        """
        if not self.requires_choice:
            return {}
            
        return {
            choice: data.get("description", f"Choose {choice}")
            for choice, data in self.choices.items()
        }
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert event to dictionary representation.
        
        Returns:
            Dict representation of the event
        """
        return {
            "event_type": self.event_type.value,
            "name": self.name,
            "description": self.description,
            "effects": self.effects,
            "probability": self.probability,
            "requires_choice": self.requires_choice,
            "choices": self.choices
        }