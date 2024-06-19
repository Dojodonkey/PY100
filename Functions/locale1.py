'''
Write a function that extracts the language code from a locale. 
A locale is a combination of a language code, a region, 
and usually also a character set, 
e.g en_US.UTF-8.
'''

locale = input("write a locale: ") 

def extract_language(locale): 
	return locale.split('_')[0]

print(extract_language(locale))
