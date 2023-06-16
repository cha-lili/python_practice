import pygame
from ship import Ship
import game_functions as gf
from setting import Setting
from pygame.sprite import Group


def run_game():
    #初始化pygame
    pygame.init()
    #创建设置实例
    ai_setting = Setting()
    #创建屏幕(屏幕尺寸(应是可迭代属性))
    screen = pygame.display.set_mode(ai_setting.size)
    #创建image实例(传入屏幕，设置)
    ship = Ship(screen,ai_setting)
    #创建Group实例,Group类似列表,储存精灵
    bullets = Group()
    
    
    while True:
    	#检查按键
    	gf.check_events(ship,screen,bullets,ai_setting)
    	#检查按键标志
    	ship.update()
    	bullets.update()
    	for bullet in bullets.copy():
    		if bullet.bullet_rect.bottom <= 0:
    			bullets.remove(bullet)
    	#刷新屏幕
    	if ship.right_num <= 2:
    		with open(ship.file,'a') as fi:
    			fi.write('向右运行了{}步，向左运行了{}步\n'.format(str(ship.right),str(ship.left)))
    	else:
    		break
    	gf.update_screen(screen,ship,ai_setting,bullets)
    	
run_game()