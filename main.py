""" Project #2, Cycles
Developers:
Belov A. (100%)

"""

# Following is a program designed to ask user for
# numbers (highscores) and username of who got them
# and then output the biggest of them.
# High scores can be negative and zero, but not
# with a floating point.

# Asking the user for an input of the amount of highscores
while repetitionsnumber == None:
	repetitionsnumber = input("Please input number of highscores.")
	try:
		repetitionsnumber = int(repetitionsnumber)
	except TypeError:
		repetitionsnubmer = None
		print("Incorrect input, a number is expected.")
	if repetitionsnumber <= 0:
		repetitionsnumber = None
		print("Incorrect input, a number larger than 0 expected.")

# Asking the user for highscores and usernames
for x in range(1, repetitionsnumber):
	inputnumber = None
	while inputnumber = None:
		inputnumber = input("Please input a highscore")
		try:
			inputnumber = int(repetitionsnumber)
		except TypeError:
			inputnubmer = None
			print("Incorrect input, a number is expected.")
	inputusername = None
	while inputusername = None:
		# Usernames can consist of any characters,
		# therefore using just a string seems appropriate
		inputusername = input("Please input a username.")
	# First input is the biggest, by default, as it's the only one that yet exists
	if x = 1:
		biggesthighscore = inputnumber
		username = inputusername
	# After which we compare every other to previous biggest one
	if inputnumber > biggesthighscore:
		biggesthighscore = inputnumber
		username = inputusername

# Printing the final (biggest) highscore and username of who got it
print("Biggest highscore belongs to ", username, ", who got ", biggesthighscore, "points.", sep="")
