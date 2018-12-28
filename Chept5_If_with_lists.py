#   Dec 28 2018

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]    # Example 1

for requested_topping in requested_toppings:
	print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")


requested_toppings = ["mushrooms", "green peppers", "extra cheese"]    # Example 2

for requested_topping in requested_toppings:
	if requested_topping == "green peppers":
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")


requested_toppings = ["mushrooms", "green peppers", "extra cheese"]   # Example 3

if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")	
else:
	print("Are you sure you want a plain pizza?")

requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")	
else:
	print("Are you sure you want a plain pizza?")


available_toppings = ["mushrooms", "olives", "green peppers",      # Example 4
  					  "pepperoni", "pineapple", "extra cheese"]    # Note that the list could be a tuple,
requested_toppings = ["mushrooms", "french fries", "extra cheese"] # if the available toppings are stable.

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

#  TRY IT YOURSELF
# 5-8. Hello Admin: Make a list of fve or more usernames, including the name
# 'admin' Imagine you are writing code that will print a greeting to each user
# after they log in to a website Loop through the list, and print a greeting to
# each user:
# •	 If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# •	 Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

usernames = ["david", "lilei", "admin", "lichard", "jack"]      # 5-8
for username in usernames:
	if username == "admin":
		print("Hello " + username.title()
			  + ", would you like to see a status report?")
	else:
		print("Hello " + username.title()
			  + ", thank you for logging in again.")

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty
# •	 If the list is empty, print the message We need to fnd some users!
# •	 Remove all of the usernames from your list, and make sure the correct
# message is printed

usernames = []                                  # 5-9
if usernames:
	for username in usernames:
		if username == "admin":
			print("Hello " + username.title()
 			       + ", would you like to see a status report?")
		else:
			print("Hello " + username.title()
 			       + ", thank you for logging in again.")
else:
	print("We need to find some users!")

# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username
# •	 Make a list of fve or more usernames called current_users
# •	 Make another list of fve usernames called new_users Make sure one or
# two of the new usernames are also in the current_users list
# •	 Loop through the new_users list to see if each new username has already
# been used If it has, print a message that the person will need to enter a
# new username If a username has not been used, print a message saying
# that the username is available
# •	 Make sure your comparison is case insensitive If 'John' has been used,
# 'JOHN' should not be accepted

current_users = ["david", "lilei", "admin", "lichard", "jack", "vincent"]  # 5-10

new_users = ["xiaohong", "daming", "Lilei", "lichard", "trump"]

for new_user in new_users:
	if new_user.lower() in current_users:              # case sensitive.
		print("The username has already existed, please enter a new username.")
	else:
		print("The username is available!")


# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd Most ordinal numbers end in th, except 1, 2, and 3
# •	 Store the numbers 1 through 9 in a list
# •	 Loop through the list
# •	 Use an if-elif-else chain inside the loop to print the proper ordinal 
#      ending for each number Your output should read "1st 2nd 3rd 4th 5th 6th
#      7th 8th 9th", and each result should be on a separate line

ordinal_numbers = list(range(1, 10))      # 5-11
for n in ordinal_numbers:
	if n == 1:
		print(str(n) + "st")
	elif n == 2:
		print(str(n) + "nd")
	elif n == 3:
		print(str(n) + "rd")
	else:
		print(str(n) + "th")


