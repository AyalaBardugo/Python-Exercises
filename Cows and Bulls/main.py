from CowAndBullsLogic import *

number_of_attempts = 0
num = rand_number()
print("Welcome to the Cows and bulls game")

while number_of_attempts < 10:
    num_input = input("Hi, Enter the number to guess:  ")
    if not checkInput(num_input):
        print("You entered an invalid number , Try again")
        exit(1)

    print(num_of_cows_and_bulls(num, num_input))
    number_of_attempts += 1

    if num == num_input:
        print("You won the game!!")
        answer = input("Do you want to play again? , Write yes or no:  ")
        if answer == "yes":
            number_of_attempts = 0
            num = rand_number()
        else:
            exit(1)

print("You lost the game!!")



