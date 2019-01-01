# Chepter 7 INPUT

# How the input() function works

message = input("Tell me something, and I will repeat it back to you: ")    # Example 1
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is you first name? "
name = input(prompt)
print("Hello, " + name + "!")

# Using int() to accept numerical input

height = input("How tall are you, in inches? ")          # Example 2
height = int(height)

if height >= 36:
	print("\nYou are tall enough to ride!")

else:
	print("\nYou'll be able to ride when you're a little older.")


number = input("Enter a number, ande I'll tell you if it's even or odd: ")   # Example 3
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")


#  TRY IT YOURSELF

# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like Print a message about that car, such as “Let me see if I can fnd you
# a Subaru ”

car = input("What kind of rental car would you like? ")
print("\nLet me see if I can find you a " + car.title() + ".")

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group If the answer is more than eight, print a message 
# saying they’ll have to wait for a table Otherwise, report that their table is ready

group_num = input("How many people are in your dinner group? ")
group_num = int(group_num)

if group_num >= 8:
	print("\nSorry, you'll have to wait for a table.")
elif 0 < group_num < 8:
	print("\nYour table is ready.")
else:
	print("\nPlease enter a valid number.")


# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not

number = input("Enter a number, and I'll tell you whether it's multiple of ten or not. ")
number = int(number)

if number % 10 == 0:
	print("\n" + str(number) + " is multiple of ten.")
else:
	print("\n" + str(number) + " is not multiple of ten.")


# Introducing while loops

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
	message = input(prompt)
	print(message)

