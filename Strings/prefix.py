'''
Write a function that checks whether a string starts with a specific prefix
print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True
'''

prefix = input("write prefix: ") 
my_string = input("write a string: ") 

print(prefix in my_string)

#bug in code because prefix in this case would 
#not necessarily have to be in the beginning 
#or that order or length of characters.


#launch's solution using startswith() method
'''
def starts_with(string, prefix):
    return string.startswith(prefix)
'''
