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
    
    def update_gauges(self, hunger_change: int = 0, thirst_change: int = 0, energy_change: int = 0):
        """
        Update player's vital gauges.
        
        Args:
            hunger_change (int): Change in hunger (+increases, -decreases)
            thirst_change (int): Change in thirst (+increases, -decreases)
            energy_change (int): Change in energy (+increases, -decreases)
        """
        self.hunger += hunger_change
        self.thirst += thirst_change
        self.energy += energy_change
        
        # Keep gauges within 0-100 limits
        self._clamp_gauges()
        
        # Check if player is still alive
        self._update_alive_status()
        
    def _clamp_gauges(self):
        """Keep gauges within 0-100 limits."""
        self.hunger = max(0, min(100, self.hunger))
        self.thirst = max(0, min(100, self.thirst))
        self.energy = max(0, min(100, self.energy))
        
    def _update_alive_status(self):
        """Update player's alive/dead status."""
        # Game over if hunger or thirst >= 100, or energy <= 0
        if self.hunger >= 100 or self.thirst >= 100 or self.energy <= 0:
            self.is_alive = False
            
    def natural_evolution(self):
        """
        Natural evolution of gauges each day.
        According to specs: Hunger +5, Thirst +3, Energy -10
        """
        self.update_gauges(hunger_change=5, thirst_change=3, energy_change=-10)
        self.days_survived += 1
        
    def check_game_over(self) -> bool:
        """
        Check if the player is dead.
        
        Returns:
            bool: True if player is dead, False if alive
        """
        return not self.is_alive