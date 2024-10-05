def reverse_name(name):
    return name[::-1]


def intersperse_name(first, last):
    combined = ""
    if len(first) > len(last):
        a = first_name
    else:
        a = last_name
    for i in range(len(a)):
        try:
            combined += first_name[i] + last_name[i]
        except:
            combined += a[i]
    return combined


def format_name(name):
    return name[:len(name)//2].capitalize() + " " + name[len(name)//2:].capitalize()


print("enter first name:")
first_name = input()
print("enter last name:")
last_name = input()
print("intersperse name is:")
first_name = reverse_name(first_name)
print(intersperse_name(first_name, last_name))
print("new name is:")
print(format_name(intersperse_name(first_name, last_name)))
