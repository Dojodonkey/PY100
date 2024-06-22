'''
Use a for loop to iterate over the numbers dictionary 
and print each element's key/value pair.
'''

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

high = "A high number is " 
med = "A medium number is " 
low = "A low number is " 

for value in numbers.values():
	if value > 50: 
		print(f'{high}{value}.') 
	elif value > 10: 
		print(f'{med}{value}.') 
	else: 
		print(f'{low}{value}.')
 
	
#using the dict.items() method: 
for key, value in numbers.items():
    print(f"A {key} number is {value}.")
