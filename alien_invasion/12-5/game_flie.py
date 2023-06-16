import pygame
from pygame.sprite import Group

from setting import Setting
from ship import Ship
import game_functions as gf

def run_game():
	pygame.init()
	
	ai_setting = Setting()
	bullets = Group()
	
	screen = pygame.display.set_mode(ai_setting.screen_size)
	ship = Ship(screen,ai_setting)
	
	while True:
		gf.check_event(screen,ship,ai_setting,bullets)
		gf.update_image(ship,ai_setting)
		bullets.update()
		gf.update(screen,ship,ai_setting,bullets)
	
run_game()