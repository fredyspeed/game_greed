

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._positionX = 0
        self._positionY = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, objects):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            objects (Elements): The Elements of objects  (ObjectInBoard).
        """
        player = objects.get_first_object("robots")
        point_now = player.get_position()
        self._positionX = point_now.get_x()
        self._positionY = point_now.get_y()
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates(self, elements):
        """Updates the player's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = elements.get_first_object("banners")
        player = elements.get_first_object("robots")
        playerstatics = elements.get_objects("artifacts")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        for playerstatic in playerstatics:
            if player.get_position().equals(playerstatic.get_position()):
                message = playerstatic.get_message()
                if message == "Gem":
                    player.set_points(+50)
                elif(message == "Rock"):
                    player.set_points(-50)
                 
                elements.remove_object("artifacts",playerstatic) 
                #elements.change_positions("artifacts")

            result = str(player.get_points())
            banner.set_text(result)
        
    def _do_outputs(self, elements):
        """Draws the objects on the screen.
        
        Args:
            elements (Elements): The cast of actors.
        """
        self._video_service.clear_buffer()
        objects = elements.get_all_objects()
        self._video_service.draw_actors(objects)
        self._video_service.flush_buffer()

   
        