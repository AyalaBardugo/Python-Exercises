from HangManArt import *


def choose_word(file_path, index):
    list_word = []
    file_object = open(file_path, 'r')
    for line in file_object:
        for word in line.split():
            list_word.append(word)

    if index < len(list_word):
        chosen_secret_word = list_word.pop(index)
    else:
        chosen_secret_word = list_word.pop(0)
    return chosen_secret_word


def show_hidden_word(secret_word, old_letters_guessed):
    word = ["_"] * len(secret_word)
    cnt = 0
    for char in old_letters_guessed:
        if char in secret_word:
            for index in secret_word:
                cnt += 1
                if index == char:
                    word[cnt - 1] = char
        cnt = 0
    return word


def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) != 1 or not (letter_guessed.isalpha()) or letter_guessed in old_letters_guessed:
        return False

    elif letter_guessed.isalpha() and len(letter_guessed) == 1 and letter_guessed not in old_letters_guessed:
        return True


def print_hangman(num_of_tries):
    num_of_tries += 1
    for key in HANGMAN_PHOTOS.keys():
        if key == num_of_tries:
            print(HANGMAN_PHOTOS.get(key))
            break


def try_update_letter_guessed(letter_guessed, old_letters_guessed, draw_man, current_word):
    list_to_str, str_with_arrows = " ", " "
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        if letter_guessed in current_word:
            print(show_hidden_word(current_word, old_letters_guessed))
            return True
        else:
            draw_man += 1
            print_hangman(draw_man)
            print(show_hidden_word(current_word, old_letters_guessed))
            return False
    else:
        print("\n X")
        map(lambda x: x.lower(), old_letters_guessed)
        sorted_list = sorted(old_letters_guessed)
        list_to_str += list_to_str.join(sorted_list)
        str_with_arrows += '->'.join(f'{list_to_str[i:i + 2]}' for i in range(0, len(list_to_str), 2))
        print(str_with_arrows)
        return True


def user_won(current_word, list_char):
    word = show_hidden_word(current_word, list_char)
    str = ""
    for ele in word:
        str += ele
    if current_word == str:
        print("\nYou won the game!! ")
        return True
    return False
