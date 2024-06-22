'''
What will the following code do and why? Don't run it until you have tried to answer.
'''

a = 1

def my_function():
    print(a)
    a = 2

my_function()

#outputs UnboundLocalError because within function block, 
#a is initialized after the print function. 
#my_function wants to print the local a, not the global a, 
#leading to the error. 

