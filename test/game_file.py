#点击显示，一秒后消失

import pygame
from setting import Setting
from pygame.sprite import Group
import check_event as ce

number = 0
file = '/storage/emulated/0/python/test/draw_number.txt'


def run_game(num):
	pygame.init()
	ai_setting = Setting()
	container = Group()
	screen = pygame.display.set_mode(ai_setting.size)
	Active = True
	
	while Active:
#		if num >9:
#			Active = False
		
		screen.fill(ai_setting.color)
		ce.check_event(container,screen,ai_setting)
		for spr in container.sprites():
			num += 1
			spr.draw_rect()
			ce.write_data(num,file)
		pygame.display.update()
	return num

number = run_game(number)
with open(file,'a') as fi:
	fi.write('总共运行{}次\n'.format(str(number)))