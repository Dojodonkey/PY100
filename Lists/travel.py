'''
Write a function that, without using the built-in in operator, 
checks whether a specific destination is included within destinations. 
For example: 
When checking whether 'Barcelona' is contained in destinations, 
the expected output is True, 
whereas the expected output for 'Nashville' is False.
'''
my_city = input("city: ") 

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city, list): 
	if city in list: 
		return True
	else: 
		return False


print(contains(my_city, destinations))
