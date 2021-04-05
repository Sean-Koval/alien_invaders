import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    # Initialize the game and create an object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the ship
    ship = Ship(game_settings, screen)
    # Make a group to store bullets in
    bullets = Group()
    # Make aliens
    aliens = Group()
    
    # Create fleet of aliens
    gf.create_fleet(game_settings, screen, ship, aliens)    
    # Start main loop of the game
    while True:

        # Watch keyboard and mouse events
        gf.check_events(game_settings, screen, ship, aliens, bullets)
        ship.update()

        gf.update_bullets(aliens, bullets)
        gf.update_aliens(game_settings, aliens)

        # Redraws the screen during each pass through the loop
        gf.update_screen(game_settings, screen, ship, aliens, bullets)

run_game()