# #------------------------------------------- " Guess the number" game -------------------------------------------#
# # Task: Create a Python program for a "Guess the Number" game. The game will generate a random number within a specified range and prompt the user to guess the number. The program provides feedback based on the user's guess - whether it's too high, too low, or correct. The game continues until the user guesses the number correctly.
# # Requirements:
# # Random Number Generation: The program should generate a random number within a given range (e.g., 1 to 10). You can use the random.randint(1, 10) method, after including in your code import random
# # User Input: Prompt the user to enter their guess. Ensure, the user guess is in the range, and if not, display "Your guess is out of bounds."
# # Feedback to User: After each guess, the program should provide feedback: 
# # If the guess is too high, display "Too hight!"
# # If the guess is too low, display "Too low!"
# # If the guess is correct, display "Congratulations! You guessed it right."
# # Repeat Guesses: The game should continue, allowing the user to guess again if the guess is incorrect.
# # Terminate the Game: Once the correct number is guessed, the game should end with message "Bravo, you guessed my number"
# # Optional - Guess Counter: Keep track of the number of guesses the user makes and display this count when the correct number is guessed.
# # Bonus Challenge:
# # Add a feature to limit the number of guesses a user can make. If the user doesn't guess the number within the limit, end the game with a message indicating that the user has lost.
# # Implement a difficulty level for the game (e.g., easy, medium, hard), where each level has a different range of numbers or a different number of allowed guesses.
# #------------------------------------------------------------------------------------------------------------------#
# My code:

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("Choose difficulty: easy,medium or hard")
    
    difficulty = input("Enter difficulty: ")

    if difficulty == "easy":
        secret_number = 4
        max_number = 5
    elif difficulty == "medium":
        secret_number = 7
        max_number = 10
    elif difficulty == "hard":
        secret_number = 14
        max_number = 20

    print(f"Generating a  number between 1 and {max_number}.")

    guess = 0
    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed it right.")
            


guess_the_number() # Run the game
