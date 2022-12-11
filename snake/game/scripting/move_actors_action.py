from game.scripting.action import Action

# TODO: Implement MoveActorsAction class here! 

class MoveActorsAction(Action):
    def __init__(self):
        super().__init__()

    # Override the execute(cast, script) method as follows:
    def execute(self, cast, script):
        """Get all the actors from the cast, loop through the actors, and move the actors. This method overrides the same method of the Action class.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # 1) get all the actors from the cast
        actors=cast.get_all_actors()
        # 2) loop through the actors
        for actor in actors:
            # 3) call the move_next() method on each actor
            actor.move_next()
        