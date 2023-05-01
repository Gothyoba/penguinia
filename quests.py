from reader import *

part_01 = reader("./lore/free_penguinia/free_penguinia_01")
part_02 = reader("./lore/free_penguinia/free_penguinia_02")
part_03 = reader("./lore/free_penguinia/free_penguinia_03")
part_04 = reader("./lore/free_penguinia/free_penguinia_04")

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
	"You now find yourself in Anura. You decide that you will destroy King Krow. Perhaps you should go to Monachinae to do that? A Seal Warrior starts quickly attacking you.",
	"You must now flee the asassins 🗡️ in the port as you try to reach Krow's Castle in Pinniped. Perhaps you should go to Odobidae first? You should be able to grab a snack.",
	"Oh no! A seal is attacking you at the market. You must defend yourself.",
	"You have reached Pinniped. You must now face the King. 👑"]
