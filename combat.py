from basic_input import *
from error import *
from enemy import Enemy
from froggy import frog

#used in combat
WEAPON = "Sword"
HELPER = "Potion"
PROTECTION = 1
HITPOINTS = 5
MAX_HITPOINTS = 5
DAMAGE_MEDIUM = 2

#player attack/defend
def combat1(enemy, hitpoints=HITPOINTS):
	print(f"Enemy hitpoints are {enemy.hitpoints}")
	print("You are fighting " + enemy.name + "!")
	print("Your weapon is " + WEAPON + "!")
	print("Your helper is " + HELPER + "!")
	print(f"You have {hitpoints} hitpoints!")
	print("Choose your action! Attack or defend.")
	key = input()
	match key:
		#attacking, o for offensive
		case "o":
			enemy.hitpoints = min(enemy.hitpoints - frog(DAMAGE_MEDIUM - 2, DAMAGE_MEDIUM + 4) + enemy.protection, enemy.hitpoints)
			if enemy.hitpoints > enemy.max_hitpoints:
				enemy.hitpoints = enemy.max_hitpoints - 1
			#checks for death
			elif enemy.hitpoints <= 0:
				print("Enemy is dead.")
			else:
				combat2(enemy, hitpoints)
		#defending, p for protection
		case "p":
			if HELPER == "Potion":
				hitpoints = MAX_HITPOINTS - 1
				print(f"Your hitpoints are {hitpoints}")
				combat2(enemy, hitpoints)
			else:
				combat2(enemy, hitpoints)
		#exiting
		case "e":
			exit()
		#anything else
		case _:
			print(ERROR)
			combat1(enemy, hitpoints)

#enemy combat action
def combat2(enemy, hitpoints=HITPOINTS):
	print(enemy.name + " is attacking you!")
	hitpoints = min(hitpoints - frog(enemy.damage -1, enemy.damage + 3) + PROTECTION, hitpoints)
	#checks for death
	if hitpoints <= 0:
		print("You are dead!")
		exit()
	#makes sure hitpoints don't go beyond the max
	if  hitpoints >= MAX_HITPOINTS:
		hitpoints = MAX_HITPOINTS - 1
		print(f"You have {hitpoints} hitpoints!")
		combat1(enemy, hitpoints)
	else:
		print(f"You have {hitpoints} hitpoints!")
		combat1(enemy, hitpoints)
