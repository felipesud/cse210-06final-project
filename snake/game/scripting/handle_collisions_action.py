import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
import pyray

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
        __winnerr (string): A string of text, representing who has won the game.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner=''

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        scores = cast.get_actors("scores")
        score1 = scores[0]
        score2 = scores[1]
        foods = cast.get_actors("foods")
        snakes = cast.get_actors("snake")
        for snake in snakes:
            for food in foods:
                if snakes[0].get_head().get_position().equals(food.get_position()):
                    points = food.get_points()
                    snakes[0].grow_tail(points)
                    score1.add_points(points)
                    food.reset()
                elif snakes[1].get_head().get_position().equals(food.get_position()):
                    points = food.get_points()
                    snakes[1].grow_tail(points)
                    score2.add_points(points)
                    food.reset()

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snakes = cast.get_actors("snake")
        for i in range(len(snakes)):
            head = snakes[i].get_segments()[0]
            segments0 = snakes[0].get_segments()[1:]
            segments1 = snakes[1].get_segments()[1:]
            segment0 = snakes[0].get_segments()[1:]
            segment1 = snakes[1].get_segments()[1:]


            value=abs(len(segments0)-len(segments1))
            if len(segments0)>=len(segments1):
                for segment in range(len(segments0)-value):
                    if snakes[0].get_segments()[0].get_position().equals(segment1[segment].get_position()):
                        self._is_game_over = True
                        self._winner='GREEN SNAKE WINNER'
                for segment in range(len(segments1)+value):
                    if snakes[1].get_segments()[0].get_position().equals(segment0[segment].get_position()):
                        self._is_game_over = True
                        self._winner='RED SNAKE WINNER'
            elif len(segments0)<len(segments1):
                for segment in range(len(segments0)+value):
                    if snakes[0].get_segments()[0].get_position().equals(segment1[segment].get_position()):
                        self._is_game_over = True
                        self._winner='GREEN SNAKE WINNER'
                for segment in range(len(segments1)-value):
                    if snakes[1].get_segments()[0].get_position().equals(segment0[segment].get_position()):
                        self._is_game_over = True
                        self._winner='RED SNAKE WINNER'
                    
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snake")
            segments = snake.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)
            snakes = cast.get_actors("snake")

            message = Actor()
            if self._winner=='RED SNAKE WINNER':
                message.set_color(constants.RED)
            else:
                message.set_color(constants.GREEN)

            message.set_text(f"Game Over! {self._winner}")
            message.set_position(position)
            cast.add_actor("messages", message)
            for snake in snakes:
                segments = snake.get_segments()
                for segment in segments:
                    segment.set_color(constants.WHITE)
            food.set_color(constants.WHITE)