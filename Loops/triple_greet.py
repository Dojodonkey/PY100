'''
Write a loop that prints the value
of the greeting variable three times.
'''

greeting = 'Aloha!'

print(greeting * 3)

#to include a space: 
print((greeting + ' ') * 3)

#using a for loop: 

for i in range(3): 
	print(greeting) 

#using a while loop: 

index = 3

while index > 0: 
	print(greeting) 
	index -= 1 
