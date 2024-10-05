from string import ascii_lowercase
from random import randint


def ask_user_for_number():
    number = input()
    if number == "1" or number == "2":
        return int(number)
    else:
        print("Bad input, try again")
        ask_user_for_number()




def reverse_name(name):
    return name[::-1]


def intersperse_name(first_name, last_name):
    combined = ""
    if len(first_name) > len(last_name):
        longest_name = first_name
    else:
        longest_name = last_name
    for i in range(len(longest_name)):
        try:
            combined += first_name[i] + last_name[i]
        except:
            combined += longest_name[i]
    return combined


def format_name(name):
    return name[:len(name)//2].capitalize() + " " + name[len(name)//2:].capitalize()


def create_username_names():
    print("enter first name:")
    first_name = input()
    print("enter last name:")
    last_name = input()
    first_name = reverse_name(first_name)
    print("new username is:")
    print(format_name(intersperse_name(first_name, last_name)))


def create_username_random():
    name = ""
    space = int(randint(3,7))
    for i in range(10):
        a = randint(0,1)
        if a == 1:
            name += ascii_lowercase[randint(0, len(ascii_lowercase) - 1)]
        else:
            name += str(randint(0,9))
    name = name[:space] + " " + name[space:]
    print(name)


# create_username_names()
# create_username_random()

print("press key 1 to generate username based on a name \n"
      "press key 2 to generate random username")
if ask_user_for_number() == 1:
    create_username_names()
else:
    print("random username:")
    create_username_random()

