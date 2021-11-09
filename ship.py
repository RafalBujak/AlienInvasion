import pygame

class Ship:
    """A calls to manage the ship"""

    def __init__(self, ai_game):
        #initialize the ship and its starting position

        self.screen = ai_game.screen
        self.screenRect = ai_game.screen.get_rect()

        #Load the ship image and get its rec

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screenRect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
