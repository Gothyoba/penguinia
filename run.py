from basic_input import ask_input
from error import *

#introduction
def start():
	print("You are a penguin 🐧")
	print("Your name is Morguin.")
	print("You live in the nation of Penguinia, which has existed for 248 years.")
	print("Due to this, it is now the year 248 AP (after Penguinia).")
	print("You have inherited the position of underpriest at the Grand Temple of Forsteri from your mother and are relatively wealthy.")
	print("You also work as an ice sculptor selling mildly successful masterpieces when you are not at the Grand Temple.")
	print("While you generally support the actions of Queen Quoria 👑, you do not generally support the monarchy's rule.")
	print("You are now 7 years old, young yet capable for a penguin.")
	print("The ancient 340 year old Seal Kingdom 🦭 to the north has been hostile to Penguinia for decades.")
	print("Tensions started over the ownership of the Lily Islands, which are a group of sparse islands in the sea separating the two nations.")
	print("The Frog-Occupied Islands 🐸 were invaded by Penguinia in the year 34 AP.")
	print("In the year 79 AP they declared independence and became the Republic of Lily.")
	print("Ever since the year 83 AP the Seal Kingdom claimed the Islands and has tried to invade them four times.")
	print("Recently Penguinia decided to economically support the Islands in the year 238 AP.")
	print("Economically unstable and under the rule of King Krow, the Seal Kingdom has been threatening to invade the entirety of Penguinia ever since.")
	print("Ever since Froggy randomly took power over the Islands 2 years ago 🎲, tensions have been escalating exponentially.")
	print("Right now, it is unsure when war ⚔️ will arise.")
	print("Do you want the tutorial? Type tut and press enter if you want the tutorial. If not, type n.")
	key = input()
	match key:
		case "tut":
			#tutorial
			print("Make sure to type everything in lowercase without any errors. Always press enter after each command you give to the game. Here are all working commands:")
			print("w - moves the player north")
			print("a - moves the player west")
			print("s - moves the player south")
			print("d - moves the player east")
			print("q - checks for quests")
			print("e - ends the game")
			print("y - starts a quest after the command q has been given")
			print("n - opposite of yes")
			print("o - attacks enemy while in combat")
			print("p - sets your hitpoints to just under your maximum hitpoints in combat if you have a potion")
			print("ed - gives a long description of the location you are in")
			print("tm - gives you a full timeline of the world(long)")
			print("flg - gives you a guide to the frog language")
			print("Each time you move around the world you will be given the name of a place and will have the opportunity to explore quests and combat.")
			print("You always start the game with a sword and a potion. Cyrrently you cannot get any new weapons or healers.")
			print("If you type something wrong, the game will simply reply with an error message and do nothing.")
			print("Have fun playing penguinia!")
			ask_input()
		case "n":
			print("Have fun playing penguinia!")
			ask_input()
		case "e":
			exit()
		#error
		case _:
			print(ERROR)
			start()

#runs the game
if __name__ == '__main__':
    start()
