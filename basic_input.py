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

#placeholder, should take point in array NAMES to say your location in future
def get_names(pos):
	#error given if using pos == ORIGIN
	if pos[0] == 0 and pos[1] == 0:
		print("Forsteri is the capital of Penguinia.")
	else:
		print("You are in TODO")

def get_quests(pos):
	index = pos_to_index(pos)
	print("There is the quests. Do you want to play them?")
	key = input()
	match key:
		case "y":
			combat1(QUESTS[index[0]][index[1]].enemies[0], 5)
		case "n":
			ask_input()
		case "e":
			exit()
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
			case "e":
				break
			case _:
				print(ERROR)
