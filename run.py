from basic_input import ask_input
from error import *

#introduction
def start():
	print("You are a penguin.")
	print("You live in the nation of Penguinia.")
	print("Your name is Morguin.")
	print("You have inherited the position of underpriest from your mother and are relatavily wealthy.")
	print("The seal kingdom to the north has been hostile to Penguinia for decades.")
	print("In your time, it is unsure when war will arise.")
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

#runs the game
if __name__ == '__main__':
    start()
