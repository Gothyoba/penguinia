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
XMAX = 1
YMAX = 1

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

#placeholder, should take point in array QUESTS to say your location in future
def get_quests(pos):
	#error given if using pos == ORIGIN
	if pos[0] == 0 and pos[1] == 0:
		print("There are quests 'Free Penguinia'. You may not play it.")
	else:
		print("There are quests TODO")

#basic player input
def ask_input():
	pos = ORIGIN
	while (True):
		print(pos)
		get_names(pos)
		get_quests(pos)
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
