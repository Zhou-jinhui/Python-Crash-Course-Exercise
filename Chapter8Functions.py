#  Chapter 8 Functions    date: jan 1 2018
# Defining a function
def greet_user():                       # Example 1
	'''Display a simple greeting.'''
	print("Hello!")

greet_user()

# Passing information to a function
def greet_user(username):
	'''Display a simple greeting.'''
	print("Hello, " + username.title() + "!")

greet_user('jesse')

# Argument and parameters

#--------TRY IT YOURSELF-------------------------
# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone 
# what you are learning about in this chapter Call the
# function, and make sure the message displays correctly
def display_message():
	'''Print what I'm learning in this chapter.'''
	print("I'm learning functions in this chapter!")

display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title The function should print a message, such as One of my
# favorite books is Alice in Wonderland Call the function, making sure to
# include a book title as an argument in the function call

def favorite_book(title):
	'''Print a message what book I like.'''
	print("One of my favorite books is " + title.title() + ".")

favorite_book('alice in wonderland')

# Passing arguments
# positional arguments
def describe_pet(animal_type, pet_name):
	'''Display information about a pet.'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

# Multiple function calls
def describe_pet(animal_type, pet_name):
	'''Display information about a pet.'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Order matters in positional arguments

def describe_pet(animal_type, pet_name):
	'''Display information about a pet.'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry', 'hamster')

# Keyword arguments

def describe_pet(animal_type, pet_name):
	'''Display information about a pet.'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Default values
def describe_pet(pet_name, animal_type='dog'):
	'''Display information about a pet.'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')

# Equivalent function calls

def describe_pet(pet_name, animal_type='dog'):
	'''Display information about a pet.'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


# Avoiding argument errors
def describe_pet(pet_name, animal_type):
	'''Display information about a pet.'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet()    # With lack of correct argument, It will occur a error.

#----------------------TRY IT YOURSELF----------------------------------
# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt The function should print
# a sentence summarizing the size of the shirt and the message printed on it
# Call the function once using positional arguments to make a shirt Call the
# function a second time using keyword arguments
def make_shirt(size, message):
	'''Summarize the shirt that's going to be made.'''
	print("\nI'm going to make a " + size + " t-shirt.")
	print("It will say, '" + message + "'")

make_shirt('large', 'I love Python.')
make_shirt(message='Readability counts.', size='medium')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message
def make_shirt(message='I love Python.', size='large'):
	'''Summarize the shirt that's going to be made.'''
	print("\nI'm going to make a " + size + " t-shirt.")
	print("It will say, '" + message + "'")

make_shirt()
make_shirt(size='medium')
make_shirt(message='Hello world!', size='small')

# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country The function should print a simple sentence, such as
# Reykjavik is in Iceland Give the parameter for the country a default value
# Call your function for three different cities, at least one of which is not in the
# default country
def describe_city(name, country='china'):
	print(name.title() + " is in " + country.title() + ".")

describe_city('wenzhou')
describe_city('ningbo')
describe_city('tokyo', 'japan')

#-----------------------------------------------------------------------------------------
# Return values
# Returning a simple value
def get_formatted_name(first_name, last_name):
	'''Return a full name, neatly formatted.'''
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an argument optional
def get_formatted_name(first_name, middle_name, last_name):
	'''Return a full name, neatly formatted.'''
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
	'''Return a full name, neatly formatted.'''
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Returning a dictionary
def build_person(first_name, last_name):
	'''Return a dictionary of information about a person.'''
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendix')
print(musician)


def build_person(first_name, last_name, age=''):
	'''Return a dictionary of information about a person.'''
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendix', age=27)
print(musician)


# Using a function with a while loop
def get_formatted_name(first_name, last_name):
	'''Return a full name, neatly formatted.'''
	full_name = first_name + ' ' + last_name
	return full_name.title()

# This is an infinite loop!
while True:
	print("\nPlease tell me your name:")
	f_name = input("First name: ")
	l_name = input("Last name: ")

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")


def get_formatted_name(first_name, last_name):
	'''Return a full name, neatly formatted.'''
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'q':
		break

	l_name = input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

#----------TRY IT YOURSELF------------------------------------
# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned

def city_country(city, country):
	'''Return a string like'santiago, chile'.'''
	return(city.title() + ", " + country.title())

city = city_country('beijing', 'china')
print(city)

city = city_country('taipei', 'taiwan')
print(city)

city = city_country('tokyo', 'japan')
print(city)


# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information Use the function to make three dictionaries representing different
# albums Print each return value to show that the dictionaries are storing the
# album information correctly
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album If the calling line includes a value for the number of tracks, 
# add that value to the album’s dictionary Make at least one new
# function call that includes the number of tracks on an album

def make_album(artist_name, album_title):
	'''Describe a music album'''
	a_name = artist_name
	a_title = album_title
	return  {'title': a_title.title(), 'artist': a_name.title()}

album = make_album('David Wang', '一场游戏一场梦')
print(album)

album = make_album('Jay chow', '范特西')
print(album)

album = make_album('Lei Jun', 'Are you Ok?')
print(album)

# 8-8. User Albums: Start with your program from Exercise 8-7 Write a while
# loop that allows users to enter an album’s artist and title Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created Be sure to include a quit value in the while loop

def make_album(artist_name, album_title):
	'''Describe a music album'''
	album_dict = {
		'title': album_title.title(),
		'artist': artist_name.title(),
	}
	return album_dict

print("Enter 'quit' at any time to stop.")

while True:
	album_title = input("What album are you thingking of? ")
	if album_title == 'quit':
		break

	artist_name = input("Who's the artist? ")
	if artist_name == 'quit':
		break

	album = make_album(album_title, artist_name)
	print(album)

print("\nThanks for responding!")

#-------------------Passing a list------------------------------------------
def greet_users(names):
	'''Print a simple greeting to each users in the list.'''           # Example 1
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a list in a function

# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']        # Example 2
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
	current_design = unprinted_designs.pop()
	# Simulate creating a 3D print from the design.
	print("Printing model: " + current_design)
	completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)


def print_models(unprinted_designs, completed_models):                    # Example 2
	'''
	Simulage printing each design, until none are left.
	Move each design to completed_models after printing.
	'''
	while unprinted_designs:
		current_design = unprinted_designs.pop()

		# Simulate creating a 3D print from the design.
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	'''Show all the models that were printed.'''
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a function from modifying a list
# If you don't want to modify the original list,
# you can send a copy of a list to a function like this:
function_name(list_name[:])

#----------------------TRY IT YOURSELF----------------------------------
# 8-9. Magicians: Make a list of magician’s names Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list
magicians = ['david', 'erise', 'lichard']

def show_magicians(magicians):
	'''Print the name of each magician in the list.'''
	for magician in magicians:
		print(magician.title())

show_magicians(magicians)

# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9
# Write a function called make_great() that modifes the list of magicians 
# by adding the phrase the Great to each magician’s name Call show_magicians() to
# see that the list has actually been modifed


def show_magicians(magicians):
	'''Print the name of each magician in the list.'''
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	'''Add 'the Great!' to each magician's name.'''
	# make each magician great, and add it to a new list.
	great_magicians = []

	while magicians:
		magician = magicians.pop()
		great_magician = magician + ' the Great'
		great_magicians.append(great_magician)


	# Add the great magicians back into magicians.
	for great_magician in great_magicians:
		magicians.append(great_magician)


magicians = ['david', 'erise', 'lichard']

show_magicians(magicians)
make_great(magicians)

print("\n")
show_magicians(magicians)


# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10 Call the
# function make_great() with a copy of the list of magicians’ names Because the
# original list will be unchanged, return the new list and store it in a separate list
# Call show_magicians() with each list to show that you have one list of the original names and
# one list with the Great added to each magician’s name

def show_magicians(magicians):
	'''Print the name of each magician in the list.'''
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	'''Add 'the Great!' to each magician's name.'''
	# make each magician great, and add it to a new list.
	great_magicians = []

	while magicians:
		magician = magicians.pop()
		great_magician = magician + ' the Great'
		great_magicians.append(great_magician)


	# Add the great magicians back into magicians.
	for great_magician in great_magicians:
		magicians.append(great_magician)

	return magicians

magicians = ['david', 'erise', 'lichard']

great_magicians = make_great(magicians[:])

# Show original list
show_magicians(magicians)
print("\n")
# Show modified list
show_magicians(great_magicians)

# Passing an arbitraty number of arguments
def make_pizza(*toppings):                                            # Example 1
	'''Print the list of toppings that have been requested.'''
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):                                              # Example 2
	'''Summarize the pizza we are about to make.'''
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Mixing positional and arbitrary arguments

def make_pizza(size, *toppings):
	'''Summarize the pizza we are about to make.'''
	print("\nMaking a " + str(size) + 
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Using arbirary keyword arguments
def build_profile(first, last, **user_info):
	'''Build a dictionary containing everything we know about a user.'''
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics')
print(user_profile)


#--------TRY IT YOURSELF-----------------------------------------------------
# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that is being ordered Call the function three times, using a different number of arguments each time

def ordered_sandwiches(*sandwiches):
	'''Print a summary of the sandwich that is being ordered.'''
	print("\nYou have ordered the following sandwiches:")
	for sandwich in sandwiches:
		print(sandwich)


ordered_sandwiches('apple')
ordered_sandwiches('apple', 'banana')
ordered_sandwiches('apple', 'banana', 'pair')


# 8-13. User Profile: Start with a copy of user_profle.py from page 153 Build
# a profle of yourself by calling build_profile(), using your frst and last names
# and three other key-value pairs that describe you

def build_profile(first, last, **user_info):
	'''Build a dictionary containing everything we know about a user.'''
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile

my_profile = build_profile(
			'jinhui',
			'zhou',
			location='china',
			field='programming'
			)

for key, value in my_profile.items():
	print(key.title() + ": " + value.title())

# 8-14. Cars: Write a function that stores information about a car in a dictionary 
# The function should always receive a manufacturer and a model name It
# should then accept an arbitrary number of keyword arguments 
# Call the function with the required information and two other name-value pairs, such as a
# color or an optional feature Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly

def make_car_info(manufacturer, model, **other_info):
	'''Build a dictionary containing the infomation of a car'''
	car_info = {}
	car_info['manufacturer'] = manufacturer
	car_info['model'] = model
	for key, value in other_info.items():
		car_info[key] = value
	return car_info

car = make_car_info('bmw', 'M2', color='white', tow_package=True)

print(car)


# Storing your functions in modules
#   Importing an entire module

def make_pizza(size, *toppings):                              # pizza.py
	'''Summarize the pizza we are about to make.'''
	print("\nMaking a " + str(size) +
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)


import pizza                                                    # making_pizzas.py

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Improting specific functions

from module_name import function_name

from module_name import function_0, function_1, function_2

# Using as to give a function an alias
from pizza import making_pizzas as making_pizzas

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# Using as to give a module an alias
import module_name as mn

# Importing all functions in a module
from module_name import *

# Styling functions
# If you specify a default value for a parameter, no spaces should be
# used on either side of the equal sign:
def function_name(parameter_0, parameter_1='default value')
# The same convention should be used for keyword arguments in function calls:
function_name(value_0, parameter_1='value')
# If a set of parameters causes a function's definition to be longer than 79:
def function_name(
		parameter_0, parameter_1, parameter_2,
		parameter_3, parameter_4, parameter_5):
	function body...

#----------------------TRY IT YOURSELF-----------------------------
# 8-15. Printing Models: Put the functions for the example print_models.py in a
# separate fle called printing_functions.py Write an import statement at the top
# of print_models.py, and modify the fle to use the imported functions


### Finished at Jan 04 2019