#Is there a method to reverse a string,
# for example turning 'hello' into 'olleh'?

#There are two ways to do this: 
#1.) using the reversed() method. 
#Note that this only iterates a string
#and must be joined using the join() function. 

original_string = input("write a string: ") 
reversed_iterator = reversed(original_string) 
reversed_string = ''.join(reversed_iterator)

print(reversed_string) 

#2.)the second way is by slicing

reversed_string_sliced = original_string[::-1]
print(reversed_string_sliced) 

#remember slicing sytax: [start(inclusive): stop(exclusive): step] 
