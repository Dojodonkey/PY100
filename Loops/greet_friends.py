'''
Your friends just showed up! 
Given the following list of names, 
use a for loop to greet each friend individually.
'''

friends = ['Sarah', 'John', 'Hannah', 'Dave']

for i in range(len(friends)): 
	print(f'Hello, {friends[i]}!') 

#using better comprehension: 

for friend in friends: 
	print(f'Hello, {friend}!') 

