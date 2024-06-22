'''
Write an is_empty_or_blank function 
to determine whether a string is either empty 
or consists entirely of spaces.
For example:
print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
'''

my_string = input("write a string: ")

def is_empty_or_blank(string): 
	return len(string.strip()) == 0

print(is_empty_or_blank(my_string))

