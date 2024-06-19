'''
Building on your solutions from the previous exercises, 
write a function local_greet that takes a locale as input, 
and returns a greeting. 
The locale lets us greet people from different countries appropriately, 
even when they share a common language.
'''
#solution from local1.py 

def extract_language(locale):
        return locale.split('_')[0]

#solution from locale2.py

def extract_region(locale):
        return locale[3:5] 


#solution from internat1.py

def greet(lang_code):
	greetings = {
		'en' : 'Hello',
                'es' : 'Hola',
                'de' : 'Hallo',
                'pt' : 'Ola',
	}
	return greetings.get(lang_code)

locale = input("write a locale: ") 

def locale_greet(locale): 
	extract_language(locale)	
	if extract_language(locale) == 'en': 
		extract_region(locale)
		if extract_region(locale) == 'US':
			print("Hey!") 
		elif extract_region(locale) == "GB": 
			print("Hallo Govna!")
		else: 
			print("No hables ingles eh?!") 

locale_greet(locale)
