# Chepter 4  Working with part of a list
# Slice
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])             # !!! It's a colon in the square bracket, not commas.

print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# Looping through a slice
players = ["charles", "martina", "michael", "florence", "eli"]

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

# Copying a list
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print(my_foods)
print(friend_foods)

# TRY IT YOURSELF

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# •	 Print the message, The frst three items in the list are: Then use a slice to
# print the frst three items from that program’s list
# •	 Print the message, Three items from the middle of the list are: Use a slice
# to print three items from the middle of the list
# •	 Print the message, The last three items in the list are: Use a slice to print
# the last three items in the list

players = ["charles", "martina", "michael", "florence", "eli"]
print("The first three items in the list are:")
print(players[:3])
print("Three items from the middle of the list are:")
print(players[1:4])
print("The last three items in the list are:")
print(players[-3:])

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60) Make a copy of the list of pizzas, and call it friend_pizzas
# Then, do the following:
# •	 Add a new pizza to the original list
# •	 Add a different pizza to the list friend_pizzas
# •	 Prove that you have two separate lists Print the message, My favorite
# pizzas are:, and then use a for loop to print the frst list Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second list Make sure each new pizza is stored in the appropriate list

my_pizzas = ["apple", "banana", "tomato"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("cheese")
friend_pizzas.append("ice cream")

print("My favorite pizzas are:")
for i in my_pizzas:
	print(i+" pizza.")

print("My friend's favarite pizzas are:")
for i in friend_pizzas:
	print(i+" pizza.")