dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimentions[0] = 250   Tuple is immutable.

for dimension in dimensions:
	print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)            # We can overwrite a tuple instead of modifying it.
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)

#   TRY IT YOURSELF
# 4-13. Buffet: A buffet-style restaurant offers only fve basic foods Think of fve
# simple foods, and store them in a tuple
# •	 Use a for loop to print each food the restaurant offers
# •	 Try to modify one of the items, and make sure that Python rejects the
# change
# •	 The restaurant changes its menu, replacing two of the items with different
# foods Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu

buffet_foods = ("rice", "noodles", "fruit", "bread", "vegetables")
print("The buffet foods are:")
for food in buffet_foods:
	print(food + ".")

buffet_foods = ("cakes", "noodles", "fruit", "bread", "vegetables")
print("\nThe new buffet foods are:")
for food in buffet_foods:
	print(food + ".")

