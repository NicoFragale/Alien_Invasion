import sys
import pygame


def check_events(ship):  # respond to key presses and mouse events

    for event in pygame.event.get():  # per ogni evento che viene registrato dagli input

        if event.type == pygame.QUIT:  # se chiudo il gioco
            sys.exit()  # allora chiudo il gioco

        elif event.type == pygame.KEYDOWN:  # se premo un tasto
            check_keydown_events(event, ship)  # richiamo la funzione qua sotto

        elif event.type == pygame.KEYUP:  # se non premo piu niente
            check_keyup_events(event, ship)  # richiamo la funzione qua sotto


def check_keydown_events(event, ship):  # se premo un tasto
    if event.key == pygame.K_RIGHT:  # se è la freccia a destra
        ship.moving_right = True  # attivo il movimento a destra
    elif event.key == pygame.K_LEFT:  # altrimenti sinistra
        ship.moving_left = True


def check_keyup_events(event, ship):  # se non premo piu niente
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False  # la ship non deve piu muoversi
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    # Update images on the screen and flip to the new screen
    screen.fill(ai_settings.bg_color)  # riempio lo schermo del colore
    ship.blitme()  # lo mostro
    pygame.display.flip()  # e aggiorno lo schermo
