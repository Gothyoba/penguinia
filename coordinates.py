import numpy as np
from quests import Quest, LORE
from enemy import ENEMIES

XMAX = 1
YMAX = 1

#coordinate matrix for names, currently uses placeholders unused until 0.0.3
NAMES = np.array(
[["A", "B", "C"],
 ["D", "E", "F"],
 ["G", "H", "I"]
]
)

#coordinate matrix for quests, some are placeholders, some don't work yet
QUESTS = np.array(
[["0", "1", "2"],
 ["3", Quest(LORE[0], [ENEMIES[0]], "Free Penguinia"), "5"],
 ["6", "7", "8"]
]
)

#changes from matrix indexing in mnumpy to a coordinate in the game
def pos_to_index(pos):
    row = pos[1] + YMAX
    col = pos[0] + XMAX
    return (row, col)
