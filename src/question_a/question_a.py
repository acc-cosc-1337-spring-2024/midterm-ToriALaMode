#write functions here, don't add input('') statements here!
# Write a program that generates a random number in the range of 1 through 5, and asks the user to guess what the number is. If the user guesses the number, the application should congratulate the user and generate a new random number so the game can start over.
# Function:
# get_random_number 
# def test_config():
#     return True

import random
def get_random_number():
    return random.randint(1, 5)
def test_config():
    return True