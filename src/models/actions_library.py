"""
Action library with predefined actions for the survival game.
"""

from .action import Action


# Define all available actions
ACTIONS = {
    'fish': Action(
        name="Fish",
        description="Try to catch fish to reduce hunger",
        effects={'hunger_change': -20, 'energy_change': -15}
    ),
    
    'find_water': Action(
        name="Find Water", 
        description="Look for fresh water to drink",
        effects={'thirst_change': -15, 'energy_change': -10}
    ),
    
    'sleep': Action(
        name="Sleep",
        description="Rest to recover energy", 
        effects={'energy_change': +30, 'hunger_change': +10, 'thirst_change': +5}
    ),
    
    'explore': Action(
        name="Explore",
        description="Explore the island for resources",
        effects={'energy_change': -20}  # Exploration will trigger events separately
    )
}


def get_action(action_name):
    """
    Get an action by name.
    
    Args:
        action_name (str): Name of the action
        
    Returns:
        Action: The requested action or None if not found
    """
    return ACTIONS.get(action_name)