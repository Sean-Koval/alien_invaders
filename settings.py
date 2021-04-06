
class Settings():
    
    """
    Class that stores all setting for Alien Invasion
    """

    def __init__(self):
        
        """
        Initialize the games's settings
        """

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)
        
        # Ship speed
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5
        
        # Alien Settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
    

    
    
        

        