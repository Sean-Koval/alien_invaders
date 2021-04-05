import sys
import pygame
from bullet import Bullet
from alien import Alien

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
        fire_bullet(game_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    
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

def check_events(game_settings, screen, ship, aliens, bullets):
    
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
        
                

def update_screen(game_settings, screen, ship, aliens, bullets):
    
    """
    Update images on the screen and flip to the new screen
    """

    # Redraw the screen during each pass through the loop
    screen.fill(game_settings.background_color)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

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

def fire_bullet(game_settings, screen, ship, bullets):
    
    """
    Fire bullet if limit not reached

    Args:
        game_settings ([type]): [description]
        screen ([type]): [description]
        ship ([type]): [description]
        bullets ([type]): [description]
    """
    # Create a new bullet and add it to the bullets group
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)
        

def create_fleet(game_settings, screen, aliens):
    
    """
    Create a full fleet of aliens
    """
    
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is equal to one alien width
    alien = Alien(game_settings, screen)
    number_of_aliens = get_number_of_aliens(game_settings, alien.rect.width)


    # Create the first row of aliens
    for alien_number in range(number_of_aliens):
        # Create an alien and palace it in the row
        create_alien(game_settings, screen, aliens, alien_number)


def get_number_of_aliens(game_settings, alien_width):
    """
    Determines the number of aliens that fit in a row
    """
    available_space = game_settings.screen_width - (2 * alien_width)
    number_of_aliens = int(available_space / (2 * alien_width))
    
    return number_of_aliens

def create_alien(game_settings, screen, aliens, alien_number):
    """
    Create an alien and place it in a row
    """
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.x = alien.x
    aliens.add(alien)