"""
Action manager to handle player actions execution.
"""

from ..models.action import Action


class ActionManager:
    """
    Manages all player actions and their execution.
    """
    def __init__(self, actions : list[Action] = []):
        """
        Initialize the action manager with available actions.
        
        Args:
            actions (list): List of Action instances
        """
        self.actions = actions

    def __init__(self):
        """Initialize ActionManager with default actions if none are provided."""
        self.setDefaultActions()



    def setDefaultActions(self):
        """Set default actions."""
        self.actions = {
            'fish': Action(
                name='Fish',
                description='Catch fish to reduce hunger.',
                effects={'hunger_change': 20, 'energy_change': -15}
            ),
            'sleep': Action(
                name='Sleep',
                description='Rest to restore energy.',
                effects={'energy_change': 30, 'hunger_change': 10, 'thirst_change': 5}
            ),
            'find_water': Action(
                name='Find Water',
                description='Locate water to reduce thirst.',
                effects={'thirst_change': 15, 'energy_change': -10}
            )
        }
    
    def get_actions_desc(self):
        """Get descriptions of all available actions."""
        return {name: action.description for name, action in self.actions.items()}

    def execute_fish_action(self, player):
        """Execute fish action."""
        self.actions['fish'].execute(player)
        #player.update_gauges(hunger_change=-20, energy_change=-15)
        return True
        
    def execute_sleep_action(self, player):
        """Execute sleep action."""
        self.actions['sleep'].execute(player)
        # Fixed! Sleep should RESTORE energy, not drain it!
        return True
        
    def execute_find_water_action(self, player):
        """Execute find water action."""
        self.actions['find_water'].execute(player)
        #player.update_gauges(thirst_change=-15, energy_change=-10)
        return True