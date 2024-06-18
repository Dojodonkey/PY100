'''
Using the Python documentation,
 determine how you can write large numbers in a way that makes them easier to read.
'''

#to make large numbers more readable, we can insert , or _ by using an f-string, the number, :, 
#and the symbol which we want to seperate the places. 

user_input = int(input("write a very very large number: ")) 

print(f'{user_input:,}') #1000000 = 1,000,000
print(f'{user_input:_}') #underscores are preferred in python

