import pygame
from pygame.sprite import Sprite

class Rect(Sprite):
	def __init__(self,screen,ai_setting):
		super().__init__()
		self.screen = screen
		self.ai_setting = ai_setting
		
		self.set_rect = pygame.Rect(0,0,self.ai_setting.rect_width,self.ai_setting.rect_height)
		
		self.screen_rect = self.screen.get_rect()
		
		self.set_rect.center = self.screen_rect.center
		self.rect_color = self.ai_setting.rect_color
		
	def draw_rect(self):
		pygame.draw.rect(self.screen,self.rect_color,self.set_rect)