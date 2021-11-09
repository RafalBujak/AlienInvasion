# This is a sample Python script.

import sys

import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        """Initialisation the  game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screenWidth, self.settings.screenHeight))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


    def runGame(self):
        """Start the main loop for th egame"""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        #Redraw the screen during each pass the trhought loop
        self.screen.fill(self.settings.bgColor)
        self.ship.blitme()

        #make the most recentlu drawn screen vivisible.
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.runGame()

