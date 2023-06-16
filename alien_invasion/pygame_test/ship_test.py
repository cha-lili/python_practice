import pygame

class Ship():

    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('potato.bmp')
        self.image_rect = self.image.get_rect()
    
    def blitme(self):
        self.screen.blit(self.image,self.image_rect)