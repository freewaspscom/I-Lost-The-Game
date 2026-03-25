import pygame

class Ship:
    def __init__(self, aiGame):
        self.screen = aiGame.screen.get_rect()
        self.screen_rect = aiGame.screen.get_rect

        self.image = pygame.imafge.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)