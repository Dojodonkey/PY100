'''
Use Python's control structures to create a function 
that takes an ISO 639-1 language code and 
returns a greeting in that language. 
You can take the examples below or add whatever languages you like.

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
'''

def greet(lang_code):
	greetings = {
		'en' : 'Hello', 
		'es' : 'Hola', 
		'de' : 'Hallo', 
		'pt' : 'Ola',
	}
	return greetings.get(lang_code) 

print(greet(input("pick a language code: "))) 
	
