from game.shared.color import Color
from game.shared.point import Point


class ObjectInBoard:
    """ This is an object within of board, this have the most general 
    attrubute in the game
    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
    """

    def __init__(self):
        """Constructs a new instance of ObjectInBoard.

        Args:
            self (ObjectInBoard): An instance of ObjectInBorard.
        """
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        

    def get_color(self):
        """Gets the color as Object Color that is in the directorie shared .
        
        Returns:
            Color: The color that the object will have.
        """
        return self._color

    def get_font_size(self):
        """Gets the actor's font size.
        
        Returns:
            Point: The actor's font size.
        """
        return self._font_size

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text

    

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_font_size(self, font_size):
        """Updates the font size to the given one.
        
        Args:
            font_size (int): The given font size.
        """
        self._font_size = font_size
    
    def set_text(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    