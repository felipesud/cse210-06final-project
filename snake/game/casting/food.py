from email import charset
import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Food(Actor):
    """
    A tasty item that snake like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self._points = 0
        if random.random()>0.5:
            self.set_velocity(Point(random.choice([-3,3]),random.choice([-3,3])))
        self.set_text(chr(random.randint(33, 126)))
        self.reset()
        
    def reset(self):
        """Selects a random position and points that the food is worth."""
        self._points = random.randint(1, 8)
        x = random.randint(1, constants.COLUMNS*2 - 1)
        y = random.randint(1, constants.ROWS*2 - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        
    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        return self._points