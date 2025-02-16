import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if guess is correct
            if guess == secret_number:
                print(f"Congratulations! You found the number in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
            
            # Show remaining attempts
            print(f"Attempts remaining: {max_attempts - attempts}")

        except ValueError:
            print("Please enter a valid number!")
            continue

    print(f"Game Over! The number was {secret_number}")

# Start the game
if __name__ == "__main__":
    while True:
        number_guessing_game()
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break 