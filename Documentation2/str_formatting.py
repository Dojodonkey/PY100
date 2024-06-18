name = "Victor"
profession = "programmer"

'''
How can you print the string Hello, Victor. You are a programmer. using the str.format method?
 You should fill in the name and profession in a string literal that contains the rest of the text.
How can you achieve the same result using an f-string?
'''
#using an f-string:

print(f'Hello, {name}.You are a {profession}.')

#f-strings are generally cleaner and easier to read while str.format() uses placeholders and arguments. 

#using str.format(): 

message = "Hello {}, You are a {}." 
message_formatted = message.format(name, profession)

print(message_formatted)
