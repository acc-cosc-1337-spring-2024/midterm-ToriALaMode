# #add import
# In main write a program that will continue until users decides to quit, in the loop ask the user for a string and display it's reverse value.
from question_b import reverse_string

def reversed_text():
    while True:
        user_input = input("Enter characters (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("Quitting program.")
            break
        else:
            print("Reversed characters:", reverse_string(user_input))