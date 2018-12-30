#  Dec 29 2018

favorite_languages = {                            # Example 1
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


favorite_languages = {                             # example 2
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll!")

favorite_languages = {                             # example 3
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been metioned:")
for language in sorted(favorite_languages.values()):
    print(language.title())


favorite_languages = {                             # example 4
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been metioned:")
for language in set(sorted(favorite_languages.values())):
    print(language.title())


#  TRY IT YOURSELF

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values
# When you’re sure that your loop works, add fve more Python terms to your
# glossary When you run your program again, these new words and meanings
# should automatically be included in the output

glossary = {
			"string": "A series of characters.",
			"comment": "A note in a program that the Python interpreter ignores.",
			"list": "A collection of items in a particular order.",
			"loop": "Work through a collection of items, one at a time.",
			"dictionary": "A collection of key-value pairs.",
            "key": "The first item in a key-value pair in a dictionary.",
            "value": "An item associated with a key in a dictionary.",
            "conditional test": "A comparison between two values.",
            "float": "A numerical value with a decimal component.",
            "boolean expression": "An expression that evaluates to True or False.",
  			}

for key, value in glossary.items():
    print("\n" + key.title() + ": " + value)

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through One key-value pair might be 'nile': 'egypt'
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt
# •	 Use a loop to print the name of each river included in the dictionary
# •	 Use a loop to print the name of each country included in the dictionary

rivers = {
    "nile": "egypt",
    "thames": "england",
    "changjiang": "china",
    }

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

# 6-6. Polling: Use the code in favorite_languages.py (page 104)
# •	 Make a list of people who should take the favorite languages poll Include
# some names that are already in the dictionary and some that are not
# •	 Loop through the list of people who should take the poll If they have
# already taken the poll, print a message thanking them for responding
# If they have not yet taken the poll, print a message inviting them to take
# the poll

favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

voters_list = ["lichard", "jen", "xiaoming", "edward", "john"]

for voter in voters_list:
    if voter in favorite_languages.keys():
        print(voter.title() + ", thank you for taking our poll!")
    else:
        print(voter.title() + ", please take our poll!")



#  Nesting

alien_0 = {"color": "green", "points": 5}            # Example 5
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# The output will be like this:
# {'color': 'green', 'points': '5'}
# {'color': 'yellow', 'points': '10'}
# {'color': 'red', 'points': '15'}
# !! Remember that the items in a list always be values, not variables.


# Make an empty list for storing aliens.                  Example 6
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))


# Make an empty list for storing aliens.                  Example 7
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Make an empty list for storing aliens.                  Example 8
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['point'] = 15
        alien['speed'] = 'fast'

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")


# A list in a dictionary

# Store information about a pizza being ordered.
pizza = {                                           # Example 9
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
    }

# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following topping:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {                            # Example 10
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) >= 2:
        print("\n" + name.title() + "'s favorite language are:")
        for language in languages:
            print("\t" + language.title())
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is:" +
        "\n\t" + languages[0].title())

    
# A dictionary in dictionary                            # Example 11
users = {
    'aeinstein': {
        
    }
}
