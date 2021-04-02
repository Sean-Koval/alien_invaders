import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, game_settings, screen, ship, bullets):
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
    elif event.key == pygame.K_SPACE:
        # Creat a new bullet and add it to the bullets group
        if len(bullets) < game_settings.bullets_allowed:
            new_bullet = Bullet(game_settings, screen, ship)
            bullets.add(new_bullet)
    
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
            check_keydown_events(event, game_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        
                

def update_screen(game_settings, screen, ship, bullets):
    """
    Update images on the screen and flip to the new screen
    """

    # Redraw the screen during each pass through the loop
    screen.fill(game_settings.background_color)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.bltime()

    # Make most of drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """
    Update position of bullets and get rid of old bullets

    Args:
        bullets ([type]): [description]
    """
    # Update position
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

