import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()  # inizializzo
    ai_settings = Settings()  # richiamo i settaggi
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # creo lo schermo
    ship = Ship(ai_settings, screen)  # carico la navicella sullo schermo
    pygame.display.set_caption("Alien Invasion")  # mostro il nome

    while True:
        gf.check_events(ship)  # aggiorno eventi
        ship.update()  # aggiorno movimenti della ship
        gf.update_screen(ai_settings, screen, ship)  # applico allo schermo


run_game()
