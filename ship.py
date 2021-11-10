import sys

import pygame

class Ship:
    """A calls to manage the ship"""

    def __init__(self, ai_game):
        #initialize the ship and its starting position

        self.screen = ai_game.screen
        self.screenRect = ai_game.screen.get_rect()

        #Movment flags
        self.moving_right = False
        self.moving_left = False

        #Load the ship image and get its rec

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screenRect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

