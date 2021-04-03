import pygame

class Ship():
    
    """
    Class for creating a ship object
    """
    
    def __init__(self, game_settings, screen):
        
        """
        Initialize the ship object and set its starting position
        """
        
        self.screen = screen
        self.game_settings = game_settings

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        
        # Movement Flag
        self.moving_right = False
        self.moving_left = False
        
    
    def update(self):
        
        """
        Update the movement flag for the ship class.
        """
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed

        # Update object from self.center
        self.rect.centerx = self.center
        
    def blitme(self):
        
        """
        Draw the ship at its current location
        """
        
        self.screen.blit(self.image, self.rect)