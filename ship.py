import pygame


class Ship:
    def __init__(self, screen):
        self.screen = screen
        # load the ship and get its rect
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # each ship must be at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # movement flag
        self.moving_right = False

    def update(self):
        # update the position based on the movement flag
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        # draw the ship
        self.screen.blit(self.image, self.rect)
        
        