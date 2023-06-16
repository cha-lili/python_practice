import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self):
		super().__init__()
		#self.screen = screen
		self.image = pygame.image.load('image/star.bmp')
		self.rect = self.image.get_rect()
		