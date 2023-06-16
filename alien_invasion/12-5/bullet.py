import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,screen,ship,ai_setting):
		super().__init__()
		self.screen = screen
		self.ship = ship
		self.setting = ai_setting
		
		self.bullet = pygame.Rect(0,0,self.setting.bullet_width,self.setting.bullet_height)
		#self.bullet_rect = self.bullet.get_rect()
		self.bullet.center = self.ship.image_rect.center
		self.bullet.right = self.ship.image_rect.right
		
		self.bullet_speed = self.setting.bullet_speed_factor
		self.x = float(self.bullet.x)
		self.color = self.setting.bullet_color
		
	def update(self):
		self.x += self.bullet_speed
		self.bullet.x = self.x
	
	def bullet_draw(self):
		pygame.draw.rect(self.screen,self.color,self.bullet)
		