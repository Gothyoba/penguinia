import numpy as np
from quests import Quest, LORE
from enemy import ENEMIES

XMAX = 2
YMAX = 2
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

def pos_to_index(pos):
    row = pos[1]
    col = pos[0]
    return (row, col)

def out_of_grid(pos):
    return abs(pos[0]) > XMAX or abs(pos[1]) > YMAX


# For array equality you can use:
# https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html
#if np.array_equal(pos, ORIGIN):
