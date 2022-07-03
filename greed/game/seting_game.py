import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

class GameSettings:
    FRAME_RATE = 12
    MAX_X = 900
    MAX_Y = 600
    CELL_SIZE = 15
    FONT_SIZE = 15
    COLS = 60
    ROWS = 40
    WHITE = Color(255, 255, 255)
    DEFAULT_ARTIFACTS = 40


    def __init__(self):
        """Constructs a new."""
        self.__CAPTION = "Game Greed"
        self.__points = 0


    def start_elements(self):
    
        # create the cast
        cast = Cast()
        
        # create the banner
        banner = Actor()
        banner.set_text("")
        banner.set_font_size(self.FONT_SIZE)
        banner.set_color(self.WHITE)
        banner.set_position(Point(self.CELL_SIZE, 0))
        cast.add_actor("banners", banner)
        
        # create the robot
        x = int(self.MAX_X / 2)
        y = int(self.MAX_Y / 2)
        position = Point(x, y)

        robot = Actor()
        robot.set_text("#")
        robot.set_font_size(self.FONT_SIZE)
        robot.set_color(self.WHITE)
        robot.set_position(position)
        cast.add_actor("robots", robot)
        

        for n in range(self.DEFAULT_ARTIFACTS):
            char_object = [79,42,79]
            number_char = random.randint(0,2)
            text = chr(char_object[number_char])
            if (char_object[number_char] == 79):
                message = "Rock"
            else:
                message = "Gem"

            x = random.randint(1, self.COLS - 1)
            y = random.randint(1, self.ROWS - 1)
            position = Point(x, y)
            position = position.scale(self.CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(self.FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)
            artifact.set_message(message)
            cast.add_actor("artifacts", artifact)
    
    # start the game

        keyboard_service = KeyboardService(self.CELL_SIZE)
        video_service = VideoService(self.__CAPTION, self.MAX_X, self.MAX_Y, self.CELL_SIZE, self.FRAME_RATE)
        director = Director(keyboard_service, video_service)
        director.start_game(cast)
