'''
Write a function that checks whether a string is empty or not. For example:

example: 
print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True
'''

my_string = input("write a string: ")

def is_empty(string): 
	return len(string) == 0 

print(is_empty(my_string))
