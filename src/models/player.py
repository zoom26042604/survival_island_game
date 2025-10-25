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
        # Initial gauge values (100 = full health)
        self.hunger = 100     # 100 = completely satisfied
        self.thirst = 100     # 100 = completely hydrated
        self.energy = 100     # 100 = full energy
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
        # Game over if any gauge reaches 0
        if self.hunger <= 0 or self.thirst <= 0 or self.energy <= 0:
            self.is_alive = False
            
    def natural_evolution(self):
        """
        Natural evolution of gauges each day.
        Gauges decrease naturally over time.
        """
        self.update_gauges(hunger_change=-5, thirst_change=-8, energy_change=-10)
        self.days_survived += 1
        
    def check_game_over(self) -> str:
        """
        Check game over conditions.
        
        Returns:
            str: Game over message if applicable, None if game continues
        """
        if not self.is_alive:
            return "Game Over: You died from lack of vital resources!"
        elif self.days_survived >= 30:
            return "Congratulations! You won by surviving 30 days on the island!"
        return None
        
    def get_status(self) -> str:
        """
        Return current player state as formatted string.
        
        Returns:
            str: Formatted status information
        """
        return f"""
{self.name} - Day {self.days_survived}
Hunger: {self.hunger}/100
Thirst: {self.thirst}/100
Energy: {self.energy}/100
Status: {'Alive' if self.is_alive else 'Dead'}
""".strip()
        
    def get_gauge_status(self, gauge_name: str) -> str:
        """
        Return specific gauge status as readable text.
        
        Args:
            gauge_name (str): Name of the gauge ('hunger', 'thirst', 'energy')
            
        Returns:
            str: Description of the gauge state
        """
        if gauge_name == "hunger":
            if self.hunger >= 80:
                return "Satisfied"
            elif self.hunger >= 60:
                return "Slightly hungry"
            elif self.hunger >= 30:
                return "Hungry"
            else:
                return "Starving"
        elif gauge_name == "thirst":
            if self.thirst >= 80:
                return "Hydrated"
            elif self.thirst >= 60:
                return "Slightly thirsty"
            elif self.thirst >= 30:
                return "Thirsty"
            else:
                return "Dehydrated"
        elif gauge_name == "energy":
            if self.energy >= 80:
                return "Energetic"
            elif self.energy >= 60:
                return "Slightly tired"
            elif self.energy >= 30:
                return "Tired"
            else:
                return "Exhausted"
        else:
            return "Unknown gauge"