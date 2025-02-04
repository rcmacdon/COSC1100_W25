# -----------------------------------------
# Title: Guess the Number Game (ICE 3)
# Author: Clint MacDonald
# Date: Jan 31, 2025
# Purpose: Completing ICE 3 and learning selection and iteration!
# -----------------------------------------
import random

play = True
maxNumber = 100

# loop for each time you start over and choose the difficulty
while play:
    print("""-------------------------------------
          I'm thinking of a number between 1 and 10, 100, or 1000...
          Choose your difficulty level:
          1. Easy (1-10)
          2. Medium (1-100)
          3. Hard (1-1000)
          q to quit""")
    difficulty = input("Enter your choice: ")

    # determine the choice made
    if difficulty == "1":
        maxNumber = 10
    elif difficulty == "2":
        maxNumber = 100
    elif difficulty == "3":
        maxNumber = 1000
    elif difficulty == "q":
        play = False
        continue
    else:
        print("Invalid choice. Please try again.")
        continue

    # 
    playAgain = True
    while playAgain:
        numGuesses = 0
        gameNumber = random.randint(1, maxNumber)

        # comment this out on go live
        print("TEST: ", str(gameNumber)) 

        print("I thought of a number between 1 and", maxNumber)
        print("You have to guess it!")

        guessAgain = True
        while guessAgain:
            guess = input("Enter your guess: ")

            # check if valid
            if not guess.isdigit():
                print("Invalid guess. Please try again.")
                continue

            guess = int(guess)

            if not 1 <= guess <= maxNumber:
                print("Invalid guess. Please try again.")
                continue

            numGuesses += 1

            if guess == gameNumber:
                print("Congratulations! You got it right!")
                print("You guessed the number in", numGuesses, "attempts.")

                if input("Do you want to play again? (y/n):").lower() != "y":
                    playAgain = False

                guessAgain = False
                continue

            elif guess > gameNumber:
                print("Your guess is too high, guess again!")
            else:
                print("Your guess is too low, guess again!")
        # ---- end of guessAgain loop

    # ---- end of playAgain loop
    
# ---- end of play loop

print("Goodbye")
exit()