'''
Write code that capitalizes the words in the string 
'launch school tech & talk',
so that you get the string 
'Launch School Tech & Talk'
'''

tt_string = 'lauch school tech & talk' 

listed = tt_string.split() 

for i in range(len(listed)): 
	listed[i] = listed[i][:1].upper() + listed[i][1:]

print(' '.join(listed)) 
