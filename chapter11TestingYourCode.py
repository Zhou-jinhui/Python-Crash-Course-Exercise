#-------Begin on Jan 18 2019-------------------------

# Testing a function
def get_formatted_name(first, last):
	"""Generate a neatly formatted full name."""
	full_name = first + ' ' + last
	return full_name.title()


from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		break
	last = input("Please give me a last name: ")
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)
	print("\tNeatly formatted name: " + formatted_name + ".")


# Unit tests and Test cases

# A passing test
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""

	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()


# A failing test

# Responding to a failed test
# solution: fix the function that we modified instead of fixing the test case.


# Adding new tests
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""

	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
		formatted_name = get_formatted_name(
			'wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()


# ----------------TRY IT YOURSELF------------------------------------------
# 11-1. City, Country: Write a function that accepts two parameters: a city name
# and a country name The function should return a single string of the form
# City, Country, such as Santiago, Chile Store the function in a module called
# city_functions.py
# Create a fle called test_cities.py that tests the function you just wrote
# (remember that you need to import unittest and the function you want to test)
# Write a method called test_city_country() to verify that calling your function
# with values such as 'santiago' and 'chile' results in the correct string Run
# test_cities.py, and make sure test_city_country() passes
def city_country(city, country):
	"""Return a formatted print like: "City, Country"."""
	formatted_name = city + ", " + country
	return formatted_name.title()

import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
	"""Test the function city_country."""
	def test_city_country(self):
		"""Do form like:Santiago, Chile?"""
		formatted_name = city_country('santiago', 'chile')
		self.assertEqual(formatted_name, 'Santiago, Chile')

unittest.main()


# 11-2. Population: Modify your function so it requires a third parameter,
# population It should now return a single string of the form City, Country –
# population xxx, such as Santiago, Chile – population 5000000 Run
# test_cities.py again Make sure test_city_country() fails this time
# Modify the function so the population parameter is optional Run
# test_cities.py again, and make sure test_city_country() passes again
# Write a second test called test_city_country_population() that verifes you 
# can call your function with the values 'santiago', 'chile', and
# 'population=5000000' Run test_cities.py again, and make sure this new test
# passes
def city_country(city, country, population):
	"""Return a formatted print like: "City, Country - population 5000000."."""
	formatted_name = city + ", " + country + " - population " + str(population)
	return formatted_name.title()


def city_country(city, country, population=0):
	"""Return a formatted print like: "City, Country - population 5000000."."""
	if population:
		formatted_name = city + ", " + country + " - population " + str(population)
	else:
		formatted_name = city + ", " + country
	return formatted_name.title()


import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
	"""Test the function city_country."""
	def test_city_country(self):
		"""Do form like:Santiago, Chile?"""
		formatted_name = city_country('santiago', 'chile')
		self.assertEqual(formatted_name, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Do form like:Santiago, Chile - 5000000?"""
		formatted_name = city_country('santiago', 'chile', population=5000000)
		self.assertEqual(formatted_name, 'Santiago, Chile - Population 5000000')

unittest.main()


# Testing a class
# A variety of assert methods
assertEqual(a, b)   ----->  Verify that a == b
assertNotEqual(a, b) ---->  Verify that a != b
assertTrue(x)       ----->  Verify that x is True
assertFalse(x)      ----->  Verify that x is assertFalse
assertIn(item, list)----->  Verify that item is in list
assertNotIn(item, list)-->  Verify that item is not in list

# A class to test
class AnonymousSurvey():
	"""Collect anonymous answer to a survey question."""

	def __init__(self, question):
		"""Store a question, and prepare to store responses."""
		self.question = question
		self.responses = []

	def show_question(self):
		"""Show the survey question."""
		print(question)

	def store_response(self, new_response):
		"""Store a single response to the survey."""
		self.responses.append(new_response)

	def show_results(self):
		"""Show all the responses that have been given."""
		print("Survey result:")
		for response in responses:
			print('- ' + response)


from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()


# Testing the AnonymousSurvey class
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey."""
	def test_store_single_response(self):
		"""Test that a single response is stored properly."""
		question = "What language did yhou first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('English')

		self.assertIn('English', my_survey.responses)

unittest.main()


import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey."""
	def test_store_single_response(self):
		"""Test that a single response is stored properly."""
		question = "What language did yhou first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('English')

		self.assertIn('English', my_survey.responses)

	def test_store_three_responses(self):
		"""Test that three responses are stored properly."""
		question = "What language did yhou first learn to speak?"
		my_survey = AnonymousSurvey(question)
		responses = ['English', 'Spanish', 'Mandarin']
		for response in responses:
			my_survey.store_response(response)

		for response in responses:
			self.assertIn(response, my_survey.responses)

unittest.main()


# The setUp() method
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey."""

	def setUp(self):
		"""
		Create a survey and a set of responses for use in all test methods.
		"""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Spanish', 'Mandarin']

	def test_store_single_response(self):
		"""Test that a single response is stored properly."""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		"""Test that three individual responses are stored properly."""
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

unittest.main()


# ---------------TRY IT YOURSELF-------------------------------------------
# 11-3. Employee: Write a class called Employee The __init__() method should
# take in a frst name, a last name, and an annual salary, and store each of these
# as attributes Write a method called give_raise() that adds $5000 to the
# annual salary by default but also accepts a different raise amount
# Write a test case for Employee Write two test methods, test_give_
# default_raise() and test_give_custom_raise() Use the setUp() method so
# you don’t have to create a new employee instance in each test method Run
# your test case, and make sure both tests pass
class Employee():
	"""A class for describing a employee."""
	def __init__(self, first, last, salary):
		"""Initialize the three attributes of the class."""
		self.first = first
		self.last = last
		self.salary = salary

	def give_raise(self, amount=5000):
		"""Add $5000 to the annual salary by default,
		but also accept a different raise amount.
		"""
		self.salary += amount


import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Test the Employee class."""
	def setUp(self):
		"""Create an instance."""
		self.employee1 = Employee('lichard', 'liu', 100000)

	def test_give_default_raise(self):
		"""Test the give_raise() method by giving default amount."""
		self.employee1.give_raise()
		self.assertEqual(self.employee1.salary, 105000)

	def test_give_custom_raise(self):
		"""Test the give_raise() method by giving custom amount."""
		self.employee1.give_raise(10000)
		self.assertEqual(self.employee1.salary, 110000)

unittest.main()


# Finished on Jan 19 2019.---------------------------------------------