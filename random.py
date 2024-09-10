import random

def guess_the_number():
    random_number = random.randint(1, 100)
    attempts = 10
    
    print("Welcome to the 'Guess The Number' game!")
    print("I've chosen a number between 1 and 100. Can you guess it?")
    print(f"You have {attempts} attempts to guess the correct number.")

    while attempts > 0:
        try:
            user_guess = int(input("Enter your guess: "))
            
            if user_guess < random_number:
                print("Too low! Try again.")
            elif user_guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {random_number} correctly.")
                break

            attempts -= 1
            print(f"Remaining attempts: {attempts}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")
        
        if attempts == 0:
            print(f"Sorry! You've run out of attempts. The correct number was {random_number}.")

guess_the_number()
