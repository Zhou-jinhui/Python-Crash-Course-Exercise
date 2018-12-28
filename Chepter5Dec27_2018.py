cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else :
		print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")



#  if statements
#  and or conditions
#  keyword: in  not

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")

# Boolean Expressions

#  TRY IT YOURSELF
# 5-1. Conditional Tests: Write a series of conditional tests Print a statement
# describing each test and your prediction for the results of each test Your 
# code should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# •	 Look closely at your results, and make sure you understand why each line
# evaluates to True or False
# •	 Create at least 10 tests Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False
# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to 10 If you want to try more comparisons, write more tests and add
# them to conditional_tests.py Have at least one True and one False result for
# each of the following:
# •	 Tests for equality and inequality with strings
# •	 Tests using the lower() function
# •	 Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
# •	 Tests using the and keyword and the or keyword
# •	 Test whether an item is in a list
# •	 Test whether an item is not in a list

car = "bmw"
print("Is car == 'bmw'? I predict True.")
print(car == "bmw")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

age = 28
print("Is age < 30 ? I predict True.")
print(age < 30)

print("\nIs age < 25 ? I predict False.")
print(age < 25)

age = 19
if age >= 18:
	print("You are old enough to vote.")
	print("Have you registered to vote yet?")


age = 17
if age >= 18:
	print("You are old enough to vote.")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

age = 12

if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10

print("Your admission cost is $" + str(price) + ".")

age = 45
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5

print("Your admission cost is $" + str(price) + ".")

requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
	print("Adding mushroom.")
if "pepperoni" in requested_toppings:
	print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")

#  	TRY IT YOURSELF
# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'
# •	 Write an if statement to test whether the alien’s color is green If it is, print
# a message that the player just earned 5 points
# •	 Write one version of this program that passes the if test and another that
# fails (The version that fails will have no output )
# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
# write an if-else chain
# •	 If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien
# •	 If the alien’s color isn’t green, print a statement that the player just earned
# 10 points
# •	 Write one version of this program that runs the if block and another that
# runs the else block

alien_color = "green"
if alien_color == "green":
	print("You've earned 5 points.")

alien_color = "yellow"
if alien_color == "green":
	print("You've earned 5 points.")    # 5-3

alien_color = "green"
if alien_color == "green":
	print("You've earned 5 points.")
else:
	print("You've earned 10 points.")

alien_color = "yellow"
if alien_color == "green":
	print("You've earned 5 points.")
else:
	print("You've earned 10 points.")   # 5-4

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an 
#      if-elifelse chain
# •	 If the alien is green, print a message that the player earned 5 points
# •	 If the alien is yellow, print a message that the player earned 10 points
# •	 If the alien is red, print a message that the player earned 15 points
# •	 Write three versions of this program, making sure each message is printed
# for the appropriate color alien

alien_color = "green"
if alien_color == "green":
	print("You've earned 5 points.")
elif alien_color == "yellow":
	print("You've earned 10 points.")
else :
	print("You've earned 15 points.")

alien_color = "yellow"
if alien_color == "green":
	print("You've earned 5 points.")
elif alien_color == "yellow":
	print("You've earned 10 points.")
else :
	print("You've earned 15 points.")

alien_color = "red"
if alien_color == "green":
	print("You've earned 5 points.")
elif alien_color == "yellow":
	print("You've earned 10 points.")
else :
	print("You've earned 15 points.")  # 5-5

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life Set a value for the variable age, and then:
# •	 If the person is less than 2 years old, print a message that the person is
# a baby
# •	 If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler
# •	 If the person is at least 4 years old but less than 13, print a message that
# the person is a kid
# •	 If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager
# •	 If the person is at least 20 years old but less than 65, print a message that
# the person is an adult
# •	 If the person is age 65 or older, print a message that the person is an
# elder

age = int(input("Enter your age:"))

if age < 2:
	stage_of_life = "a baby."
elif age >= 2 and age < 4:
	stage_of_life = "a toddler."
elif age >= 4 and age < 13:
	stage_of_life = "a kid."
elif age >= 13 and age < 20:
	stage_of_life = "a teenage."
elif age >= 20 and age < 65:
	stage_of_life = "an adult."
else:
	stage_of_life = "an elder."

print("You are " + stage_of_life)   # 5-6

# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list
# •	 Make a list of your three favorite fruits and call it favorite_fruits
# •	 Write fve if statements Each should check whether a certain kind of fruit
# is in your list If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!


favorite_fruits = ["apple", "longan", "banana"]
if "apple" in favorite_fruits:
	print("I really like apples!")
if "pear" in favorite_fruits:
	print("I really like pears!")
if "orange" in favorite_fruits:
	print("I really like oranges!")
if "longan" in favorite_fruits:
	print("I really like longans!")
if "banana" in favorite_fruits:
	print("I really like bananas!")   # 5-7