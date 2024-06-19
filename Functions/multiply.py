'''
Examine the function invocation below. 
Write the function multiply, 
such that it accepts two arguments and returns the product of its arguments. 
You may assume that the function arguments will always be numbers.
'''

#multiply(12, 4)      # 48

num1 = int(input("num1 = "))
num2 = int(input("num2 = ")) 

def multiply(num1, num2): 
	return num1*num2 

print(multiply(num1, num2))

