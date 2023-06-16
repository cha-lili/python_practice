import pygame
from setting import Setting

Active=0
Active_0 = True
mo=0
settings = Setting()

file = '/storage/emulated/0/python/test/event_test.txt'
pygame.init()

def check_event(m):
	for event in pygame.event.get():
		if Active_0:
			m+=1
			with open(file,'a') as fe:
			        fe.write('触摸'+ str(m)+'\n')
while True:
	check_event(mo)
	Active += 0.5