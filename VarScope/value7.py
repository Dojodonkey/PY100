'''
What will the following code do and why? Don't run it until you have tried to answer.
'''

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

#prints 2 because global a is referenced with my_function. 
#my_function is then executed, changing the value of global a.
#then prints that mutated value of a. 
