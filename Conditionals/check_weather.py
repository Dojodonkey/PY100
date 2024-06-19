'''
Initialize a variable weather with a string value being 'sunny', 'rainy', 
or whatever weather condition you choose. 
Then, write an if statement that prints:

It's a beautiful day! if weather's value is 'sunny'
Grab your umbrella. if weather's value is 'rainy'
Let's stay inside. if weather's value is anything else
Test your code with different values for weather.
'''

import random

weather_conditions = ['sunny', 'rainy', 'snowy']

random_weather = random.choice(weather_conditions)

if random_weather == 'sunny': 
	print("It's beautiful day!") 
elif random_weather == 'rainy': 
	print('Grab your umbrella.') 
else: 
	print("Let's stay inside.") 

