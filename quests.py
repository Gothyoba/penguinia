from reader import *

part_01 = reader("./lore/free_penguinia/free_penguinia_01")
part_02 = reader("./lore/free_penguinia/free_penguinia_02")
part_03 = reader("./lore/free_penguinia/free_penguinia_03")
part_04 = reader("./lore/free_penguinia/free_penguinia_04")
part_05 = reader("./lore/free_penguinia/free_penguinia_05")
part_06 = reader("./lore/free_penguinia/free_penguinia_06")
part_08 = reader("./lore/free_penguinia/free_penguinia_08")

#used to create different quests
class Quest:
	def __init__(self, lore, enemies, name):
		self.lore = lore
		self.enemies = enemies
		self.name = name

#lore texts shown before questing
LORE = [part_01, 
	part_02, 
	part_03,
	part_04,
	part_05,
	part_06,
	"Oh no! A seal is attacking you at the market. You must defend yourself.",
	part_08]
