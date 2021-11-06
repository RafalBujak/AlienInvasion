# This is a sample Python script.

import sys

import pygame

class AlienInvasion:
    def __init__(self):
        """Initialisation the  game"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def runGame(self):
        """Start the main loop for th egame"""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                sys.exit()

            #make the most recentlu drawn screen vivisible.
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.runGame()

