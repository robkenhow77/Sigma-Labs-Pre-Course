animals = [
    {"name": "Fluffy", "type": "dog"},
    {"name": "Parsley", "type": "dog"},
    {"name": "Ginger", "type": "cat"},
    {"name": "Biscuit", "type": "cat"}
]


def say_hello_to_pets(pets):
    for pet in pets:
        print(f'{"Woof" if pet["type"] == "dog" else "Meow"}, {pet["name"]}!')


say_hello_to_pets(animals)

# Errors
#  - Two semicolons can be removed.
#  - hello_messgae variable can be removed unless you want to add an empty string
#    in the event pet type isn't a cat or dog,
#    in this case add a pet_message variable as well.
#  - pet_name variable should equal pet["name"] not pet.name
#  - An infinte loop is created with the final if statement.

# Improvements
# - The if statments to identify cat or dog can be replaced and put into the f string, 
#   however this will set any animal type that isn't a dog to say meow.
#   This is resolved in the next task with the error exception.
