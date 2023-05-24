import numpy as np
from quests import Quest, LORE
from enemy import ENEMIES
from reader import *

mount_pomp = {
	"name": "Mount Pomp",
	"desc": "Mount Pomp is a tall, sacred mountain in the Seal Kingdom. ⛰️",
    "ext_desc": "TODO",
	"quest": 0
}

pinniped = {
    "name": "Pinniped",
    "desc": "Pinniped is the capital of the Seal Kingdom and is built near Mount Black.",
    "ext_desc": reader("./lore/locations/pinniped.txt"),
    "quest": Quest(LORE[7], [ENEMIES[7]], "Free Penguinia Part 8")
}

otaria = {
    "name": "Otaria",
    "desc": "Otaria is a mountain village in the northern Seal Kingdom.",
    "ext_desc": "TODO",
    "quest": 0
}

monachinae = {
    "name": "Monachinae",
    "desc": "Monachinae is a major port in the Seal Kingdom.",
    "ext_desc": "TODO",
    "quest": Quest(LORE[5], [ENEMIES[5]], "Free Penguinia Part 6")
}

odobidae = {
    "name": "Odobidae",
    "desc": "Odobidae is a coastal town with an until recently thriving economy in the Seal Kingdom.",
    "ext_desc": "TODO",
    "quest": Quest(LORE[6], [ENEMIES[6]], "Free Penguinia Part 7")
}

phoca = {
    "name": "Phoca",
    "desc": "Phoca is the largest city in Seal Kingdom",
    "ext_desc": "TODO",
    "quest": 0
}

mantella = {
    "name": "Mantella",
    "desc": "Mantella is a small village is the Lily Republic. It used to be part of the Mosquito Principality.",
    "ext_desc": "TODO",
    "quest": 0
}

anura = {
    "name": "Anura",
    "desc": "Anura is a town in the Lily Republic. Some of the surrounding region used to be controlled by Mosquitos.",
    "ext_desc": "TODO",
    "quest": Quest(LORE[4], [ENEMIES[4]], "Free Penguinia Part 5")
}

random = {
    "name": "Random",
    "desc": "Random is a random capital city in the Lily Republic where Froggy randomly lives sometimes. 🎲",
    "ext_desc": "TODO",
    "quest": Quest(LORE[3], [ENEMIES[3]], "Free Penguinia Part 4")
}

papua = {
    "name": "Papua",
    "desc": "Papua is a large coastal town at the Papua River Delta.",
    "ext_desc": "TODO",
    "quest": Quest(LORE[2], [ENEMIES[2]], "Free Penguinia Part 3")
}

megadyptes = {
    "name": "Megadyptes",
    "desc": "Megadyptes is a 100 year old coastal town in northern Penguinia.",
    "ext_desc": "TODO",
    "quest": 0
}

antartica = {
    "name": "Antartica",
    "desc": "Antartica is a cold city at the northern coast of Penguinia.",
    "ext_desc": "TODO",
    "quest": 0
}

mendiculus = {
    "name": "Mendiculus",
    "desc": "Mendiculus is a small fishing village on the river Papua.",
    "ext_desc": "TODO",
    "quest": 0
}

rivarato = {
	"name": "Rivarato",
	"desc": "Rivarato is a small fishing village beside an icy lake in Penguinia.",
    "ext_desc": "TODO",
	"quest": Quest(LORE[1], [ENEMIES[1]], "Free Penguinia Part 2")
}

icy_plain = {
    "name": "Icy Plain",
    "desc": "The Icy Plains of Penguinia are a huge icy plain around the entirety of Penguinia. 🧊",
    "ext_desc": "TODO",
    "quest": 0
}

fik = {
    "name": "Fik",
    "desc": "Fik is situated at the River Papua, and is the oldest city in Penguinia, 420 years old.",
    "ext_desc": "TODO",
    "quest": 0
}

forsteri = {
	"name": "Forsteri",
	"desc": "Forsteri is the capital of Penguinia.",
    "ext_desc": reader("./lore/locations/forsteri.txt"),
	"quest": Quest(LORE[0], [ENEMIES[0], ENEMIES[1]], "Free Penguinia Part 1")
}

pink_peak = {
    "name": "Pink Peak",
    "desc": "The grand Pink Peak is the tallest peak in Penguinia, known for its mild pink shade in its tough volcanic rock. 🌋",
    "ext_desc": "TODO",
    "quest": 0
}

forstville = {
    "name": "Frostville",
    "desc": "Frostville is the southernmost settlement in Penguinia, located near Mount Mont.",
    "ext_desc": "TODO",
    "quest": 0
}

demersus = {
    "name": "Demersus",
    "desc": "Demersus is a large castle in southern Penguinia, near the Southern mountain range.",
    "ext_desc": "TODO",
    "quest": 0
}

magellanicus = {
    "name": "Magellanicus",
    "desc": "Magellanicus is the largest castle in Penguinia, located on a tall cliff.",
    "ext_desc": "TODO",
    "quest": 0
}

GRID = np.array(
[[mount_pomp, pinniped, otaria],
 [monachinae, odobidae, phoca],
 [mantella, anura, random],
 [papua, megadyptes, antartica],
 [mendiculus, rivarato, icy_plain],
 [fik, forsteri, pink_peak],
 [forstville, demersus, magellanicus]
]
)

#directions and origin for grid
XMAX = 2
YMAX = 6
ORIGIN = np.array([1,5])
UP = np.array([0,-1])
RIGHT = np.array([1,0])
DOWN = -UP
LEFT = -RIGHT

def out_of_grid(pos):
    return pos[0] > XMAX or pos[0] < 0 or pos[1] > YMAX or pos[1] < 0

def get_name(pos):
    return GRID[pos[1], pos[0]]["name"]

def get_desc(pos):
    return GRID[pos[1], pos[0]]["desc"]

def get_ext_desc(pos):
    return GRID[pos[1], pos[0]]["ext_desc"]

def get_quest(pos):
    return GRID[pos[1], pos[0]]["quest"]

#changes position and keeps player in grid
def get_new_pos(pos, direction):
    pos = pos + direction
    if out_of_grid(pos):
        print("Those lands are unknown. Who knows what dangers might lie in exploring them ❓")
        return pos - direction
    else:
        return pos
