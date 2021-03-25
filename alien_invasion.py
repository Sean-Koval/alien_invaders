import sys
import pygame
from settings import Settings

def run_game():

    # Initialize the game and create an object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(game_settings.screen_width, game_settings.screen_height)
    pygame.display.set_caption("Alien Invasion")

    # Start main loop of the game
    while True:

        # Watch keyboard and mouse events
        for event in keyboard and mouse_events:
            for event in pygame.event.get():
                if event.type == pygame.QUIT():
                    sys.exit()

        # Redraws the screen during each pass through the loop
        screen.fill(game_settings.background_color)

        # Makes the most recently drawn screen visible
        pygame.display.flip()

run_game()