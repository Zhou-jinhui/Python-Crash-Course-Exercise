 # Dec 28 2018

alien_0 = {"color": "green", "points": 5}  # Example 1

print(alien_0["color"])
print(alien_0["points"])

# A key’s value can be a number, a string, a list, or even another dictionary.
# In fact, you can use any object that you can create in Python as a value in a
# dictionary.

alien_0 = {"color": "green", "points": 5}   # Example 2

new_points = alien_0["points"]
print("You just earned " + str(new_points) + " points!")


# Adding new key-value pairs

alien_0 = {"color": "green", "points": 5}    # Example 3
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

#  Notice that the order of the key-value pairs does not match the
# order in which we added them. Python doesn’t care about the order in
# which you store each key-value pair; it cares only about the connection
# between each key and its value.

# Starting with an empty dictionary

alien_0 = {}                                 # Example 4
alien_0["color"] = "green"
alien_0["points"] = 5

print(alien_0)

# Modifying values in dictionary

alien_0 = {"color": "green"}
print("The alien is " + alien_0["color"] + ".")

alien_0["color"] = "yellow"
print("The alien is now " + alien_0["color"] + ".")

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}  # Example 5
alien_0["speed"] = "fast"
print("Original x_position: " + str(alien_0["x_position"]))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0["speed"] == "slow":
	x_increment = 1
elif alien_0["speed"] == "medium":
	x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3

# The new position is the old position plus the increment.
alien_0["x_position"] = alien_0["x_position"] + x_increment

print("New x-position: " + str(alien_0["x_position"]))

alien_0 = {"color": "green", "points": 5}                 # Example 6
print(alien_0)

del alien_0["points"]
print(alien_0)


# A dictionary of similar objects

favorite_languages = {                           # Example 7
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

print("Sarah's favorite language is " + 
	favorite_languages["sarah"].title() +
	".")

#  	TRY IT YOURSELF
# 6-1. Person: Use a dictionary to store information about a person you know
# Store their frst name, last name, age, and the city in which they live You
# should have keys such as first_name, last_name, age, and city Print each
# piece of information stored in your dictionary

xiao_liu = {
			"first_name": "lichard",
			"last_name": "liu",
			"age": 52,
			"city": "beijing",
			}
#for i in xiao_liu:              # This statement prints key only!
	#print(i)

print(xiao_liu["first_name"].title())
print(xiao_liu["last_name"].title())
print(xiao_liu["age"])
print(xiao_liu["city"].title())

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers
# Think of fve names, and use them as keys in your dictionary Think of a favorite
# number for each person, and store each as a value in your dictionary Print
# each person’s name and their favorite number For even more fun, poll a few
# friends and get some actual data for your program

favorite_numbers = {
					"lichard": 52,
					"lilei": 38,
					"hanmeimei": 69,
					"xiaozhang": 12,
					"xiaohong": 25,
					}

print("Lichard's favorite number is " +
	  str(favorite_numbers["lichard"]) + ".")
print("Lilei's favorite number is " +
	  str(favorite_numbers["lilei"]) + ".")
print("Hanmeimei's favorite number is " +
	  str(favorite_numbers["hanmeimei"]) + ".")
print("Xiaozhang's favorite number is " +
	  str(favorite_numbers["xiaozhang"]) + ".")
print("Xiaohong's favorite number is " +
	  str(favorite_numbers["xiaohong"]) + ".")

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary
# However, to avoid confusion, let’s call it a glossary
# •	 Think of fve programming words you’ve learned about in the previous
# chapters Use these words as the keys in your glossary, and store their
# meanings as values
# •	 Print each word and its meaning as neatly formatted output You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output

glossary = {
			"string": "A series of characters.",
			"comment": "A note in a program that the Python interpreter ignores.",
			"list": "A collection of items in a particular order.",
			"loop": "Work through a collection of items, one at a time.",
			"dictionary": "A collection of key-value pairs.",
  			}

print("string:\n\t" + glossary["string"])
print("comment:\n\t" + glossary["comment"])
print("list:\n\t" + glossary["list"])
print("loop:\n\t" + glossary["loop"])
print("dictionary:\n\t" + glossary["dictionary"])


# Looping through a dictionary

user_0 = {                             # Example 8
	"username": "efermi",
	"first": "enrico",
	"last": "fermi",
	}

for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)


favorite_languages = {                     # Example 9
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

for name, language in favorite_languages.items():
	print(name.title() +
		"'s favorite language is " +
		language.title() + ".")

favorite_languages = {                     # Example 10
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

for name in favorite_languages.keys():
	print(name.title())

favorite_languages = {                     # Example 11
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() +
			", I see your favorite language is " +
			favorite_languages[name].title() + "!")  
			# !! name is a variable that refer to a string.
			# hence, what in the square brackets is "phil"\"sarah" etc.

   # to page 105