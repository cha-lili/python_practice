import pygame
from pygame.sprite import Group

from setting import Setting
import functions as fu


def main():
	pygame.init()
	clock = pygame.time.Clock()
	
	setting = Setting()
	screen = pygame.display.set_mode(setting.size)
	
	stars = Group()
	fu.get_star(stars,setting)
	
	while True:
		clock.tick(90)
		screen.fill(setting.color)
		stars.draw(screen)
		pygame.display.update()

main()