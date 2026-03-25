import sys
import pygame
from ship import Ship

class AlienInvasion: # Overall class to manage game assets and behavior
    def __init__(self): # Initialize the game amd create game resources
        pygame.init()
        self.screenWidth = 1280
        self.screenHeight = 800
        self.ship = Ship(self)
        self.screen = pygame.display.set_mode((1280, 800))
        # Setting background color
        self.bgColor = (27, 37, 77) # (128, 180, 130)

        pygame.display.set_caption("Definitely not Space Invaders")
        self.clock = pygame.time.Clock()



    def runGame(self): # Start the main loop for the game
        while True:
            self._checkEvents()
            self._updateScreen()
            self.clock.tick(60)
            self.ship.blitme()
    def _checkEvents(self):
        while True:
            # Watching for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.rect.x += 10
                    if event.key == pygame.K_LEFT:
                        self.ship.rect.x -= 10
                    # My favorite part of Space Invaders, moving up and down
                    if event.key == pygame.K_UP:
                        self.ship.rect.y -= 10
                    if event.key == pygame.K_UP:
                        self.ship.rect.y -= 10
                    
                    


    def _updateScreen(self):
            # Redraw the screan for each pass through the loop
            self.screen.fill(self.bgColor)
            self.ship.blitme()
            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance and run it
    ai = AlienInvasion()
    ai.runGame()

# Page 236