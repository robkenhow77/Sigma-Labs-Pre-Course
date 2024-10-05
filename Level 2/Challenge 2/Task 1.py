from random import randint


def guess_number():
    print("Guess a number between 0 and 100: ")
    try:
        return int(input())
    except:
        print("invalid number")
        guess_number()


random_number = randint(0,100)
# print("random number " + str(random_number))
number_of_guesses = 0

while True:
    guess = guess_number()
    number_of_guesses += 1
    if guess > random_number:
        print("number is lower")
    if guess < random_number:
        print("number is higher")
    if guess == random_number:

        break
    print("number of guesses: " + str(number_of_guesses))

print("correct, completed in " + str(number_of_guesses) + " guesses")

