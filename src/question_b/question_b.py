#write functions here, don't add input('') statements here!
# Create a function named reverse_string that has one parameter named string1 that returns the
# reverse of the string. MUST USE A WHILE LOOP. DO NOT USE STRING SLICING!!!
def reverse_string(string1):
    reversed_string = ''
    index = len(string1) - 1
    
    while index >= 0:
        reversed_string += string1[index]
        index -= 1
    
    return reversed_string