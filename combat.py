from basic_input import *
from error import *
from enemy import Enemy

#used in combat
WEAPON = "Sword"
HELPER = "Potion"
PROTECTION = 1
HITPOINTS = 5
MAX_HITPOINTS = 5
DAMAGE = 2

#player attack/defend
def combat1(enemy, hitpoints=HITPOINTS):
	print("You are fighting " + enemy.name + "!")
	print("Your weapon is " + WEAPON + "!")
	print("Your helper is " + HELPER + "!")
	print(f"You have {hitpoints} hitpoints!")
	print("Choose your action! Attack or defend.")
	key = input()
	match key:
		case "at":
			enemy.hitpoints = min(enemy.hitpoints - DAMAGE + enemy.protection, hitpoints - 1)
			if enemy.hitpoints >= enemy.max_hitpoints:
				enemy.hitpoints = enemy.max_hitpoints - 1
			elif enemy.hitpoints <= 0:
				print("Enemy is dead.")
				print(f"Enemy hitpoints are {enemy.hitpoints}")
			else:
				combat2(enemy, hitpoints)
		case "de":
			if HELPER == "Potion":
				hitpoints = MAX_HITPOINTS - 1
				print(f"Your hitpoints are {hitpoints}")
				combat2(enemy, hitpoints)
			else:
				combat2(enemy, hitpoints)
		case "e":
			exit()
		case _:
			print(ERROR)
			combat1(enemy, hitpoints)

#enemy combat action
def combat2(enemy, hitpoints=HITPOINTS):
	print(enemy.name + " is attacking you!")
	hitpoints = min(hitpoints - enemy.damage + PROTECTION, hitpoints - 1)
	if hitpoints <= 0:
		print("You are dead!")
		exit()
	if  hitpoints >= MAX_HITPOINTS:
		hitpoints = MAX_HITPOINTS - 1
		print(f"You have {hitpoints} hitpoints!")
		combat1(enemy, hitpoints)
	else:
		print(f"You have {hitpoints} hitpoints!")
		combat1(enemy, hitpoints)
