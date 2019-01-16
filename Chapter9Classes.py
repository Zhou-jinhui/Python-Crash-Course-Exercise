#-------------------Chapter 9 Classes--------------------------
# Creating and using a class
# Creating the dog class
class Dog():
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")

# Making an instance from a class


my_dog = Dog('willie',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# Accessing attributes
# To access the attributes of an instance, you use dot notation. At v we access
# the value of my_dog’s attribute name by writing:

my_dog.name

# Calling methods
my_dog = Dog('willie',6)
my_dog.sit()
my_dog.roll_over()

# Creating multiple instances
class Dog():
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


#--------------------TRY IT YOURSELF-----------------------------
# 9-1. Restaurant: Make a class called Restaurant The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
#  that the restaurant is open
# Make an instance called restaurant from your class Print the two attributes individually,
#  and then call both methods
class Restaurant():
	"""Introduce restaurants"""

	def __init__(self, name, cuisine_type):
		self.name = name.title()
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(self.name + " is a " + self.cuisine_type + " restaurant.")

	def open_restaurant(self):
		print(self.name + " is open.")

restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1 Create three
# different instances from the class, and call describe_restaurant() for each
# instance
class Restaurant():
	"""Introduce restaurants"""

	def __init__(self, name, cuisine_type):
		self.name = name.title()
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(self.name + " is a " + self.cuisine_type + " restaurant.")

	def open_restaurant(self):
		print(self.name + " is open.")

restaurant_0 = Restaurant('kfc', 'fast food')
restaurant_1 = Restaurant('mc', 'fast food')
restaurant_2 = Restaurant('chuanfu', 'hot-pot')

restaurant_0.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()

# 9-3. Users: Make a class called User Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profle Make a method called describe_user() that prints a summary
# of the user’s information Make another method called greet_user() that prints
# a personalized greeting to the user
# Create several instances representing different users, and call both methods
# for each user
class User():
	# A class containing user infomation.

	def __init__(self, first_name, last_name, username, email, location):
		self.f_name = first_name.title()
		self.l_name = last_name.title()
		self.u_name = username.title()
		self.email = email
		self.location = location

	def describe_user(self):
		print("\n" + self.f_name + " " + self.l_name)
		print("  Username: " + self.u_name)
		print("  Location: " + self.location)
		print("  Email: " + self.email)

	def greet_user(self):
		msg = "Hi " + self.u_name + ", welcome."
		print(msg)

user_0 = User('lichard', 'liu', 'qiangdong', '111@jd.com', 'beijing')
user_0.describe_user()
user_0.greet_user()

user_1 = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
user_1.describe_user()
user_1.greet_user()

user_2 = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
user_2.describe_user()
user_2.greet_user()


# Working with classes and instances
# The car class
class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Setting a default value for an attribute
class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying attribute values
# Modifying an attribute's value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an attribute's value through method
class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# Incrementing an attribute's value through a method
class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#------------TRY IT YOURSELF----------------------------------
# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166)
# Add an attribute called number_served with a default value of 0 Create an
# instance called restaurant from this class Print the number of customers the
# restaurant has served, and then change this value and print it again
# Add a method called set_number_served() that lets you set the number
# of customers that have been served Call this method with a new number and
# print the value again
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served Call this method with any number you like 
# that could represent how many customers were served in, say, a
# day of business
class Restaurant():
    """ A simple attempt to model a restaurant."""
    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a descriptive message."""
        print(self.name.title() + " is a " + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        """Print a message that indicating that the restaurant is open."""
        print(self.name.title + " is open.")


restaurant = Restaurant('chuanfu', 'hot-pot')
print(restaurant.number_served)
restaurant.number_served = 12
print(restaurant.number_served)


class Restaurant():
    """ A simple attempt to model a restaurant."""
    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a descriptive message."""
        print(self.name.title() + " is a " + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        """Print a message that indicating that the restaurant is open."""
        print(self.name.title + " is open.")


    def set_number_served(self, number):
    	"""set the number of customers that have been served."""
    	self.number_served = number

    def increment_number_served(self,increment_number):
    	"""Increment the number of served customers."""
    	self.number_served += increment_number

restaurant = Restaurant('chuanfu', 'hot-pot')
restaurant.set_number_served(16)
print(restaurant.number_served)
restaurant.increment_number_served(3)
print(restaurant.number_served)

# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166) Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1 Write
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0
# Make an instance of the User class and call increment_login_attempts()
# several times Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts() Print login_attempts again to
# make sure it was reset to 0
class User():
    """A simple attempt to model a user information."""
    def __init__(self, first_name, last_name, location, username, age, login_attempts):
        """Initialize profile attributes."""
        self.f_name = first_name
        self.l_name = last_name
        self.location = location
        self.username = username
        self.age = age
        self.login_attempts = login_attempts


    def describe_user(self):
        """Print the profile of the user."""
        print(self.username.title() + "'s fullname is " + self.f_name.title() + " " + self.l_name.title() +
            ", " + str(self.age) + " years old living in " + self.location.title() + ".")

    def greet_user(self):
        """Print a personalized greeting message."""
        print("Hi " + self.username.title() + ", welcome back.")

    def increment_login_attempts(self):
    	"""Increment the login attempts."""
    	self.login_attempts += 1

    def reset_login_attempts(self):
    	"""Reset the value of login_attempts to 0."""
    	self.login_attempts = 0

alice = User('lichard', 'liu', 'beijing', 'alice', 49, 4)
alice.increment_login_attempts()
print(alice.login_attempts)
alice.increment_login_attempts()
print(alice.login_attempts)
alice.increment_login_attempts()
print(alice.login_attempts)
alice.reset_login_attempts()
print(alice.login_attempts)


#  Inheritance
# The __init__() method for a child class
class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

class ElectricCar(Car):          # 2
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):    # 3
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year)   # 4

my_tesla = ElectricCar('tesla', 'model s', 2016)  # 5
print(my_tesla.get_descriptive_name())
# In this point, we're just making sure that the subclass has the attributes that 
# superclass included.

# Defining attributes and methods for the child class
class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery_size = 70

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# Overriding methods from the parent class
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery_size = 70

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def fill_gas_tank():
		"""Electric cars don't have gas tanks."""
		print("This doesn't need a gas tank!")


# Instances as attributes
class Battery():
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()     # We have to call it through the car's battery attribute.


class Battery():
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size ==70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " mile on a full charge."
		print(message)


# Modeling Real-world Objects

#------------TRY IT YOURSELF-------------------------------
# 9-6. Ice Cream Stand: An ice cream stand is a specifc kind of restaurant Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) Either version of
# the class will work; just pick the one you like better Add an attribute called
# flavors that stores a list of ice cream ﬂavors Write a method that displays
# these ﬂavors Create an instance of IceCreamStand, and call this method
class Restaurant():
	"""Introduce restaurants"""

	def __init__(self, name, cuisine_type):
		self.name = name.title()
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(self.name + " is a " + self.cuisine_type + " restaurant.")

	def open_restaurant(self):
		print(self.name + " is open.")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)

        self.flavors = ['apple', 'chocolate', 'banana']

    def display_flavors(self):
        message = "Here is the flavors of ice cream:"
        print(message)
        for flavor in self.flavors:
            print("\t" + flavor)

stand1 = IceCreamStand('shizu', 'ice cream')
stand1.display_flavors()

# 9-7. Admin: An administrator is a special kind of user Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171) Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on
# Write a method called show_privileges() that lists the administrator’s set of
# privileges Create an instance of Admin, and call your method
class User():
    """A simple attempt to model a user information."""
    def __init__(self, first_name, last_name, location, username, age):
        """Initialize profile attributes."""
        self.f_name = first_name
        self.l_name = last_name
        self.location = location
        self.username = username
        self.age = age
        self.login_attempts = 0


    def describe_user(self):
        """Print the profile of the user."""
        print(self.username.title() + "'s fullname is " + self.f_name.title() + " " + self.l_name.title() +
            ", " + str(self.age) + " years old living in " + self.location.title() + ".")

    def greet_user(self):
        """Print a personalized greeting message."""
        print("Hi " + self.username.title() + ", welcome back.")

    def increment_login_attempts(self):
        """Increment the login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0

class Admin(User):
    """Creat a child class inherits from User."""

    def __init__(self, first_name, last_name, location, username, age):
        super().__init__(first_name, last_name, location, username, age)

        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        message = "Here are the administrator's privileges:"
        print(message)
        for privilege in self.privileges:
            print("\t" + privilege)

admin1 = Admin('lichard', 'liu', 'beijing', 'dongdong', '52')
admin1.show_privileges()

# 9-8. Privileges: Write a separate Privileges class The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7
# Move the show_privileges() method to this class Make a Privileges instance
# as an attribute in the Admin class Create a new instance of Admin and use your
# method to show its privileges
class User():
    """A simple attempt to model a user information."""
    def __init__(self, first_name, last_name, location, username, age):
        """Initialize profile attributes."""
        self.f_name = first_name
        self.l_name = last_name
        self.location = location
        self.username = username
        self.age = age
        self.login_attempts = 0


    def describe_user(self):
        """Print the profile of the user."""
        print(self.username.title() + "'s fullname is " + self.f_name.title() + " " + self.l_name.title() +
            ", " + str(self.age) + " years old living in " + self.location.title() + ".")

    def greet_user(self):
        """Print a personalized greeting message."""
        print("Hi " + self.username.title() + ", welcome back.")

    def increment_login_attempts(self):
        """Increment the login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0


class Privileges():
    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges

    def show_privileges(self):
        message = "Here are the administrator's privileges:"
        print(message)
        for privilege in self.privileges:
            print("\t" + privilege)


class Admin(User):
    """Creat a child class inherits from User."""

    def __init__(self, first_name, last_name, location, username, age):
        super().__init__(first_name, last_name, location, username, age)

        self.privileges = Privileges()

admin2 = Admin('jack', 'ma', 'hangzhou', 'laoma', 59)
admin2.privileges.show_privileges()

# 9-9. Battery Upgrade: Use the fnal version of electric_car.py from this section
# Add a method to the Battery class called upgrade_battery() This method
# should check the battery size and set the capacity to 85 if it isn’t already
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery You should
# see an increase in the car’s range
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size ==70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " mile on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 85:
            print("The battery needn't to upgrade.")
        elif self.battery_size < 85:
            self.battery_size = 85
            print("The battery has been upgraded.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print("\n")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print("\n")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# Importing classes
# Importing a single class
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Storing multiple classes in a module
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# Importing multiple classes from a module
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


# Importing all classes from a module
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


# Importing all classes from a module
from module_name import * # Not recommended


# Importing a module into a module


# Finding your own workflow

#------------TRY IT YOURSELF----------------------------------
# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module Make
#  a separate fle that imports Restaurant Make a Restaurant instance,
# and call one of Restaurant’s methods to show that the import statement is working properly
from restaurant import Restaurant

chuanfu = Restaurant('chuanfu', 'hot-pot')
chuanfu.describe_restaurant()

# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178)
# Store the classes User, Privileges, and Admin in one module Create a separate fle,
#  make an Admin instance, and call show_privileges() to show that
# everything is working correctly
from usermodule import User, Privileges, Admin

admin1 = Admin('lichard', 'liu', 'beijing', 'dongdong', 54)
admin1.privileges.show_privileges()

# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module In a separate fle, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly
from usermodule import User
from usermodule2 import Privileges, Admin

admin1 = Admin('lichard', 'liu', 'beijing', 'dongdong', 54)
admin1.privileges.show_privileges()


# The python standard library
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
		language.title() + ".") 


#------TRY IT YOURSELF----------------------------------------------------
# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
# used a standard dictionary to represent a glossary Rewrite the program using
# the OrderedDict class and make sure the order of the output matches the order
# in which key-value pairs were added to the dictionary
from collections import OrderedDict

glossary = OrderedDict()
glossary["string"] = "A series of characters."
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

# for key, value in glossary.items():
# 	print("\n" + key.title() + ": " + value)

# 9-14. Dice: The module random contains functions that generate random numbers in 
# a variety of ways The function randint() returns an integer in the
# range you provide The following code returns a number between 1 and 6:
# from random import randint
# x = randint(1, 6)
# Make a class Die with one attribute called sides, which has a default
# value of 6 Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has Make a 6-sided die and roll
# it 10 times
# Make a 10-sided die and a 20-sided die Roll each die 10 times
from random import randint

class Die():

	def __init__(self, sides=6):
		
		self.sides = sides


	def roll_die(self):
		x = randint(1, self.sides)
		
		return x

six_sided_die = Die()
results = []
for roll_num in range(10):
	result = six_sided_die.roll_die()
	results.append(result)
print("10 rolls of a 6-sided die: ")
print(results)

print("--------- Ten sided die below ------------------------")

ten_sided_die = Die(10)
results = []
for roll_num in range(10):
	result = ten_sided_die.roll_die()
	results.append(result)
print("10 rolls of a 10-sided die: ")
print(results)

print("--------- Twenty sided die below ------------------------")

twenty_sided_die = Die(20)
results = []
for roll_num in range(10):
	result = twenty_sided_die.roll_die()
	results.append(result)
print("10 rolls of a 20-sided die: ")
print(results)

# 9-15. Python Module of the Week: One excellent resource for exploring the
# Python standard library is a site called Python Module of the Week Go to
# http://pymotw.com/ and look at the table of contents Find a module that
# looks interesting to you and read about it, or explore the documentation of
# the collections and random modules

# Styling classes
# CamelCaps

# Summary  Finished on Jan 16 2019