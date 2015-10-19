# class Vector2(object):
# 	"""docstring for Vector2"""
# 	def __init__(self, x=0.0,y=0.0):
# 		self.x=x
# 		self.y=y
# 	def __str__(self):
# 		return "(%s,%s)" %(self.x,self.y)
# 	@classmethod
# 	def from_piont(cls,p1,p2):
# 		return cls(p2[0]-p1[0],p2[1]-p1[1])

# A = (10.0, 20.0)
# B = (30.0, 35.0)
# AB = Vector2.from_piont(A, B)
# print AB
# from gameobjects.vector2 import *
# A = (10.0, 20.0)
# B = (30.0, 35.0)
# AB = Vector2.from_points(A, B)
# print "Vector AB is", AB
# print "AB * 2 is", AB * 2
# print "AB / 2 is", AB / 2

# print "Magnitude of AB is", AB.get_magnitude()
# print "AB normalized is", AB.get_normalized()
# 		
# 	
background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'
import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
position = Vector2(100.0,100.0)
pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
background = pygame.image.load(background_image_filename).convert()
sprtie = pygame.image.load(sprite_image_filename).convert_alpha()
clock = pygame.time.Clock()

heading = Vector2()
while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
	screen.blit(background,(0,0))
	screen.blit(sprtie,position)
	time_passed=clock.tick()
	time_passed_seconds = time_passed/1000.0
	desination = Vector2(*pygame.mouse.get_pos())-Vector2(*sprtie.get_size())/2
	vector_to_mouse = Vector2.from_points(position,desination)
	vector_to_mouse.normalize()
	heading=heading+(vector_to_mouse*.6)
	position+=heading*time_passed_seconds
	pygame.display.update()
