import random
import logo

print(logo.logo)

def compare_numbers(user_num, comp_num):
    if user_num > comp_num:
        return "high"
    elif user_num < comp_num:
        return "low"
    else:
        return "correct"

print("Welcome to the Number Guessing Game!")
computer_choice = random.randint(1, 100)

choice = input("Do you want to play the number guessing game? (yes/no): ").lower()

if choice == "yes":
    print("Choose the difficulty level: easy, medium, hard")
    level = input("Enter the difficulty level: ").lower()

    if level == "easy":
        attempts = 10
        print("You have 10 attempts to guess the number between 1 to 100.")
    elif level == "medium":
        attempts = 7
        print("You have 7 attempts to guess the number between 1 to 100.")
    elif level == "hard":
        attempts = 5
        print("You have 5 attempts to guess the number between 1 to 100.")
    else:
        print("Invalid level! Setting difficulty to EASY by default.")
        attempts = 10

    user_input = int(input("Enter your number between 1 to 100: "))

    while attempts > 0:
        if user_input == computer_choice:
            print("Congratulations! You win the number guessing game!")
            break
        else:
            attempts -= 1
            result = compare_numbers(user_input, computer_choice)
            print(f"Your guess is too {result}.")

            if attempts == 0:
                print(f"Sorry, you lost the game! The correct number was {computer_choice}.")
                break

            print(f"Wrong choice! You have {attempts} attempts left.")
            user_input = int(input("Enter your number between 1 to 100: "))

else:
    print("Alright! Maybe next time.")
