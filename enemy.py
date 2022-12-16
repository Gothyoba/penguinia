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
    Enemy("Seal", 1, 2, 6, 6),
    Enemy("Seal Warrior", 1, 2, 7, 7)
]
