import sys
import pygame


def check_events(ship):
    """
    Responds to keypresses and mouse events
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right with key press
                ship.centerx+= 1

def update_screen(ai_settings, screen, ship):
    """
    Update images on the screen and flip to the new screen
    """

    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.bltime()

    # Make most of drawn screen visible
    pygame.display.flip()

