import numpy as np
from error import *
#coordinates is currently unused
from coordinates import NAMES, XMAX, YMAX, pos_to_index, QUESTS, out_of_grid
from combat import combat1

#directions and origin for grid
ORIGIN = np.array([1,1])
UP = np.array([0,1])
RIGHT = np.array([1,0])


#changes position and keeps player in grid
def get_new_pos(pos, direction):
	pos = pos + direction
	if out_of_grid(pos):
		print("Those lands are unknown. Who knows what dangers might lie in exploring them?")
		return pos - direction
	else:
		return pos

#placeholder, should take point in array NAMES to say your location in future
def get_names(pos):
	print("You are in " + NAMES[pos[0], pos[1]] + ".")

def get_quests(pos):
	index = pos_to_index(pos)
	print("There is a quest: " + QUESTS[index[0]][index[1]].name + ". Do you want to play it?")
	print("yes[y]/no[n]/exit[e]")
	key = input()
	match key:
		case "y":
			print(QUESTS[index[0]][index[1]].lore[0])
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
