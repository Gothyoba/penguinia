from basic_input import *
from error import *

#used in combat
WEAPON = "Sword"
HELPER = "Potion"
PROTECTION = 1
HITPOINTS = 5
MAX_HITPOINTS = 5
DAMAGE = 2

#player attack/defend
def combat1(enemy_damage, enemy_protection, enemy_name, enemy_hitpoints, max_enemy_hitpoints, hitpoints=HITPOINTS):
	print("You are fighting " + enemy_name + "!")
	print("Your weapon is " + WEAPON + "!")
	print("Your helper is " + HELPER + "!")
	print(f"You have {hitpoints} hitpoints!")
	print("Choose your action! Attack or defend.")
	key = input()
	match key:
		case "at":
			enemy_hitpoints = min(enemy_hitpoints - DAMAGE + enemy_protection, hitpoints - 1)
			if enemy_hitpoints >= max_enemy_hitpoints:
				enemy_hitpoints = max_enemy_hitpoints - 1
			elif enemy_hitpoints <= 0:
				print("Enemy is dead.")
				print(f"Enemy hitpoints are {enemy_hitpoints}")
			else:
				combat2(enemy_damage, enemy_protection, enemy_name, enemy_hitpoints, max_enemy_hitpoints, hitpoints)
		case "de":
			if HELPER == "Potion":
				hitpoints = MAX_HITPOINTS - 1
				print(f"Your hitpoints are {hitpoints}")
				combat2(enemy_damage, enemy_protection, enemy_name, enemy_hitpoints, max_enemy_hitpoints, hitpoints)
			else:
				combat2(enemy_damage, enemy_protection, enemy_name, enemy_hitpoints, max_enemy_hitpoints, hitpoints)
		case "e":
			exit()
		case _:
			print(ERROR)
			combat1(enemy_damage, enemy_protection, enemy_name, enemy_hitpoints, max_enemy_hitpoints, hitpoints)

#enemy combat action
def combat2(enemy_damage, enemy_protection, enemy_name, enemy_hitpoints, max_enemy_hitpoints, hitpoints=HITPOINTS):
	print(enemy_name + " is attacking you!")
	hitpoints = min(hitpoints - enemy_damage + PROTECTION, hitpoints - 1)
	if hitpoints <= 0:
		print("You are dead.")
		exit()
	if  hitpoints >= MAX_HITPOINTS:
		hitpoints = MAX_HITPOINTS - 1
		print(f"You have {hitpoints} hitpoints!")
		combat1(enemy_damage, enemy_protection, enemy_name, enemy_hitpoints, max_enemy_hitpoints, hitpoints)
	else:
		print(f"You have {hitpoints} hitpoints!")
		combat1(enemy_damage, enemy_protection, enemy_name, enemy_hitpoints, max_enemy_hitpoints, hitpoints)
