from game.casting.object_in_board  import ObjectInBoard
from game.shared.point import Point

class Player(ObjectInBoard):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._velocity = Point(0, 0)
        self._message = ""
        self._points = 0

    def move_next(self, max_x, max_y):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)

        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity
    
    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def get_points(self):
        """Gets the point that the artefact contains.
        
        Returns:
            int: The number of points accumulated.
        """
        return self._points
    
    def set_points(self, points_add):
        """Updates the points to add or rest of the score save in points
        Args:
            point_add (int): contains value positive if touch a Gem or negative 
            if touch a Rock        
        """
        self._points += points_add