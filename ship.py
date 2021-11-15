import sys

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A calls to manage the ship"""

    def __init__(self, ai_game):
        # initialize the ship and its starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()



        # Movment flags
        self.moving_right = False
        self.moving_left = False

        # Load the ship image and get its rec

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Store a decimal value for the ship,s horizontal possition
        self.x = float(self.rect.x)

        #start each new ship at the bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
