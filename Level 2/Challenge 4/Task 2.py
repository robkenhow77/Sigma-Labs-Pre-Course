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
