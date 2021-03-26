import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    # Initialize the game and create an object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(game_settings.screen_width, game_settings.screen_height)
    pygame.display.set_caption("Alien Invasion")

    # Make the ship
    ship = Ship(screen)

    # Start main loop of the game
    while True:

        # Watch keyboard and mouse events
        gf.check_events(ship)

        # Redraws the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship)

run_game()