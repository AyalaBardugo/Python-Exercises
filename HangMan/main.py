from HangManLogic import *

draw_man = 0
list_char = []
print(HANGMAN_ASCII_ART)
path_to_word_file = input("Hi , Enter file path:  ")
word_index = int(input("Enter index:  "))
print("Let’s start! \n")

current_word = choose_word(path_to_word_file, word_index)
print(current_word)  # need to remove
print(HANGMAN_PHOTOS[1])

print(show_hidden_word(current_word, list_char))


while 1:
    if user_won(current_word, list_char):
        break
    if draw_man == 6:
        print("\nYou lost the game :(")
        break

    character_entered = input("\nGuess a letter:  ")
    character_entered = character_entered.lower()
    if not try_update_letter_guessed(character_entered, list_char, draw_man, current_word):
        draw_man += 1
