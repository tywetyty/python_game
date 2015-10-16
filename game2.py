#coding=utf-8
import pygame
from pygame.locals import *
from sys import exit
# import os
# TORK_FONT_NAME = 'TORK____.ttf'
SCREEN_SIZE = (640,480)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
# tork_font_path = os.path.join('data\\font', TORK_FONT_NAME)
# font = pygame.font.Font(tork_font_path , 16)
# font_height=font.get_linesize()
font = pygame.font.SysFont("arial", 16);
font_height = font.get_linesize()
event_text=[]
while True:
	event=pygame.event.wait()
	#获得时间的名称
	event_text.append(str(event))
	#这个切片操作保证了event_text里面只保留一个屏幕的文字
	event_text=event_text[-SCREEN_SIZE[1]/font_height]
	if event.type==QUIT:
		exit()
	screen.fill((255,255,255))
	y=SCREEN_SIZE[1]-font_height
	for text in reversed(event_text):
		screen.blit(font.render(text,True,(0,0,0)),(0,y))
		y-=font_height
	pygame.display.update


	
