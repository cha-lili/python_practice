import pygame
import sys

from bullet import Bullet



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

def update_screen(screen,ship,ai_setting,bullets):
	#填充屏幕颜色，刷新image,刷新屏幕
	screen.fill(ai_setting.color)
	#绘画精灵
	for bullet in bullets.sprites():
		#bullets是Group类的实例,类中方法.sprites返回列表,Group容器中每个变量均为Bullet的实例，调用其中方法draw_bullet(),绘画矩形
		bullet.draw_bullet()
	ship.blitme()
	
	pygame.display.update()
	
	
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