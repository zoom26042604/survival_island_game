"""
Player class to manage player state in the survival game.
"""


class Player:
    """
    Represents a player with their vital gauges.
    
    Attributes:
        name (str): Player's name
        hunger (int): Hunger level (0-100, 100 = starving)
        thirst (int): Thirst level (0-100, 100 = dehydrated)  
        energy (int): Energy level (0-100, 0 = exhausted)
        days_survived (int): Number of days survived
        is_alive (bool): Player status (alive/dead)
    """
    
    def __init__(self, name: str):
        """
        Initialize a new player with default gauge values.
        
        Args:
            name (str): Player's name
        """
        self.name = name
        # Initial gauge values (according to specifications)
        self.hunger = 30      # 30% hunger at start
        self.thirst = 20      # 20% thirst at start  
        self.energy = 80      # 80% energy at start
        self.days_survived = 0
        self.is_alive = True
        
    def __str__(self):
        """String representation of player."""
        return f"Player: {self.name} (Day {self.days_survived + 1})"
        
    def __repr__(self):
        """Debug representation."""
        return f"Player(name='{self.name}', hunger={self.hunger}, thirst={self.thirst}, energy={self.energy})"