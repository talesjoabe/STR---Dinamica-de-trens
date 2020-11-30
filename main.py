import arcade
import os
from functions import *
from train import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
	def __init__(self,width,height):
		super().__init__(width, height)
		arcade.set_background_color(arcade.color.WHITE)
	
	def setup(self):
		# xc, yc, colour, velocity, width_rail, height_rail, width_train, height_train
		self.train1 = train(75, 482,arcade.color.ELECTRIC_GREEN, 1, 105, 65,20,10 )
		self.train2 = train(185,482,arcade.color.PURPLE, 1, 105, 65, 20, 10)
		self.train3 = train(293,482,arcade.color.RED, 1, 105, 65, 20, 10)	
		self.train4 = train(75, 412, arcade.color.BLUE, 1, 325, 65, 20, 10) 
	
		pass

	def on_draw(self):
		arcade.start_render()
		arcade.draw_text("Visualizacao  da dinamica dos trens", 35, 550, arcade.color.BLACK, 20)
		arcade.draw_text("Painel de controle de velocidade", 35, 180, arcade.color.BLACK, 20)

		# desenhando os trens
		self.train1.drawTrain()
		self.train2.drawTrain()
		self.train3.drawTrain()
		self.train4.drawTrain()
		
		# TRILHO-RETANGULO
		drawRails()
		
		# VELOCIMETRO
		drawControlVelocity()
		
		# BOTAO DE CONTROLE DO VELOCIMETRO
		drawControlVelocityButton()
	
	def update(self, delta_time):
		self.train1.moveTrain()
		self.train2.moveTrain()
		self.train3.moveTrain()
		self.train4.moveTrain()
		
		pass

	
def main(): 
	window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
	window.setup()
	arcade.run()
	
	#arcade.finish_render()

if __name__ == "__main__":
    main()
