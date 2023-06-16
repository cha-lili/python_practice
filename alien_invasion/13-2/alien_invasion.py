import sys
import pygame
from setting import Setting
from ship import Ship
from Alien import Alien
from bullet import Bullet

import game_functions as gf
from pygame.sprite import Group

def run_game():
	#初始化并创建对象
	pygame.init()
	clock = pygame.time.Clock()
	ai_setting = Setting()
	screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
	
	pygame.display.set_caption('Alien Invasion')
	ship = Ship(screen,ai_setting)
	#alien = Alien(screen,ai_setting)
	bullets = Group()
	aliens = Group()
	gf.create_fleet(ai_setting,screen,aliens,ship)
	
	#bg_color = (230,230,230)
	#开始游戏的主循环
	while True:
	    clock.tick(90)
	    gf.check_events(ship,screen,bullets,ai_setting)
	    gf.update_screen(screen,ship,ai_setting,bullets,aliens)

run_game()