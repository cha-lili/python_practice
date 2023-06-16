import pygame
from ship_test import Ship
import time

def run_game():

    pygame.init()
    screen = pygame.display.set_mode((1920,1920))
    screen_rect = screen.get_rect()
    ship = Ship(screen)
    
    while True:
        #填充屏幕
        screen.fill((135,206,235))
        
        if (ship.image_rect.top) == (screen_rect.top) and (ship.image_rect.right) != (screen_rect.right):
            ship.image_rect.right+=1
        
        elif (ship.image_rect.right) == (screen_rect.right) and (ship.image_rect.bottom) != (screen_rect.bottom):
            ship.image_rect.bottom+=1
        
        elif (ship.image_rect.bottom) == (screen_rect.bottom) and (ship.image_rect.left) != (screen_rect.left):
            ship.image_rect.right-=1
            
        elif (ship.image_rect.left) ==(screen_rect.left) and (ship.image_rect.top) != (screen_rect.top):
            ship.image_rect.bottom-=1
        
        #time.sleep(0.005)
        ship.blitme()
        pygame.display.update()
        
run_game()