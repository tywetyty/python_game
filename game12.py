import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from math import *

class GameEntity(object):
	"""docstring for GameEntity"""
	def __init__(self, world,name,image):
		self.world=world
		self.name=name
		self.image=image
		self.location=Vector2(0,0)
		self.destination=Vector2(0,0)
		self.speed=0
		self.brain=StatMachine()
		self.id=0
	def render(self,surface):
		x,y=self.location
		w,h=self.image.get_size()
		surface.blit(self.image,(x,y))
	def process(self,time_passed):
		self.brain.think()
		if self.speed>0 and self.location != self.destination:
			vec_to_destination = self.destination-self.location
			distance_to_destination=vec_to_destination.get_length()
			heading = vec_to_destination.get_normalized()
			travel_distance=min(distance_to_destination,time_passed*self.speed)
			self.location+=travel_distance*heading



class World(object):
			"""docstring for world"""
			def __init__(self):
				self.entities={}
				self.entity_id=0
				self.background=pygame.surface.Surface(SCREEN_SIZE).convert()
				self.background.fill((255,255,255))
				pygame.draw.circle(self.background,(200,255,200),NEST_POSITION, int(NEST_SIZE))
			def add_entity(self,entity):
				self.entities[self.entity_id]=entity
				entity.id=self.entity_id
				self.entity_id+=1
			def remove_entity(self,entity):
				del self.entities[entity.id]
			def get(self,entity_id):
				if entity_id in self.entities:
					return self.entities[entity_id]
				else:
					return None
			def process(self,time_passed):
				time_passed_seconds=time_passed/1000.0
				for entity in self.entities.itervalues():
					entity.process(time_passed_seconds)
			def render(self,surface):
				surface.blit(self.background,(0,0))
				for  entity in self.entities.values():
					entity.render(surface)
			def get_close_entity(self, name, location, Irange=100.):
				location=Vector2(*location)
				for entity in self.entities.values():
					if entity.name==name:
						distance = location.get_distance_to(entity.location)
						if distance<Irange:
							return entity
				return None
				
		