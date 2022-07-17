import time

from pyray import get_time

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
        self._start = time.time()
        self._corner_reached = 0 
        self._first = True
        self._second = True
        self._thirth = True
        self._fourth = True
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open() and self._corner_reached != 4:
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
            self._get_time()
        # guardar en el archivo
        with open('dog_breeds_reversed.txt', 'w') as writer:
        # Alternatively you could use
        # writer.writelines(reversed(dog_breeds))

        # Write the dog breeds to the file in reversed order
            writer.write()



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
        banner_time = elements.get_first_object("banners_time")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        banner_time.set_text(self._get_time() + " corners visit: " + str(self._corner_reached))

        self._touched_one_corner(player.get_position())
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

    def _get_time(self):
        # start measuring time      
        # task to measure
        #l = [x for x in range(1000000)]
        # end measuring time
        end = time.time()
        # getting elapsed time
        seconds = int(end - self._start)
        #time_in_miliseconds = time_elapsed * 1000
        # printing information
        return "Seconds: "+str(seconds) 
    
    def _touched_one_corner(self, point):

        if(point.get_x()== 0 and point.get_y()== 0 and self._first):
            self._corner_reached +=1
            self._first = False
        elif(point.get_x()== 885 and point.get_y()== 0 and self._second):
            self._corner_reached +=1
            self._second = False
        elif(point.get_x()== 885 and point.get_y()== 585 and self._thirth):
            self._corner_reached +=1
            self._thirth = False
        elif(point.get_x()== 0 and point.get_y()== 585 and self._fourth):
            self._corner_reached +=1
            self._fourth = False
   
        