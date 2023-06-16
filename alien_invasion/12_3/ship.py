import pygame


class Ship():
	
	def __init__(self,screen,ai_setting):
		self.screen = screen
		self.image = pygame.image.load('huojian.bmp')
		self.ai_setting = ai_setting
		
		self.image_rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		self.image_rect.center = self.screen_rect.center
		
		self.center_right = float(self.image_rect.right)
		self.center_left = float(self.image_rect.left)
		self.center_top = float(self.image_rect.top)
		self.center_bottom = float(self.image_rect.bottom)
		
		
		
		#运动标志
		self.moving_right = True
		self.moving_left = False
		self.moving_top = False
		self.moving_bottom = False
		
		#文件控件
		self.file = '/storage/emulated/0/python/alien_invasion/12_3/file.txt'
		self.left = 0
		self.right = 0
		self.right_num = 0
	
	def blitme(self):
		self.screen.blit(self.image,self.image_rect)
	
	def update(self):
		#检查移动标志状态，以及与屏幕边界的距离
		if self.image_rect.right == self.screen_rect.right:
		    self.moving_right = False
		    self.moving_left = True
		    self.right_num += 1
		if self.image_rect.left == self.screen_rect.left:
		    self.moving_left = False
		    self.moving_right = True
		
		if self.moving_right and (self.image_rect.right) != (self.screen_rect.right) :
			self.image_rect.centerx += self.ai_setting.ship_speed_factor
			self.right += 1
			#self.image_rect.right = self.center_right
			
		if self.moving_left and (self.image_rect.left) != (self.screen_rect.left):
			#self.center_right -= self.ai_setting.ship_speed_factor
			self.image_rect.centerx -= self.ai_setting.ship_speed_factor
			self.left += 1
			
		if self.moving_top and (self.image_rect.top) < (self.screen_rect.top) :
			self.center_top += self.ai_setting.ship_speed_factor
			self.image_rect.center.top = self.center_top
		
		if self.moving_bottom and (self.image_rect.bottom) < (self.screen_rect.bottom):
			self.center_bottom += self.ai_setting.ship_speed_factor
			self.image_rect.center.bottom =self.center_bottom
					