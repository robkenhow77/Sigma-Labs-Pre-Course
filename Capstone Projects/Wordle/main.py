import string
from random import randint
from colorama import Fore


# - Functions
# To validate the guess word ensuring the word is the right length,
# there are no non-alphabetical characters and that the word is in the word list.
# Three functions are used then combined in a fourth. If any stage of validation fails a new word must be given.

#  This function validates the length of the guess word to ensure
def validate_length(word):
    if len(word) == 5:
        return True
    else:
        print("invalid length")
        return False


# This function validates there are no non-alphabetical characters.
def validate_characters(word):
    letters = [letter for letter in word]
    for letter in letters:
        if letter not in string.ascii_lowercase:
            print("invalid character")
            return False
    return True


# This function validates the guess word is in the list of words sourced online.
def validate_word_in_list(word):
    if word in list_of_words:
        return True
    else:
        print("invalid word")
        return False


# This function creates the input variable then ensures all the validation steps are passed.
def guess_and_validate_word():
    while True:
        print("Enter a word: ")
        word = input().lower()
        if validate_length(word) and validate_characters(word) and validate_word_in_list(word):
            return word


# This function looks for green letters.
def find_greens(letters):
    green_letters = []
    for i in range(len(letters)):
        if letters[i] == wordle_list[i]:
            green_letters.append(True)
        else:
            green_letters.append(False)
    return green_letters


# This function looks for yellow letters.
def find_yellows(letters):
    yellow_letters = []
    for i in range(5):
        if letters[i] in wordle_list:
            yellow_letters.append(True)
        else:
            yellow_letters.append(False)
    return yellow_letters


# This function looks combines the greens and yellows,
# specifying which of the five letters should be green, yellow or black.
def greens_and_yellows_list(greens, yellows):
    combined = []
    for i in range(5):
        if greens[i]:
            combined.append("green")
        elif yellows[i]:
            combined.append("yellow")
        else:
            combined.append("black")
    return combined


# This function colours and capitalises each letter, ready to be printed.
def colour_and_capitalise_words(word, colours):
    colour_codes = []
    for colour in colours:
        if colour == "green":
            colour_codes.append(Fore.GREEN)
        elif colour == "black":
            colour_codes.append(Fore.RESET)
        elif colour == "yellow":
            colour_codes.append(Fore.YELLOW)
        else:
            raise Exception("invalid colour")
    w = [capitals.upper() for capitals in word]
    cc = colour_codes
    return f' {cc[0]}{w[0]}   {cc[1]}{w[1]}   {cc[2]}{w[2]}   {cc[3]}{w[3]}   {cc[4]}{w[4]}{Fore.RESET} '


# - Script
# Starts by reading a text file (sourced from the internet) and creating
# a list of all the words. Also removes the \n from the end of each word.
file = open("WORDS.txt", "r")
list_of_words = []
for words in file:
    list_of_words.append(words[:5])

# Selecting a random word from list and defining the variable.
wordle = list_of_words[randint(0, len(list_of_words) - 1)]
wordle_list = [letter for letter in wordle]

# Printing for aesthetics
print(" W  O  R  D  L   E")
for i in range(6):
    print("[ ] [ ] [ ] [ ] [ ]")


tries = 0   # Counts the number of attempts.
guesses = []    # Stores the previous attempts to be displayed.
while True:
    tries += 1
    guess = guess_and_validate_word()
    characters = [letter for letter in guess]
    letter_colours = greens_and_yellows_list(find_greens(characters), find_yellows(characters))

    for previous_guess in guesses:
        previous_letters = [letter for letter in previous_guess]
        previous_letter_colours = (
            greens_and_yellows_list(find_greens(previous_letters), find_yellows(previous_letters)))
        print(colour_and_capitalise_words(previous_guess, previous_letter_colours))

    print(colour_and_capitalise_words(guess, letter_colours))
    for i in range(6 - tries):
        print("[ ] [ ] [ ] [ ] [ ]")
    guesses.append(guess)
    if guess == wordle:
        print(f"Well done, you won in {tries} goes!")
        break
    elif tries == 6:
        print(f"The word was {wordle}, you lose!")
        break
