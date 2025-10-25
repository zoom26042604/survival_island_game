"""
Action manager to handle player actions execution.
"""

class ActionManager:
    """
    Manages all player actions and their execution.
    """
    
    def __init__(self):
        """Initialize the action manager."""
        # Just hardcode actions for now - simple approach
        pass
    
    def execute_fish_action(self, player):
        """Execute fish action."""
        player.update_gauges(hunger_change=-20, energy_change=-15)
        return True
        
    def execute_sleep_action(self, player):
        """Execute sleep action."""
        # Oops! Wrong sign on energy - typical student mistake!
        player.update_gauges(energy_change=-30, hunger_change=10, thirst_change=5)
        return True
        
    def execute_find_water_action(self, player):
        """Execute find water action."""
        player.update_gauges(thirst_change=-15, energy_change=-10)
        return True