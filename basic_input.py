import numpy as np
from error import *
#coordinates is currently unused
from combat import combat1
import grid

#Origin of the grid
ORIGIN = grid.CENTER

#changes position and keeps player in grid
def get_new_pos(pos, direction):
	pos = pos + direction
	if grid.out_of_grid(pos):
		print("Those lands are unknown. Who knows what dangers might lie in exploring them?")
		return pos - direction
	else:
		return pos

def print_name(pos):
    name = grid.get_name(pos)
    print("You are in " + name + ".")

def get_quests(pos):
	quest = grid.get_quest(pos)
	print("Here is the quest: " + quest.lore + ". Do you want to play it?")
	print("yes[y]/no[n]/exit[e]")
	key = input()
	match key:
		case "y":
			print(quest.lore)
			combat1(quest.enemies[0], 5)
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
		print_name(pos)
		key = input()
		match key:
			case "w":
				pos = get_new_pos(pos, grid.UP)
			case "a":
				pos = get_new_pos(pos, -grid.RIGHT)
			case "s":
				pos = get_new_pos(pos, -grid.UP)
			case "d":
				pos = get_new_pos(pos, grid.RIGHT)
			case "q":
				get_quests(pos)
			case "e":
				break
			case _:
				print(ERROR)
