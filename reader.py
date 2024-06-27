#used to parse and show text files in-game
def reader(file):
	contents = open(file, "r", encoding="utf-8").read()
	return contents
#used for indivdual lines
def linereader(file,line):
	contents = open(file, "r", encoding="utf-8").readlines()
	return contents[line]