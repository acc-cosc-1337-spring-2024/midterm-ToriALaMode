#write functions here, don't add input('') statements here!
# Write a function is_prime that returns True if a number is prime False otherwise.
def prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1): #had to google this because I had no idea how to math a prime number within coding atm but there were no errors
        if number % i == 0:
            return False
    return True