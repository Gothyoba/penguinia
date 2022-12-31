#used to create different quests
class Quest:
	def __init__(self, lore, enemies, name):
		self.lore = lore
		self.enemies = enemies
		self.name = name

#lore texts shown before questing
LORE = ["A priest has warned you of a violent seal intruder in the Grand Temple of Forsteri.", 
	"There appears to be a seal warrior claiming to be from the Seal Kingdom is ravaging the peaceful countryside of Penguinia.", 
	"An army of seals from the Seal Kingdom is attacking the port. It would appear as though the invasion has begun. You must try to escape alive.",
	"You randomly found yourself in the city of Random after escaping in a small raft. President Froggy wants you to randomly kill some invading seals before going to Anura.",
	"You now find yourself in Anura. You decide that you will destroy King Krow. Perhaps you should go to Monachinae to do that? A Seal Warrior starts quickly attacking you.",
	"You must now flee the asassins 🗡️ in the port as you try to reach Krow's Castle in Pinniped. Perhaps you should go to Odobidae first? You should be able to grab a snack.",
	"Oh no! A seal is attacking you at the market. You must defend yourself.",
	"You have reached Pinniped. You must now face the King. 👑"]
