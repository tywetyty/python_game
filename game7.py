#conding=utf-8
import pygame
from pygame.locals import *
from  sys import exit
from random import randint
pygame.init()
srceen=pygame.display.set_mode((640,480),0,32)
while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
	rand_col=(randint(0,255),randint(0,255),randint(0,255))
	srceen.lock()
	for _ in range(100):
		rand_pos=(randint(0,639),randint(0,479))
		srceen.set_at(rand_pos,rand_col)
	srceen.unlock()
	pygame.display.update()