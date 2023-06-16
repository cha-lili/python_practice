import pygame

class Ship():
	def __init__(self,screen,ai_setting):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.setting = ai_setting
		
		self.image = pygame.image.load('/storage/emulated/0/python/alien_invasion/12-5/image/ship.bmp')
		self.image_rect = self.image.get_rect()
		
		self.image_rect.left = self.screen_rect.left
		self.image_rect.centery = self.screen_rect.centery
		self.y = float(self.image_rect.y)
		self.speed = self.setting.image_speed
		
		
	def blitme(self):
		self.screen.blit(self.image,self.image_rect)

	def downdate(self):
		self.y -= self.speed
		self.image_rect.y = self.y
	def update(self):
		self.y += self.speed
		self.image_rect.y = self.y
		
		