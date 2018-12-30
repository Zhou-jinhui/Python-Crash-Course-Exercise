# Dec 30 2018
# A dictionary in dictionary

users = {                                   # Example 1
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},

	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris'
		},

}

for username, userinfo in users.items():
	print("\nUsername: " + username)
	full_name = userinfo['first'].title() + " " + userinfo['last'].title()
	location = userinfo['location'].title()

	print("\tFull name: " + full_name)
	print("\tLocation: " + location)


                    # TRY IT YOURSELF

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102)
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people Loop through your list of people As you
# loop through the list, print everything you know about each person

people = []

person = {
		"first_name": "lichard",
		"last_name": "liu",
		"age": 52,
		"city": "beijing",
		}

people.append(person)

person = {
	"first_name": "jack",
	"last_name": "ma",
	"age": 58,
	"city": "hangzhou",
	}

people.append(person)

person = {
	"first_name": "huateng",
	"last_name": "ma",
	"age": 55,
	"city": "shenzhen",
	}

people.append(person)

for person in people:
	fullname = person["first_name"].title() + person["last_name"].title()
	age = str(person["age"])
	city = person["city"].title()
	print("\n" + fullname + " is from " + city + " and is " +
		age + " years old.")

# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet In each dictionary, include the kind of animal and the owner’s
# name Store these dictionaries in a list called pets Next, loop through your list
# and as you do print everything you know about each pet

pets = []

pet = {
	"name": "xiaohong",
	"kind": "cat",
	"owner": "yongyuan",
	"age": 2,
	}
pets.append(pet)

pet = {
	"name": "xiaobai",
	"kind": "dog",
	"owner": "xijin",
	"age": 3,
	}
pets.append(pet)

pet = {
	"name": "xiaohuang",
	"kind": "bear",
	"owner": "jinping",
	"age": 66,
	}
pets.append(pet)

i = 0
for pet in pets:
	name = pets[i]["name"]
	kind = pets[i]["kind"]
	owner = pets[i]["owner"]
	age = str(pets[i]["age"])
	i += 1
	print("\n" + name.title() + " is a " + kind + " ownned by " +
		owner.title() + " and is " + age + " years old.")

### What in above is my solution, but it's not good when the count of items in
### dictionary is large. so I referance the solution by author and imitate it below.

pets = []

pet = {
	"name": "xiaohong",
	"kind": "cat",
	"owner": "yongyuan",
	"age": 2,
	}
pets.append(pet)

pet = {
	"name": "xiaobai",
	"kind": "dog",
	"owner": "xijin",
	"age": 3,
	}
pets.append(pet)

pet = {
	"name": "xiaohuang",
	"kind": "bear",
	"owner": "jinping",
	"age": 66,
	}
pets.append(pet)

for pet in pets:
	print("\nHere is what I know about " + pet["name"].title() + ":")
	for key, value in pet.items():
		print("\t" + key + " : " + str(value).title())


# 6-9. Favorite Places: Make a dictionary called favorite_places Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places Loop through the dictionary, and print
# each person’s name and their favorite places

favorite_places = {
	"lichard": ["minisuda", "england", "nanjing"],
	"jack": ["hangzhou", "yiwu", "losangi"],
	"xijin": ["xinjiang", "thailand"],
}

for key, value in favorite_places.items():
	print("\n" + key.title() + "'s favorite places are:")
	for place in value:
		print("\t" + place.title())

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number Then print each person’s
# name along with their favorite numbers

favorite_numbers = {
					"lichard": [52, 45, 545],
					"lilei": [65, 34, 53],
					"hanmeimei": [23, 76, 45],
					"xiaozhang": [2, 45, 55],
					"xiaohong": [5, 45, 547],
					}

for name, numbers in favorite_numbers.items():
	print("\n" + name.title() + " likes the following numbers:")
	for number in numbers:
		print("\t" + str(number))


# 6-11. Cities: Make a dictionary called cities Use the names of three cities as
# keys in your dictionary Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city The keys for each city’s dictionary should be something like
# country, population, and fact Print the name of each city and all of the information you have stored about it

cities = {
	"shanghai": {
	"country": "china",
	"population": "1000 million",
	"fact": "one of biggest cities in china."
	},

	"tokyo":{
	"country": "japan",
	"population": "900 million",
	"fact": "one of biggest cities in Japan."
	},

	"taipei":{
	"country": "taiwan",
	"population": "800 million",
	"fact": "one of biggest cities in Tanwan."
	},
}

for city, info in cities.items():
	country = info["country"].title()
	population = info["population"]	
	fact = info["fact"]
	print("\n" + city.title() + " is in " + country + ".")
	print("\tIt has a population of about " + population + ".")
	print("\tIt is " + fact)

# Chepter 6 finished.