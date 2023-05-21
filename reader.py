#used to parse and show text files in-game
def reader(file):
	contents = open(file, "r").read()
	return contents
