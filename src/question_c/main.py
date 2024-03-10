# #add import
# Write a program that runs until the user decided to quit, prompt the user for a number, 
# and display the result.
from question_c import prime_number
def prime():
    while True:
        user_input = input("Enter a number (or 'quit' to exit): ") 
        if user_input.lower() == 'quit':
            print("Exiting the program.")
            break
        else:
            try: # displaying a result for every outcome, hopefully okay to use try/except
                number = int(user_input)
                if prime_number(number):
                    print(number, "is a prime number.")
                else:
                    print(number, "is not a prime number.")
            except ValueError:
                print("Error. Enter a valid number or select 'quit'.")