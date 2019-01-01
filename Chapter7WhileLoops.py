#   Jan 1 2019

#  Introducing while loops

prompt = "\nTell me something, and I will repeat it back to you: "    # This block of code is my fault practise.
prompt += "\nEnter 'quit' to end the program. "

message = input(prompt)

while message != 'quit':
	print(message)

# The example below is correct.

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ''

while message != 'quit':
	message = input(prompt)    # As loop reaches this statement, It waits for user's input.
	print(message)             # So, It's the key why this block of code is different from the above.


prompt = "\nTell me something, and I will repeat it back to you: "   # Example 2
prompt += "\nEnter 'quit' to end the program. "

message = ''

while message != 'quit':
	message = input(prompt)    # As loop reaches this statement, It waits for user's input.
	
	if message != 'quit':
		print(message)


#  Using a flag

prompt = "\nTell me something, and I will repeat it back to you: "     #  Example 3
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)


# Using break to exit a loop

prompt = "\nPlease enter the name of a city you have visited: "    # Example 4
prompt += "\n(Enter 'quit' when you finished.)"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")

current_num = 0                                              # Example 5

while current_num < 10:
	current_num += 1

	if current_num % 2 == 0:
		continue   #-----------> This statement tells Python to ignore the rest of loop and return
	                           # to the beginning.
	print(current_num)


# Avoiding infinite loops
# !! The value in conditional test statement should be changed in the following loops,
#    Otherwise, the loop will continue to run forever!!!

x = 1              # Example 6
while x <= 5:
	print(x)
	x += 1


# This loop runs forever!
x = 1
while x <= 5:
	print(x)


#  TRY IT YOURSELF

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value As they enter each topping,
# print a message saying you’ll add that topping to their pizza

prompt = "\nEnter a pizza topping: "
prompt += "\nEnter 'quit' when you finished."

while True:
	topping = input(prompt)
	if topping != 'quit':
		print("\nYou'll add " + topping.title() + " to your pizza.")
	else:
		break


# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15 Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket

''' age < 3  free
    3 <= age <= 12  $10
    age > 12 $15
'''

prompt = "\nEnter your age to know your ticket price: "
prompt += "\nEnter 'quit' to finish."

while True:
	age = input(prompt)
	if age == 'quit':
		break
	age = int(age)
	
	if age < 3:
		print("\nYour ticket price is free.")
	if 3 <= age <= 12:
		print("\nYour ticket price is $10.")
	if age > 12:
		print("\nYour ticket price is $15.")

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# •	 Use a conditional test in the while statement to stop the loop
# •	 Use an active variable to control how long the loop runs
# •	 Use a break statement to exit the loop when the user enters a 'quit' value


prompt = "\nEnter a pizza topping: "
prompt += "\nEnter 'quit' when you finished."

topping = ''

while topping != 'quit':
	topping = input(prompt)
	if topping != 'quit':
		print("\n" + topping.title() + " will be added to your pizza.")


#---------------------------------------------------------------------------------

prompt = "\nEnter a pizza topping: "
prompt += "\nEnter 'quit' when you finished."

active = True

while active:
	topping = input(prompt)
	if topping == 'quit':
		active = False
	else:
		print("\n" + topping.title() + " will be added to your pizza.")

#-------------------------------------------------------------------------------

prompt = "\nEnter a pizza topping: "
prompt += "\nEnter 'quit' when you finished."

while True:
	topping = input(prompt)
	if topping == 'quit':
		break
	if topping != 'quit':
		print("\n" + topping.title() + " will be added to your pizza.")



# Using a while loop with lists and dictionaries
# Moving items from one list to another
#------------------------------------------------------

# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brain', 'candace']               # Example 1
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

#---------------------------------------------------------

# Removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']      # Example 2
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)

#-------------------------------------------------------------
# Fill a dictionary with user input
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")

	# Store the response in the dictionary:
	responses[name] = response

	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/ no)")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name,response in responses.items():
	print(name + " would like to climb " + response + ".")

# -----------TRY IT YOURSELF-------------------------------------------------
# 7-8. Deli: Make a list called sandwich_orders and fll it with the names of various sandwiches 
# Then make an empty list called finished_sandwiches Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of fnished sandwiches After all the sandwiches have been made, print a
# message listing each sandwich that was made

sandwich_orders = ['apple', 'banana', 'orange', 'tomato']
finished_sandwiches = []


while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("I'm working on your " + current_sandwich + " sandwich.")
	finished_sandwiches.append(current_sandwich)

print("\n")

for sandwich in finished_sandwiches:
	print("I made a " + sandwich + " sandwich.")


# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders Make sure no pastrami sandwiches end up
# in finished_sandwiches

sandwich_orders = ['apple', 'pastrami', 'banana', 'orange', 'pastrami', 'tomato', 'pastrami']

print("***Out of Pastrami***")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
	print(sandwich)

# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll

vacation_poll = {}

prompt = "If you could visit one place in the world, "
prompt += "where would you go? "

polling_active = True
while polling_active:
	name = input("What is your name? ")
	place = input(prompt)
	vacation_poll[name] = place

	repeat = input(" Would you like to let another person poll? (yes/ no) ")
	if repeat == 'no':
		polling_active = False

print("\n----- Poll Results -----")
for name, place in vacation_poll.items():
	print(name + " would like to visit " + place + ".")


#=========================Chapter7 finished==========================