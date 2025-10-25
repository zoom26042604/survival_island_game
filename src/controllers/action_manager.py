"""
Action manager to handle player actions execution.
"""

from ..models.actions_library import ACTIONS, get_action


class ActionManager:
    """
    Manages all player actions and their execution.
    """
    
    def __init__(self):
        """Initialize the action manager."""
        self.available_actions = ACTIONS
    
    def get_available_actions(self, player):
        """
        Get list of actions available to the player.
        
        Args:
            player: Player instance
            
        Returns:
            list: List of available action names
        """
        # For now, all actions are always available
        available = []
        for action_name, action in self.available_actions.items():
            if action.can_execute(player):
                available.append(action_name)
        return available
    
    def execute_action(self, action_name, player):
        """
        Execute an action on the player.
        
        Args:
            action_name (str): Name of the action to execute
            player: Player instance
            
        Returns:
            bool: True if action was executed successfully
        """
        action = get_action(action_name)
        if action and action.can_execute(player):
            return action.execute(player)
        return False