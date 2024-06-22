'''
What will the following code do and why? 
Don't run it until you have tried to answer.
'''

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

#attempt to reassign x inside the function returns UnboundLocalError
#because x is not initialized as a local variable. 
#To modify the x we need to use the global keyword. 

'''
x = 10

def my_function():
    global x         #referencing global x
    x = x + 5
    print(x)

my_function()

#prints 15 twice (function prints x, called function also prints x) 
#to print only once, alter print x to return x. 
'''
