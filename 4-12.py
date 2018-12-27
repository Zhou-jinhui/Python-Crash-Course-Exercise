'''
for value in range(1, 5):
	print(value)
'''

'''numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)
'''
'''
squares = []
for value in range(1, 11):
	squares.append(value ** 2)

print(squares)
'''
'''
for i in range(1,21):
	print(i)

for i in range(1,10**6+1):
	print(i)
'''
'''
number_list = [i for i in range(1,10**6+1)]
print(min(number_list))
print(max(number_list))
print(sum(number_list))
'''
'''
odd_number_list = [i for i in range(1,21,2)]
for i in odd_number_list:
	print(i)
'''
'''
multiples_list = [i for i in range(3,31,3)]
for i in multiples_list:
	print(i)
'''

cube_number_list = []
for value in range(1,11):
	cube = value**3
	cube_number_list.append(cube)
print(cube_number_list)

cube_number_list = [i**3 for i in range(1,11)]   # This list comprehension equals to the above block of statements.
print(cube_number_list)