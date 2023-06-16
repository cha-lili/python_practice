import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,ai_setting,screen,ship):
		#初始化父类
		super().__init__()
		#建立屏幕尺寸对象
		self.screen = screen
		self.ai_setting = ai_setting
		self.ship = ship
		
		#创建一个矩形(x,y,宽,高)
		self.bullet_rect = pygame.Rect(0,0,self.ai_setting.bullet_width,ai_setting.bullet_height)
		
		#使创建的矩形中心点与image中心点重合
		self.bullet_rect.centerx = self.ship.image_rect.centerx
		
		#使矩形顶部等于image顶部
		self.bullet_rect.top = self.ship.image_rect.top
		#浮点数化矩形的y轴坐标
		self.y = float(self.bullet_rect.y)
		#矩形的速度数量
		self.speed_factor = self.ai_setting.bullet_speed_factor
		#矩形的颜色
		self.bullet_color = self.ai_setting.bullet_color
		
	def update(self):
		#更改浮点化的y轴坐标,将值传给矩形的y轴坐标
		self.y -= float(self.speed_factor)
		self.bullet_rect.y = self.y
	
	def draw_bullet(self):
		#绘画矩形(绘画对象,绘画颜色,创建的矩形)
		pygame.draw.rect(self.screen,self.bullet_color,self.bullet_rect)


		