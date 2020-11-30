import arcade
import os

train_width =  20
train_height = 10
velocity = 1

xc_t1 = 75 
yc_t1 = 482
colour_t1 = arcade.color.ELECTRIC_GREEN
 
xc_t2 = 185 
yc_t2 = 482
colour_t2 = arcade.color.PURPLE

xc_t3 = 295
yc_t3 = 482
colour_t3 = arcade.color.RED

xc_t4 = 75
yc_t4 = 412 
colour_t4 = arcade.color.BLUE

def move_train(xc,yc, width_rail, height_rail, velocity):
	count = 1
	while(count < width_rail):
		xc = xc+velocity
		count=count+1
def drawRails():
	# TRILHO-RETANGULO
	arcade.draw_rectangle_outline(115, 450, 105, 65,arcade.color.ELECTRIC_GREEN)
	arcade.draw_rectangle_outline(225, 450, 105, 65,arcade.color.PURPLE)
	arcade.draw_rectangle_outline(335, 450, 105, 65,arcade.color.RED)
	arcade.draw_rectangle_outline(225, 380, 325, 65,arcade.color.BLUE)

def drawControlVelocity():
	arcade.draw_rectangle_filled(80, 100, 15, 125, arcade.color.ELECTRIC_GREEN)
	arcade.draw_rectangle_filled(140, 100, 15, 125, arcade.color.PURPLE)
	arcade.draw_rectangle_filled(200, 100, 15, 125, arcade.color.RED)
	arcade.draw_rectangle_filled(260, 100, 15, 125, arcade.color.BLUE)

def drawControlVelocityButton():
	# BOTAO DE CONTROLE DO VELOCIMETRO
	arcade.draw_point(80, 60, arcade.color.ELECTRIC_GREEN, 30)
	arcade.draw_point(140, 60, arcade.color.PURPLE, 30)
	arcade.draw_point(200, 60, arcade.color.RED, 30)
	arcade.draw_point(260, 60, arcade.color.BLUE, 30)


