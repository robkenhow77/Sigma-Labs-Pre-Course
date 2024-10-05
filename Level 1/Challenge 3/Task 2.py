# Verify integer
def ask_user_for_number():
    try:
        return int(input())
    except:
        print("Number is not an integer, try again")
        ask_user_for_number()


# 1 - sum to n
def sum_to_n():
    print("Input number: ")
    chosen_number = ask_user_for_number()
    sum_of_numbers = 0
    for number in range(chosen_number + 1):
            sum_of_numbers += number
    print(sum_of_numbers)


# 2 - sum to n, multiples of 3 and 5
def sum_to_n_3_and_5():
    print("Input number: ")
    chosen_number = ask_user_for_number()
    sum_of_numbers = 0
    for number in range(chosen_number + 1):
        if number % 3 == 0 or number % 5 == 0:
            sum_of_numbers += number
    print(sum_of_numbers)


# Sum or product
def sum_or_product():
    print("Enter 1 to sum, or 2 to multiply: ")
    option = input()
    if option == "1":
        sum_to_n()
        return
    if option == "2":
        print("Input number: ")
        chosen_number = ask_user_for_number()
        product_of_numbers = 1
        for number in range(1, chosen_number + 1):
                product_of_numbers = number * product_of_numbers
        print(product_of_numbers)
        return
    else:
        print("invalid option, choose again")
        sum_or_product()


