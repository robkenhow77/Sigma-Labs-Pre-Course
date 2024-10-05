Jane = {
    "First name": "Jane",
    "Last name": "Doe",
    "Age": 42,
    "Employed": True
}

Tom = {
    "First name": "Tom",
    "Last name": "Smith",
    "Age": 18,
    "Employed": True
}

Mariam = {
    "First name": "Mariam",
    "Last name": "Coulter",
    "Age": 66,
    "Employed": False
}

Gregory = {
    "First name": "Gregory",
    "Last name": "Tims",
    "Age": 8,
    "Employed": False
}

people = [Jane, Tom, Mariam, Gregory]


def display_names():
    for names in people:
        print("Name: " + names["First name"] + " " + names["Last name"])
        print("Age: " + str(names["Age"]))
        if names["Employed"]:
            print("Employed: Yes")
        else:
            print("Employed: No")
        print("\n")


def create_person():
    print("Please enter first name:")
    first_name = input()
    print("Please enter last name:")
    last_name = input()
    print("Please enter age:")
    age = int(input())
    while True:
        print("Please enter employment status (yes or no):")
        employment_status = input()
        if employment_status == "yes":
            employment_status = True
            break
        if employment_status == "no":
            employment_status = False
            break
    new_person = {
        "First name": first_name,
        "Last name": last_name,
        "Age": age,
        "Employed": employment_status
    }
    people.append(new_person)
    print("\n")
    display_names()


def remove_person():
    print("Give the first name of the person you would like to remove:")
    first_name = input()
    print("Give the last name of the person you would like to remove:")
    last_name = input()
    for i in range(len(people)-1):
        if people[i]["First name"] == first_name and people[i]["Last name"] == last_name:
            people.pop(i)
    print("\n")
    display_names()


def add_or_remove_prompt():
    print("Would you like to add/remove someone or finish session? (type add, remove or finish)")
    add_or_remove = str(input())
    if add_or_remove == "finish":
        return
    if add_or_remove == "add":
        create_person()
    if add_or_remove == "remove":
        remove_person()
    add_or_remove_prompt()


display_names()
add_or_remove_prompt()

