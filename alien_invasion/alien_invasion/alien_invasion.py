import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#初始化并创建对象
	pygame.init()
	ai_settings = Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigth))
	
	pygame.display.set_caption('Alien Invasion')
	ship = Ship(screen)
	
	#bg_color = (230,230,230)
	#开始游戏的主循环
	while True:
	    gf.check_events()
	    gf.update_screen(ai_settings,screen,ship)
run_game()