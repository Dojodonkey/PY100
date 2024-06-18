'''
How many arguments does the str.join method expect?
 What happens if you call it with fewer or more arguments?
'''
#str.join method expects one argument and it must be an iterable. 
#no argument or a non-iterable results in a TypeError. 

str1 = "My first string." 
str2 = "My second string." 

listed1 = list(str1) 
listed2 = list(str2)

print(''.join(listed1))


