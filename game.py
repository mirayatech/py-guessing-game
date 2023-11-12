import random

random_number = random.randint(1, 10)
guess = input("Guess a number between 1 and 10: ")
guess = int(guess)

while True:
    if guess > random_number:
        print("You guessed too high!")
        guess = input("Guess a number between 1 and 10: ")
        guess = int(guess)
    elif guess < random_number:
        print("You guessed too low!")
        guess = input("Guess a number between 1 and 10: ")
        guess = int(guess)
    else:
        print("You guessed correctly!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            random_number = random.randint(1, 10)
            guess = None
        else:
            print("Thank you for playing!")
            break
