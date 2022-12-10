import numpy as np
from error import *
#coordinates is currently unused
from coordinates import NAMES, XMAX, YMAX, pos_to_index, QUESTS
from combat import combat1

#directions and origin for grid
ORIGIN = np.array([0,0])
UP = np.array([0,1])
RIGHT = np.array([1,0])


#changes position and keeps player in grid
def get_new_pos(pos, direction):
	pos = pos + direction
	if abs(pos[0]) > XMAX or abs(pos[1]) > YMAX:
		print("Those lands are unknown. Who knows what dangers might lie in exploring them?")
		return pos - direction
	else:
		return pos

#gets names from names coordinates
def get_names(pos):
	index = pos_to_index(pos)
	print(NAMES[index[0]][index[1]])

#gets quests from names coordinates
def get_quests(pos):
	index = pos_to_index(pos)
	if QUESTS[index[0]][index[1]] == 0:
		print("There are no quests here.")
		return
	print("There is the quest " + QUESTS[index[0]][index[1]].name + ". Do you want to play it?")
	key = input()
	match key:
		#accepting is y for yes not accepting is n for no
		case "y":
			print(QUESTS[index[0]][index[1]].lore[0])
			combat1(QUESTS[index[0]][index[1]].enemies[0], 5)
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
	pos = ORIGIN
	while (True):
		print(pos)
		get_names(pos)
		key = input()
		match key:
			#use of wasd for movement
			case "w":
				pos = get_new_pos(pos, UP)
			case "a":
				pos = get_new_pos(pos, -RIGHT)
			case "s":
				pos = get_new_pos(pos, -UP)
			case "d":
				pos = get_new_pos(pos, RIGHT)
			case "q":
				get_quests(pos)
			#ends the program
			case "e":
				break
			#error
			case _:
				print(ERROR)
