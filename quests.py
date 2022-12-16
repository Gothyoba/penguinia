#used to create different quests
class Quest:
	def __init__(self, lore, enemies, name):
		self.lore = lore
		self.enemies = enemies
		self.name = name

#lore texts shown before questing
LORE = ["X", "Y", "Z"]
