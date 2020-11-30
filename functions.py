import arcade
import os

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


