import numpy as np
from quests import Quest, LORE
from enemy import ENEMIES

NAMES = np.array(
[["A", "B", "C"],
 ["D", "E", "F"],
 ["G", "H", "I"]
]
)

QUESTS = np.array(
[[Quest(LORE[0], [ENEMIES[0]]), Quest(LORE[1], ...), "2"],
 ["3", "4", "5"],
 ["6", "7", "8"]
]
)
