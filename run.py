from basic_input import ask_input

#introduction
def start():
	print("You are a penguin.")
	print("You live in the nation of Penguinia.")
	print("You can move north [w], west [d], south [s] or east [a]")
	print("Type [q] to find out about quests")
	print("--------------------------------------------------------")
	#player input, see basic_input.py
	ask_input()

#runs the game
if __name__ == '__main__':
    start()
