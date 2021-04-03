import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    
    """
    Class to represent a single alien
    """
    
    def __init__(self, game_settings, screen):
        
        """
        Initialize the alien and set its starting point
        """
        
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        
        # Load the alien image an set its rect attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the aliens exact position
        self.x = float(self.rect.x)
        
    def blitme(self):
        """
        Draw the alien at its current location
        """
        self.screen.blit(self.image, self.rect)