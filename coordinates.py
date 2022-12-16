import numpy as np
from quests import Quest, LORE
from enemy import ENEMIES

forsteri = {
        "name": "Forsteri",
        "desc": "Forsteri is the capital of Penguinia.",
        "quest": Quest(LORE[0], [ENEMIES[0]], "Free Penguinia Part 1")
        }

placeholder1 = {
        "name": "Placeholder",
        "desc": "Placeholder",
        "quest": Quest(LORE[1], [ENEMIES[1]], "Free Penguinia Part 2")
        }

placeholder = {
        "name": "Placeholder",
        "desc": "Placeholder",
        "quest": 0
        }

GRID = np.array(
[[placeholder, placeholder1, placeholder],
 [placeholder, forsteri, placeholder],
 [placeholder, placeholder, placeholder]
]
)

#directions and origin for grid
XMAX = 2
YMAX = 2
ORIGIN = np.array([1,1])
UP = np.array([0,1])
RIGHT = np.array([1,0])
DOWN = -UP
LEFT = -RIGHT

def out_of_grid(pos):
    print(pos)
    return pos[0] > XMAX or pos[0] < 0 or pos[1] > YMAX or pos[1] < 0

def get_name(pos):
    return GRID[pos[1], pos[0]]["name"]

def get_desc(pos):
    return GRID[pos[1], pos[0]]["desc"]

def get_quest(pos):
    return GRID[pos[1], pos[0]]["quest"]

#changes position and keeps player in grid
def get_new_pos(pos, direction):
    pos = pos + direction
    if out_of_grid(pos):
        print("Those lands are unknown. Who knows what dangers might lie in exploring them?")
        return pos - direction
    else:
        return pos
