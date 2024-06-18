'''
Python lists come with a variety of built-in methods that allow for common list manipulations.
 One such operation is determining the index of an item in the list.
'''

fruits = ["apple", "banana", "cherry", "peach", "watermelon"]

'''
How would you determine the index of the fruit "cherry" in this list?

'''
#by using the index() method. 

print(fruits.index('cherry'))

#to prevent ValueError check if the item is even in the list: 
# using in keyword

print("cherry" in fruits)   #>>>True 

