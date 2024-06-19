'''
Take your code from the previous Check the Weather exercise 
and rewrite it as a match-case statement. 
Feel free to add more cases besides 'sunny' and 'rainy'.
'''

import random

weather_conditions = ['sunny', 'rainy', 'snowy'] 

random_weather = random.choice(weather_conditions) 

match random_weather: 
	case 'sunny':
		print("It's a beautiful day.") 
	case 'rainy': 
		print("Grab your umbrella.") 
	case 'snowy': 
		print("Let's stay inside.") 
