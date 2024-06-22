'''
Write a function that returns the last element 
of a list provided as an argument. For example:
print(last(['Earth', 'Moon', 'Mars']))  # Mars
'''
my_input = input("write items of a list: ")
my_list = my_input.split(",")

def last(lst):
        if lst:
                return lst[-1]
        else:
                return None

print(last(my_list))

