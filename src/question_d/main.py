# #add import
# In main write a program that continues until the user decides to quit.
# Prompt the user for land value and display the assessment value and tax assessed.
from question_d import get_assessment_value, get_tax_assessed

def main():
    while True:
        land_value = input("Enter value for land (or 'quit' to exit): ")
        if land_value.lower() == 'quit':
            print("Quitting the program.")
            break

        try:
            land_value = float(land_value)
            if land_value < 0:
                raise ValueError
            assessment_value = get_assessment_value(land_value)
            tax_assessed = get_tax_assessed(assessment_value)
            print(f"Assessment value: ${assessment_value:.2f}")
            print(f"Property tax: ${tax_assessed:.2f}")
        except ValueError:
            if input("Invalid input. Do you want to try again? (yes/no): ").lower() != 'yes':
                print("Exiting the program.")
                break