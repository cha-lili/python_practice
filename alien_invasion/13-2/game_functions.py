import pygame
import sys

from bullet import Bullet
from Alien import Alien



def check_events(ship,screen,bullets,ai_setting):
	#检查键盘状态
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if ai_setting.moving_bullet:
			fire_bullet(ai_setting,screen,bullets,ship)
		elif event.type == pygame.KEYDOWN:
		    pass
			#check_down(ship,event,screen,ai_setting)
		elif event.type == pygame.KEYUP:
			#check_up(ship,event)
			pass

def update_screen(screen,ship,ai_setting,bullets,aliens):
	#填充屏幕颜色，刷新image,刷新屏幕
	screen.fill(ai_setting.color)
	remove_bullet(bullets,ship)
	#更新精灵位置
	bullets.update()
	#绘画精灵
	for bullet in bullets.sprites():
		#bullets是Group类的实例,类中方法.sprites返回列表,Group容器中每个变量均为Bullet的实例，调用其中方法draw_bullet(),绘画矩形
		bullet.draw_bullet()
	#删除已离开屏幕的精灵
	
	#显示image
	ship.blitme()
	aliens.draw(screen)
	pygame.display.flip()
	
	
def check_down(ship,event,screen,ai_setting):
	#检查按下的键,隶属check_envents
	if event.key == pygame.K_RIGHT:
				ship.moving_right = True
	if event.key == pygame.K_LEFT:
				ship.moving_left = True
	if event.key == pygame.K_UP:
				ship.moving_top = True
	if event.key == pygame.K_DOWN:
				ship.moving_bottom = True
	#if event.key == pygame.K_SPACE:
#	if ai_setting.moving_bullet:
#		fire_bullet(ai_setting,screen,bullets,ship)
	
def check_up(ship,event):
	#检查抬起的键,隶属check_events
	if event.key == pygame.K_RIGHT:
				ship.moving_right = False
	if event.key == pygame.K_LEFT:
				ship.moving_left = False
	if event.key == pygame.K_UP:
				ship.moving_top = False
	if event.key == pygame.K_DOWN:
				ship.moving_bottom = False
				
def fire_bullet(ai_setting,screen,bullets,ship):
	#发射精灵(设置,屏幕,Group容器,image属性)
	if len(bullets) < ai_setting.bullet_allowed :
	    new_bullet = Bullet(ai_setting,screen,ship)
	    bullets.add(new_bullet)

def remove_bullet(bullets,ship):
	for bullet in bullets.copy():
		if bullet.bullet_rect.top <= ship.screen_rect.top:
			bullets.remove(bullet)
			
def create_fleet(ai_setting,screen,aliens,ship):
	'''创建外星人群'''
	alien = Alien(screen,ai_setting)
	alien_width = alien.rect.width
	
	number_alien_x = get_number_aliens_x(ai_setting,alien_width)
	number_rows = get_number_rows(ai_setting,ship.image_rect.height,alien.rect.height)
	
	for number_row in range(number_rows):
		for alien_number in range(number_alien_x):
			create_alien(ai_setting,screen,aliens,alien_number,number_row)

def get_number_aliens_x(ai_setting,alien_width):
	#计算屏幕空间内的外星人数量，并返回
	available_space_x = ai_setting.screen_width - 2 * alien_width
	number_alien_x = int(available_space_x / (2 * alien_width))
	return number_alien_x

def create_alien(ai_setting,screen,aliens,alien_number,row_number):
	alien = Alien(screen,ai_setting)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 *alien.rect.height * row_number
	aliens.add(alien)

def get_number_rows(ai_setting,ship_height,alien_height):
	available_space_y = (ai_setting.screen_height - (2 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

