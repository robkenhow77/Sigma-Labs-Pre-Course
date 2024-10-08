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


print("enter first name:")
first_name = input()
print("enter last name:")
last_name = input()
print("\n" + "intersperse name is:")
first_name = reverse_name(first_name)
print(intersperse_name(first_name, last_name) + "\n")
print("new name is:")
print(format_name(intersperse_name(first_name, last_name)))

