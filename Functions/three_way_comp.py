'''
Write a function that compares the length of two strings. 
It should return -1 if the first string is shorter, 
1 if the second string is shorter, 
and 0 if they're of equal length.
'''

str1 = input("str1: ") 
str2 = input("str2: ") 

def compare_by_length(str1, str2): 
	if len(str1) > len(str2): 
		print('1') 
	elif len(str1) < len(str2): 
		print('-1') 
	elif len(str1) == len(str2): 
		print('0') 

compare_by_length(str1, str2) 
