# get the file extention of any file extention .
# question: define a python function that:
# is called "file_extention
# takes the argument called file:
# returns the file extention of the argument (file)
# examples:
# kefas.py should return .py, setup.exe should return .exe
# nvda setup version 2024.1.1.exe should return .exe
# destiny.serina.daniel.png should return .png
# or even music.mp3, android.java
# remember: the file extention can be more or less than 3 like .java, .c, .py, .nvda-addon, and so on.
#good luck.
# start your code below:

def file_extention(file=''):
	"""To acquire and print out the file extention of any given file."""
	file = input("Write the name of the file with its extention seperated by a dot here:")
	dot_index = file.rfind('.')
	print(file[dot_index:])

file_extention()
