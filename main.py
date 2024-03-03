import random

def computer_guesses_number():
    print("Pick a number between 1 and 100 and keep it in mind.")

    lower_bound = 1
    upper_bound = 100
    response = ""
    while response != 'y':
        guess = random.randint(lower_bound, upper_bound)
        response = input(f"Is your number {guess}? Type L for lower, H for higher, and Y for yes: ").lower()
        if response == 'l':
            upper_bound = guess - 1
        elif response == 'h':
            lower_bound = guess + 1

    print(f"Computer guessed your number correctly: {guess}")





if __name__ == '__main__':
    computer_guesses_number()






