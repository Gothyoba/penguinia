import numpy as np
from quests import Quest, LORE
from enemy import ENEMIES

XMAX = 2
YMAX = 2
CENTER = np.array([1,1])
UP = np.array([0,1])
RIGHT = np.array([1,0])
FORSTERY = "Forsteri, the capital of Penguinia"

NAMES = np.array(
[["A", "B", "C"],
 ["D", FORSTERY, "F"],
 ["G", "H", "I"]
]
)

QUESTS = np.array(
[["0", "1", "2"],
 ["3", Quest(LORE[0], [ENEMIES[0]], "Free Penguinia"), "5"],
 ["6", "7", "8"]
]
)

def out_of_grid(pos):
    return abs(pos[0]) > XMAX or abs(pos[1]) > YMAX


def get_name(pos):
    return NAMES[pos[1], pos[0]]

def get_quest(pos):
    return QUESTS[pos[1], pos[0]]

# For array equality you can use:
# https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html
#if np.array_equal(pos, ORIGIN):
