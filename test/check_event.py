import pygame
from sprite import Rect

def save_sprite(container,screen,ai_setting):
	if len(container) <= ai_setting.rect_number:
		new_rect = Rect(screen,ai_setting)
		container.add(new_rect)



def check_event(container,screen,ai_setting):
	for event in pygame.event.get():
		if ai_setting.moving_rect:
			save_sprite(container,screen,ai_setting)
			
def write_data(info,file):
	with open(file,'a') as fi:
		fi.write('绘制{}次\n'.format(str(info)))