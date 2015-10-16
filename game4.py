#coding=utf-8
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
font = pygame.font.SysFont('arial', 50)
text=font.render(u'ssdsad',True, (0, 0, 255))
print text.get_width()
x=0
y=(480-text.get_height())/2
background = pygame.image.load("sushiplate.jpg").convert()
while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
	screen.blit(background,(0,0))
	x -=2
	print text.get_width()
	if x<-text.get_width():
		x=640-text.get_width()
	screen.blit(text,(x,y))
	pygame.display.update()