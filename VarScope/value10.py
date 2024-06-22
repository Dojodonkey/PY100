'''
What will the following code do and why? Don't run it until you have tried to answer.
'''

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

#because lists are mutable objects, 
#they can be modified within a function affecting the original list 
#in the global scope. 
#notice that the function must first be executed (this alters b). 
#then the altered list in printed. 




