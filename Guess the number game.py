logo = "welcome to number guessing game"
print(logo)

import random


computer_choice = random.randint(1, 100)

# print(f"psst! computer's number is {computer_choice}")  to test code

difficult_level = input("Choose a difficulty level: easy or hard ")
if difficult_level.lower() == "hard":
    attempts_allowed = 8
else:
    attempts_allowed = 5

attempts_made = 0

while attempts_made < attempts_allowed:
    user_guess = int(input("Make a number guess between 1 and 100: "))
    attempts_made += 1
    if user_guess != computer_choice:
        print(f"Incorrect! You have {attempts_allowed - attempts_made} attempts remaining.")
        if user_guess > computer_choice:
            print("Too high")
        elif user_guess < computer_choice:
            print("Too low")
    else:
        print(f"Congratulations! You guessed the number in {attempts_made} attempts. The correct answer was {computer_choice}.")
        break
else:
    print(f"Game over! You didn't guess the number. The correct answer was {computer_choice}.")
