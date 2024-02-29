import sys
import pygame


def check_events(ship):
    # respond to key presses and mouse events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False


def update_screen():
    # Update images on the screen and flip to the new screen
    return 0
