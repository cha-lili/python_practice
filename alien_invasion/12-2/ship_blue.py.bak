import pygame


class Ship():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('/storage/emulated/0/python/alien_invasion/potato.bmp')
#        self.screen_rect = self.screen.get_rect()
        self.image_rect = self.image.get_rect()
        self.image_rect.right = 590
        self.image_rect.bottom = 500
#       self.image_rect.center = self.screen_rect.center
        
    def blitme(self):
        self.screen.blit(self.image,self.image_rect)