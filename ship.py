import pygame

from settings import Settings


class Ship:
    def __init__(self, ai_settings, screen):
        self.screen = screen  # carico lo schermo
        # load the ship and get its rect
        self.image = pygame.image.load("images/ship.png")  # carico l immagine
        self.rect = self.image.get_rect()  # carico il rettangolo dell immagine
        self.screen_rect = screen.get_rect()  # il rettangolo dello schermo
        # each ship must be at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx  # centro la navicella
        self.rect.bottom = self.screen_rect.bottom  # in basso
        # movement flag
        self.moving_right = False  # all inizio la navicella non si muove a destra
        self.moving_left = False  # all inizio la navicella non si muove a sinistra
        self.ai_settings = ai_settings  # le caratteristiche
        self.center = float(self.rect.centerx)  # perche muoveremo la navicella di 1.5

    def update(self):
        # update the position based on the movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:  # se va a destra, nei limiti del rettangolo
            self.center += self.ai_settings.ship_speed_factor  # la faccio muovere a destra con ship_speed_factor fattore
        if self.moving_left and self.rect.left > 0:  # per la sinistra
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center  # devo aggiornare la posizione del rettangolo

    def blitme(self):
        # draw the ship
        self.screen.blit(self.image, self.rect)  # mostro l aggiornamento
        
        