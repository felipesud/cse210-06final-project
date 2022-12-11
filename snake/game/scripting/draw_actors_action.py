from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.handle_collisions_action import HandleCollisionsAction
import constants

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        scores=cast.get_actors("scores")
        score1 = scores[0]
        scores[1].set_position(Point(constants.MAX_X-constants.COLUMNS*2, 0))
        score2 = scores[1]
        foods = cast.get_actors("foods")
        snakes = cast.get_actors("snake")
        self._video_service.clear_buffer()
        for snake in snakes:
            segments = snake.get_segments()
            messages = cast.get_actors("messages")
            self._video_service.draw_actors(segments)
            self._video_service.draw_actor(score1,color='G')
            self._video_service.draw_actor(score2,color='R')
            self._video_service.draw_actors(messages, True)
            self._video_service.draw_actors(foods,color='RANDOM')
        self._video_service.flush_buffer()