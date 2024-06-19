'''
Similar to the previous exercise,
write a function that extracts the region code from a locale.
'''

locale = input("write a locale: ") 

def extract_region(locale): 
	return locale[3:5]

print(extract_region(locale)) 
