animals = [
    {"name": "Fluffy", "type": "dog"},
    {"name": "Parsley", "type": "dog"},
    {"name": "Ginger", "type": "cat"},
    {"name": "Biscuit", "type": "cat"},
    {"name": "Poppy", "type": "cow"}
]


def say_hello_to_pets(pets):
    for pet in pets:
        if pet["type"] != "dog" and pet["type"] != "cat":
            raise Exception(pet["type"] + " is an invalid animal type")
        print(f'{"Woof" if pet["type"] == "dog" else "Meow"}, {pet["name"]}!')


say_hello_to_pets(animals)
