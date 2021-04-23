class GameStats():
    """
    Track statistics for Alien Invasion
    """

    def __init__(self, game_settings):
        """
        Initialize statistics

        Args:
            game_settings ([type]): [description]
        """
        self.game_settings = game_settings
        self.reset_stats()

        # Start game in an inactice state
        self.game_active = False

        # High score
        self.high_score = 0 

    def reset_stats(self):
        """
        Intialize stats that can change during the game
        """
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1
        
        