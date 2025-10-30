"""
Predefined events for the survival island game.
"""

from .event import Event, EventType


def create_rain_event() -> Event:
    """
    Create a rain event.
    Rain reduces thirst by 15 points (good for the player).
    
    Returns:
        Event: Rain event instance
    """
    return Event(
        event_type=EventType.RAIN,
        name="Rain Storm",
        description="Heavy rain falls, providing fresh water to drink",
        effects={"thirst": -15},  # Reduces thirst (good)
        probability=0.20  # 20% chance
    )


def create_animal_event() -> Event:
    """
    Create an animal encounter event.
    Player can choose to flee (safe) or hunt (risky but rewarding).
    
    Returns:
        Event: Animal encounter event instance
    """
    return Event(
        event_type=EventType.ANIMAL,
        name="Wild Animal Encounter",
        description="You encounter a wild animal on the island",
        effects={},  # No direct effects, requires choice
        probability=0.15,  # 15% chance
        requires_choice=True,
        choices={
            "flee": {
                "description": "Run away safely (no risk, no reward)",
                "message": "You flee safely but gain nothing",
                "effects": {}  # No effects
            },
            "hunt": {
                "description": "Try to hunt the animal (risky but could provide food)",
                "message": "You attempt to hunt the animal",
                "effects": {}  # Effects determined by success/failure in EventManager
            }
        }
    )


def create_resource_event() -> Event:
    """
    Create a resource discovery event.
    Player can choose between food or water resource.
    
    Returns:
        Event: Resource discovery event instance
    """
    return Event(
        event_type=EventType.RESOURCE,
        name="Resource Discovery", 
        description="You discover useful resources on the island",
        effects={},  # No direct effects, requires choice
        probability=0.25,  # 25% chance
        requires_choice=True,
        choices={
            "food": {
                "description": "Collect food (berries, fruits)",
                "message": "You gather fresh berries and fruits",
                "effects": {"hunger": -10}  # Reduces hunger by 10
            },
            "water": {
                "description": "Collect water (from a stream or spring)",
                "message": "You find a fresh water source and drink",
                "effects": {"thirst": -10}  # Reduces thirst by 10
            }
        }
    )


def get_all_events() -> list[Event]:
    """
    Get all predefined events for the game.
    
    Returns:
        List of all available events
    """
    return [
        create_rain_event(),
        create_animal_event(),
        create_resource_event()
    ]


def get_events_by_type(event_type: EventType) -> list[Event]:
    """
    Get events filtered by type.
    
    Args:
        event_type (EventType): Type of events to filter
        
    Returns:
        List of events of the specified type
    """
    return [event for event in get_all_events() if event.event_type == event_type]