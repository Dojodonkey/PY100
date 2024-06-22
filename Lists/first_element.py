'''
Write a function that returns the first element of a list 
provided as an argument. For example: 
print(first(['Earth', 'Moon', 'Mars']))  # Earth
'''

my_input = input("write items of a list: ")   
my_list = my_input.split(",")

def first(lst): 
	if lst:
		return lst[0]
	else: 
		return None

print(first(my_list))

#not satisfactory as None is never returned if there is no input. 
