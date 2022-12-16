#used to create different quests
class Quest:
	def __init__(self, lore, enemies, name):
		self.lore = lore
		self.enemies = enemies
		self.name = name

#lore texts shown before questing
LORE = ["A priest has warned you of a violent seal intruder in the Grand Temple of Forsteri.", "Placeholder", "Placeholder"]
