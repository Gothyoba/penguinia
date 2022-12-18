import numpy as np
from error import *
#coordinates is currently unused
import coordinates as c
from combat import combat1


def print_name(pos):
    name = c.get_desc(pos)
    print("You are in " + c.get_name(pos) + ".")
    print(name)

#gets quests from names coordinates
def get_quests(pos):
	quest = c.get_quest(pos)
	try:
		print("There is a quest " + quest.name + ". Do you want to play it?")
	except Exception as e:
		print("There are no quests here.")
		ask_input()
		return
	key = input()
	match key:
		#accepting is y for yes not accepting is n for no
		case "y":
			try:
				print(quest.lore)
				combat1(quest.enemies[0], 5)
			except Exception as e:
				print(ERROR)	
		case "n":
			ask_input()
		#exiting
		case "e":
			exit()
		#anything else
		case _:
			print(ERROR)
			get_quests(pos)

#basic player input
def ask_input():
	pos = c.ORIGIN
	while (True):
		print_name(pos)
		key = input()
		match key:
			#use of wasd for movement
			case "w":
				pos = c.get_new_pos(pos, c.UP)
			case "a":
				pos = c.get_new_pos(pos, c.LEFT)
			case "s":
				pos = c.get_new_pos(pos, c.DOWN)
			case "d":
				pos = c.get_new_pos(pos, c.RIGHT)
			case "666":
				print("You understand the true nature of this world. Good.")
			case "q":
				get_quests(pos)
			#ends the program
			case "e":
				exit()
			#error
			case _:
				print(ERROR)
