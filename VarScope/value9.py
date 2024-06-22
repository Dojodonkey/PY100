'''
What will the following code do and why? Don't run it until you have tried to answer.
'''

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

#because integers are immutable, their values cannot be changed. 
#when my_function is called with a as an argument, the local variable, b, 
#is set to reference the same value as a (7). 
#execution of my_function creates a new object(17) and updates variable b. 
#However, the global variable a remains unaffected at value 7. 

