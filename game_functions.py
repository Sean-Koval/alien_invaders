import sys
import pygame

def check_keydown_events(event, ship):
    """
    Respond to keypresses.

    Args:
        event ([type]): [description]
        ship ([type]): [description]
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    
def check_keyup_events(event, ship):
    """
    Respong to key releases.

    Args:
        event ([type]): [description]
        ship ([type]): [description]
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """
    Responds to keypresses and mouse events
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        
                

def update_screen(game_settings, screen, ship):
    """
    Update images on the screen and flip to the new screen
    """

    # Redraw the screen during each pass through the loop
    screen.fill(game_settings.background_color)
    ship.bltime()

    # Make most of drawn screen visible
    pygame.display.flip()

