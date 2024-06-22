'''
Write a function that counts the number of occurrences of a substring in a string.
print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0
'''

my_string = input("write a string: ") 
my_sub = input("write a sub-string: ") 

def count_substrings(string): 
	counts = my_string.count(my_sub) 
	return counts 

print(count_substrings(my_string)) 		
