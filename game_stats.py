
class GameStats():
    """
    Track stats of the player
    """

    def __init__(self, game_settings):
        """
        Initialize stats
        """    
        self.game_settings = game_settings
        self.reset_stats()
        self.game_active = True
    
    def reset_stats(self):
        """
        Initialize stats that can change during the game
        """
        self.ships_left = self.game_settings.ship_limit