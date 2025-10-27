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
    


##########################################################################
#####                   Action Setters and Getters                    ####
##########################################################################
    def getName(self):
        """Get the name of the action."""
        return self.name

    def getDescription(self):
        """Get the description of the action."""
        return self.description

    def getEffects(self):
        """Get the effects of the action."""
        return self.effects
    
    def setName(self, name):
        """Set the name of the action."""
        self.name = name

    def setDescription(self, description):
        """Set the description of the action."""
        self.description = description

    def setEffects(self, effects):
        """Set the effects of the action."""
        self.effects = effects
