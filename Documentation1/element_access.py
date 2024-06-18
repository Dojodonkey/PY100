'''
Locate the documentation for the list built-in object in Python Documentation.

How can we access the second element ('and') in the list ['fish', 'and', 'chips']?
'''

my_list = ['fish', 'and', 'chips']

print(my_list[1])

#to access an item in a list we need to know its index. 
#if this is not known, we can use the list.index() method

index_of_and = my_list.index('and') 
print(index_of_and) 


