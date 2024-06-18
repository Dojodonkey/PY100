'''
Loop over the elements of the fish_list list below, logging each one.
Terminate the loop immediately after printing the string 'Nemo'.
'''

'''
for fish in fish_list: 
	if fish == 'Nemo': 
		print(fish) 
		break
	print(fish) 
'''
#using a while loop: 

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']


index = 0

while index < len(fish_list): 
	print(fish_list[index]) 
	if fish_list[index]  == 'Nemo': 
		break
	index += 1
