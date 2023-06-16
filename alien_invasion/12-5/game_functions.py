import pygame
from bullet import Bullet

def update(screen,ship,ai_setting,bullets):
	screen.fill(ai_setting.screen_color)
	
	for bullet in bullets.sprites():
		bullet.bullet_draw()
	remove_bullet(bullets)
	ship.blitme()
	pygame.display.flip()

def frie_bullet(screen,ship,ai_setting,bullets):
	if len(bullets) < 100:	
		new_bullet = Bullet(screen,ship,ai_setting)
		bullets.add(new_bullet)

def check_event(screen,ship,ai_settimg,bullets):
	for event in pygame.event.get():
		frie_bullet(screen,ship,ai_settimg,bullets)

def remove_bullet(bullets):
	for bullet in bullets.copy():
		if bullet.bullet.right == 1000:
			bullets.remove(bullet)

def update_image(ship,ai_setting):
	if ship.image_rect.top == ship.screen_rect.top:
		ai_setting.image_up = False
		ai_setting.image_down = True
	elif ship.image_rect.bottom == ship.screen_rect.bottom:
		ai_setting.image_up = True
		ai_setting.image_down = False
	
	if ai_setting.image_up:
		ship.downdate()
	if ai_setting.image_down:
		ship.update()