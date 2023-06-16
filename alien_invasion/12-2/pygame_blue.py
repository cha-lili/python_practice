import pygame
from ship_blue import Ship

#初始化pygame
pygame.init()

#设定幕布大小
size = width,height = 480,480
screen = pygame.display.set_mode(size)

'''
移入ship_blue.py

#读取image
image = pygame.image.load('/storage/emulated/0/python/alien_invasion/potato.bmp')

#获取image的矩形位置
image_rect = image.get_rect()
screen_rect = screen.get_rect()

#设置图片位置，center,centerx,centery..
#同样的方法还有top,bottom,left,right,直接设定参数
image_rect.center = screen_rect.center

'''
ship = Ship(screen)
ship.image_rect.left = 480

while True:
    screen.fill((135,206,235))
    
    ship.blitme()
    
    pygame.display.flip()