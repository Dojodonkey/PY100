'''
Use a for loop to iterate over the numbers dictionary 
and return a list containing each number divided 
by 2 as an integer. The result should be truncated to an integer. 
Assign the returned list to 
a variable named half_numbers and print its value using print.
'''

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

numbers_div = []

for i in numbers.values():
	numbers_div.append(i // 2)

print(numbers_div) 
	
