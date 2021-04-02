import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    Class to manage bullets fired from the ship.

    Args:
        Sprite ([type]): [description]
    """
    def __init__(self, game_settings, screen, ship):
        """
        Create bullet object at ship's current position

        Args:
            game_settings ([type]): [description]
            screen ([type]): [description]
            ship ([type]): [description]
        """
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height):
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top 

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor