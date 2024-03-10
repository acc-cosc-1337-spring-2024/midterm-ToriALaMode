# add import

# In main write a program that runs until the user decides to quit. (User continue loop)
# Create another loop, the game loop, that loops until the user guesses the number.
# If the user guesses congratulate else ask them to try again.
from question_a import get_random_number

def user_continue_loop():
    user_input = input("Continue? (yes/no): ")
    return user_input.lower() == 'yes'

def game_loop():
    while True:
        while True:
            random_number = get_random_number()
            guessed_number = int(input("Guess a number between 1 and 5: "))

            if guessed_number == random_number:
                print("Correct! Congrats!")
                break
            else:
                print("Try again?")

        if not user_continue_loop():
            print("Quitting program")
            break