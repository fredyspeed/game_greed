import os
import random


from game.casting.player import Player
from game.casting.player_static import PlayerStatic
from game.casting.elements import Elements

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
        self.__CAPTION = "EAT-TIME"
        self.__points = 0


    def start_elements(self):
    
        # create the cast
        elements = Elements()
        
        # create the banner
        banner = Player()
        banner.set_text("")
        banner.set_font_size(self.FONT_SIZE)
        banner.set_color(self.WHITE)
        banner.set_position(Point(self.CELL_SIZE, 0))
        elements.add_object("banners", banner)

        banner_time = Player()
        banner_time.set_text("")
        banner_time.set_font_size(self.FONT_SIZE)
        banner_time.set_color(self.WHITE)
        banner_time.set_position(Point(self.CELL_SIZE * 5, 0))
        elements.add_object("banners_time", banner_time)
        
        # create the player
        x = int(self.MAX_X / 2)
        y = int(self.MAX_Y / 2)
        position = Point(x, y)

        player = Player()
        player.set_text("#")
        player.set_font_size(self.FONT_SIZE)
        player.set_color(self.WHITE)
        player.set_position(position)
        elements.add_object("robots", player)
        

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
            
            player_static = PlayerStatic()
            player_static.set_text(text)
            player_static.set_font_size(self.FONT_SIZE)
            player_static.set_color(color)
            player_static.set_position(position)
            player_static.set_message(message)
            elements.add_object("artifacts", player_static)
    
    # start the game

        keyboard_service = KeyboardService(self.CELL_SIZE)
        video_service = VideoService(self.__CAPTION, self.MAX_X, self.MAX_Y, self.CELL_SIZE, self.FRAME_RATE)
        director = Director(keyboard_service, video_service)
        director.start_game(elements)


    
