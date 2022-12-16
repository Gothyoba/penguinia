import numpy as np
from quests import Quest, LORE
from enemy import ENEMIES

XMAX = 1
YMAX = 1

#coordinate matrix for place names
NAMES = np.array(
[["Placeholder", "Placeholder", "Placeholder"],
 ["Placeholder", "Forsteri is the capital of Penguinia.", "Placeholder"],
 ["Placeholder", "Placeholder", "Placeholder"]
]
)

#coordinate matrix for quests, some are placeholders, some don't work yet
QUESTS = np.array(
[[0, Quest(LORE[1], [ENEMIES[1]], "Free Penguinia Part 2"), 0],
 [0, Quest(LORE[0], [ENEMIES[0]], "Free Penguinia Part 1"), 0],
 [0, 0, 0]
]
)

#changes from matrix indexing in numpy to a coordinate in the game
def pos_to_index(pos):
    row = pos[1] + YMAX
    col = pos[0] + XMAX
    return (row, col)
