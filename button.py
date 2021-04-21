import pygame.font 

class Button():

    def __init__(self, game_settings, screen, msg):
        """
        Initialize button attributes

        Args:
            game_settings ([type]): [description]
            screen ([type]): [description]
            msg ([type]): [description]
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)