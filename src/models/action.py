"""
Player actions module for the survival game.
Handles different actions that the player can perform.
"""

class Action:
    """
    Class representing an action that the player can perform.
    """
    
    def __init__(self, name, description, effects):
        """
        Initialize an action.
        
        Args:
            name (str): Action name
            description (str): Action description
            effects (dict): Effects on player gauges
        """
        self.name = name
        self.description = description
        self.effects = effects  # Dict with hunger_change, thirst_change, energy_change
    
    def execute(self, player):
        """
        Execute the action on the player.
        
        Args:
            player: Player instance
        """
        # Apply effects
        player.update_gauges(
            self.effects.get('hunger_change', 0),
            self.effects.get('thirst_change', 0),
            self.effects.get('energy_change', 0)
        )
        return True
    
    def can_execute(self, player):
        """
        Check if the action can be executed.
        
        Args:
            player: Player instance
            
        Returns:
            bool: True if the action can be executed
        """
        # For now, all actions are always possible
        return True