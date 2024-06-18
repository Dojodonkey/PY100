use_case = input("write any string: ") 

#syntax: str.rjust(width[, fillchar])
#fillchar is optional. default is a space (' ')

def right_justify(string): 
	print(use_case.rjust(10))

right_justify(use_case)

#rjust() is useful in formatting output to make it more readable. 
#for example when making buttons or tables. 
