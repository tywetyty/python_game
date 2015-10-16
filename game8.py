#conding=utf-8
import pygame
from pygame.locals import *
from  sys import exit
from random import *
from math import pi
pygame.init()
srceen=pygame.display.set_mode((640,480),0,32)
points=[]
while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
		if event.type==