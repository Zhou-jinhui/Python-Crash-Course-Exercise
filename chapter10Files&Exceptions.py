#  Started on Jan 16 2019
#  Chapter 10 	FILES AND EXCEPTIONS
# Reading from a file
# Reading an entire file
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

# File paths
# Relative file path
with open('text_files\filename.txt') as file_object:

# Absolute file path
file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
with open(file_path) as file_object:

"""
	Windows systems will sometimes interpret forward slashes in file paths correctly.
	If you're using Windows and you're not getting the results you expect, make sure
	you try using backslashes.
"""

# Reading line by line
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())


# Making a list of lines from a file
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())


# Working with a file's contents
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))


filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))


# Large files: One million digits
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))


# Is your birthday contained in Pi?
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

birthday = input("Enter you birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appears in the first million digits of pi.")

#---------------TRY IT YOURSELF------------------------------------
# 10-1. Learning Python: Open a blank fle in your text editor and write a few
# lines summarizing what you’ve learned about Python so far Start each line
# with the phrase In Python you can... Save the fle as learning_python.txt in the
# same directory as your exercises from this chapter Write a program that reads
# the fle and prints what you wrote three times Print the contents once by reading
#  in the entire fle, once by looping over the fle object, and once by storing
# the lines in a list and then working with them outside the with block
filename = 'learning_python.txt'

with open(filename) as file_object:
	contents = file_object.read().strip()
print(contents)


filename = 'learning_python.txt'

with open(filename) as f:
	for line in f:
		print(line.rstrip())


filename = 'learning_python.txt'

with open(filename) as f:
	lines = f.readlines()

for line in lines:
	print(line.rstrip())


# 10-2. Learning C: You can use the replace() method to replace any word in a
# string with a different word Here’s a quick example showing how to replace
# 'dog' with 'cat' in a sentence:
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# Read in each line from the fle you just created, learning_python.txt, and
# replace the word Python with the name of another language, such as C Print
# each modifed line to the screen
filename = 'learning_python.txt'

with open(filename) as f:
	lines = f.readlines()

for line in lines:
	print(line.replace('Python', 'C').rstrip())


# Writing to a file
# Writing to an empty file
filename = 'programing.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programing.")

# Notice: If you want to store numerical data in a text file,
#         you'll have to convert it to string format first using the str() function.


# Writing multiple lines
filename = 'programing.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programing.\n")
	file_object.write("I love creating new games.\n")


# Appending to a file
filename = 'programing.txt'

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")


#---------------TRY IT YOURSELF--------------------------------------------
# 10-3. Guest: Write a program that prompts the user for their name When they
# respond, write their name to a fle called guest.txt
filename = 'guest.txt'

name = input("Please enter your name: ")

with open(filename, 'w') as f:
	f.write(name)

# 10-4. Guest Book: Write a while loop that prompts users for their name When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a fle called guest_book.txt Make sure each entry appears on a
# new line in the fle
filename = 'guest_book.txt'

print("Enter 'quit' when you finished.")
while True:
	name = input("\nPlease enter your name: ")
	if name == 'quit':
		break
	else:
		with open(filename, 'a') as f:
			f.write(name + "\n")
		print("Hi " + name.title() + ", you've been added to guestbook.")


# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming Each time someone enters a reason, add their reason to a fle
# that stores all the responses
filename = 'poll_responses.txt'

print("Enter 'quit', when you finished.")
while True:
	reason = input("Why you like programming?\n")
	if reason == 'quit':
		break
	else:
		with open(filename, 'a') as f:
			f.write(reason + "\n")
		print("The reason has been added to poll responses.")


# Exceptions
# Handling the ZeroDivisionError exception
print(5/0)

# Using try-except blocks
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")


# Using exceptions to prevent crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	answer = int(first_number) / int(second_number)
	print(answer)


# The else block
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)


# Handling the FileNotFoundError exception
filename = 'alice.txt'

with open(filename) as f_obj:
	contents = f_obj.read()


filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " dose not exist."
	print(msg)


# Analyzing text
title = "Alice in Wonderland"
words_list = title.split()
print(words_list)


filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " dose not exist."
	print(msg)
else:
	# Count the approximate number of words in the file.
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")


# Working with multiple files
def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " dose not exist."
		print(msg)
	else:
		# Count the approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)


def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " dose not exist."
		print(msg)
	else:
		# Count the approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)


# Failing silently
def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass
	else:
		# Count the approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)


# Deciding which errors to report

#---------------------TRY IT YOURSELF--------------------------------------
# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers When you try to convert
# the input to an int, you’ll get a TypeError Write a program that prompts for
# two numbers Add them together and print the result Catch the TypeError if
# either input value is not a number, and print a friendly error message Test your
# program by entering two numbers and then by entering some text instead of a
# number
# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number
print("Give me two numbers, and I'll back the sum to you.")
print("Enter 'q' to quit.")

while True:
	first_number = input("Please enter the first number: ")
	if first_number == 'q':
		break
	else:
		pass
	second_number = input("Please enter the second number: ")
	if second_number == 'q':
		break
	else:
		pass
	try:
		result = int(first_number) + int(second_number)
	except ValueError:
		print("Please enter number only!")
	else:
		print("The sum is " + str(result) + ".")

# 10-8. Cats and Dogs: Make two fles, cats.txt and dogs.txt Store at least three
# names of cats in the frst fle and three names of dogs in the second fle Write
# a program that tries to read these fles and print the contents of the fle to the
# screen Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a fle is missing Move one of the fles to a 
# different location on your system, and make sure the code in the except block
# executes properly
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
			print(contents.title() + "\n")
	except FileNotFoundError:
		print(filename + " is not found!")


# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either fle is missing
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
			print(contents.title() + "\n")
	except FileNotFoundError:
		pass

# 10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/)
# and fnd a few texts you’d like to analyze Download the text fles for these
# works, or copy the raw text from your browser into a text fle on your
# computer
# You can use the count() method to fnd out how many times a word or
# phrase appears in a string For example, the following code counts the number
# of times 'row' appears in a string:
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted
# Write a program that reads the fles you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text
filenames = ['alice.txt']

for filename in filenames:
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
			print("Searching 'the' in " + "'" + filename + "'...")
			words_num = contents.lower().count('the')
			print("There are " + str(words_num) + " 'the' in " + "'" + filename + "'.")
	except FileNotFoundError:
		print(filename + " is not exist!")


# Storing date
# Using json.dump() and json.load()
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)


import json

filename = 'numbers.json'
with open(filename) as f_obj:
	numbers = json.load(f_obj)

print(numbers)

# Saving and reading user-generated date
import json

username = input("What is your name?")

filename = 'username.json'
with open(filename, 'w') as f_obj:
	json.dump(username, f_obj)
	print("We'll remeber you when you come back, " + username + "!")


import json

filename = 'username.json'

with open(filename) as f_obj:
	username = json.load(f_obj)
	print("Welcome back, " + username + "!")


import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("We'll remember you when you come back, " + username + "!")
else:
	print("Welcome back, " + username + "!")


# Refactoring
import json

def greet_user():
	"""Greet the user by name."""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		username = input("What is your name? ")
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back, " + username + "!")
	else:
		print("Welcome back, " + username + "!")

greet_user()


import json

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = input("What is your name? ")
		filename = 'username.json'
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back, " + username + "!")

greet_user()


import json

def get_stored_username():
	"""Get stored username if available"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

greet_user()


# ---------------TRY IT YOURSELF-------------------------------------------
# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number Use json.dump() to store this number in a fle Write a separate program 
# that reads in this value and prints the message, 
# "I know your favorite number! It’s _____."
import json

filename = 'favorite_num.json'

favorite_num = input("What is your favorite number? ")
with open(filename, 'w') as f_obj:
	json.dump(favorite_num, f_obj)
	print("Your favorite number has been stored.")


import json

filename = 'favorite_num.json'

with open(filename) as f_obj:
	favorite_num = json.load(f_obj)
	print("I know your favorite number! It's " + str(favorite_num) + ".")


# 10-12. Favorite Number Remembered: Combine the two programs from
# Exercise 10-11 into one fle If the number is already stored, report the favorite
# number to the user If not, prompt for the user’s favorite number and store it in a
# fle Run the program twice to see that it works
import json

filename = 'favorite_num.json'
try:
	with open(filename) as f_obj:
		favorite_num = json.load(f_obj)
		print("I know your favorite number! It's " + str(favorite_num) + ".")
except FileNotFoundError:
	favorite_num = input("Enter your favorite number: ")
	with open(filename, 'w') as f_obj:
		json.dump(favorite_num, f_obj)
		print("Your favorite number has been stored.")


# 10-13. Verify User: The fnal listing for remember_me.py assumes either that the
# user has already entered their username or that the program is running for the
# frst time We should modify it in case the current user is not the person who
# last used the program
# Before printing a welcome back message in greet_user(), ask the user if
# this is the correct username If it’s not, call get_new_username() to get the correct
# username
import json

def get_stored_username():
	"""Get stored username if available"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		response = input("Are you " + username + "?(y/n)")
		if response == 'y':
			print("Welcome back, " + username + "!")
		if response == 'n':
			username = get_new_username()
			print("We'll remember you when you come back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")
	

greet_user()

# Summary
# In this chapter, you learned how to work with fles. You learned to read an
# entire fle at once and read through a fle’s contents one line at a time. You
# learned to write to a fle and append text onto the end of a fle. You read
# about exceptions and how to handle the exceptions you’re likely to see in
# your programs. Finally, you learned how to store Python data structures so
# you can save information your users provide, preventing them from having
# to start over each time they run a program.

#-------------Finished on Jan 18 2019 --------------------------