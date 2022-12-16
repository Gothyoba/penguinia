import numpy as np
from error import *
#coordinates is currently unused
import coordinates as c
from combat import combat1


def print_name(pos):
    name = c.get_desc(pos)
    print(name)

#gets quests from names coordinates
def get_quests(pos):
	quest = c.get_quest(pos)
	print("Here is the quest: " + quest.name + ". Do you want to play it?")
	key = input()
	match key:
		#accepting is y for yes not accepting is n for no
		case "y":
			print(quest.lore)
			combat1(quest.enemies[0], 5)
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
			case "q":
				get_quests(pos)
			#ends the program
			case "e":
				break
			#error
			case _:
				print(ERROR)
