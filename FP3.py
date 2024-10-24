import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Ask the user if they want to play
    play_game = input("Do you want to play? (yes/no): ").strip().lower()
    
    if play_game == "no":
        print("Maybe next time!")
        return
    
    while play_game == "yes":
        # Generate a random number between 1 and 10
        secret_number = random.randint(1, 10)
        guessed_correctly = False
        
        print("I have chosen a number between 1 and 10. Try to guess it!")
        
        while not guessed_correctly:
            guess = input("Enter your guess: ")
            
            # Validate the input
            if not guess.isdigit():
                print("Please enter a valid number.")
                continue
            
            guess = int(guess)
            
            if guess < 1 or guess > 10:
                print("Your guess is out of range! Please guess a number between 1 and 10.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You've guessed the number!")
                guessed_correctly = True
        
        # Ask the user if they want to play again
        play_game = input("Do you want to play again? (yes/no): ").strip().lower()
    
    print("Thank you for playing! Goodbye!")

# Start the game
number_guessing_game()
