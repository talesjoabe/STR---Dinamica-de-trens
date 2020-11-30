import threading # threads
import time # tempo (opcional)
import arcade
import os


# define uma classe para a criacao de threads
class train:
	def __init__(self, xc, yc, colour, velocity, width_rail, height_rail, width_train, height_train):
		self.xc = xc
		self.yc = yc
		self.xc_aux = xc
		self.yc_aux = yc
		self.colour = colour
		self.velocity = velocity
		self.width_rail = width_rail
		self.height_rail = height_rail
		self.width_train = width_train
		self.height_train = height_train
		self.count_1 = 1
		self.count_2 = 1
		self.count_3 = 1
		self.count_4 = 1
	
	def drawTrain(self):
		arcade.draw_rectangle_filled(self.xc, self.yc, self.width_train, self.height_train , self.colour)
	
	def moveTrain(self):
		if self.count_1 < self.width_rail-self.width_train:		
			self.xc = self.xc+self.velocity
			self.count_1=self.count_1+1

		elif self.count_2 < self.height_rail:
			self.width_train = 10
			self.height_train = 20
			self.yc = self.yc-self.velocity
			self.count_2= self.count_2+1
			self.count_3 = self.count_1
		elif self.count_3 > -10:
			self.width_train = 20
			self.height_train = 10
			self.xc = self.xc-self.velocity
			self.count_3= self.count_3-1
			self.count_4 = self.count_2
		elif self.count_4 > -1 :
			self.width_train = 10
			self.height_train = 20
			self.yc = self.yc+self.velocity
			self.count_4= self.count_4-1
		else:
			self.count_1 = 1
			self.count_2 = 1
			self.width_train = 20
			self.height_train = 10
			self.xc = self.xc_aux
			self.yc = self.yc_aux
			
			
		
				
