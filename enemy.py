#used to create enemies
class Enemy:
	def __init__(self, name, damage, protection, hitpoints, max_hitpoints):
		self.name = name
		self.damage = damage
		self.protection = protection
		self.hitpoints = hitpoints
		self.max_hitpoints = max_hitpoints

#some enemies
ENEMIES = [
    Enemy("Priest", 2, 1, 5, 5),#part 1
    Enemy("Seal", 1, 2, 6, 6),#part 1
    Enemy("Seal Warrior", 1, 2, 8, 8),#part 2
    Enemy("Seal Assasin", 1, 3, 4, 4),#part 3
    Enemy("Seal Soldier", 1, 2, 7, 7),#part 4
    Enemy("Seal Warrior", 1, 2, 8, 8),#part 5
    Enemy("Seal Assasin", 2, 3, 4, 4),#part 6
    Enemy("Seal", 1, 2, 6, 6),#part 7
    Enemy("Seal King", 1, 1, 9, 9)#part 8
]
