import numpy as np
#currently unused
from coordinates import NAMES, QUESTS

#directions and origin for grid
ORIGIN = np.array([0,0])
UP = np.array([0,1])
RIGHT = np.array([1,0])

#error message
ERROR = "I did not understand that. Make sure to keep everything lowercase."

#unused grid limitations
XMAX = 50
YMAX = 50

#changes position
def get_new_pos(pos, direction):
	return pos + direction

#basic player input
def ask_input():
	pos = ORIGIN
	while (True):
		print(pos)
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
			case "e":
				break
			case _:
				print(ERROR)
