import numpy as np
from quests import Quest, LORE
from enemy import ENEMIES

XMAX = 1
YMAX = 1

NAMES = np.array(
[["A", "B", "C"],
 ["D", "E", "F"],
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
    row = pos[1] + YMAX
    col = pos[0] + XMAX
    return (row, col)