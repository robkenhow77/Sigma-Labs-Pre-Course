import math

goods = {
    "eggs": 1.50,
    "flour": 2.00,
    "milk": 0.60,
    "juice": 1.35,
    "bread": 1.00,
    "bacon": 2.30,
    "sausages": 3.05,
    "chicken": 5.00,
    "crisps": 2.10
}

offers = {
    "eggs": "2 for 1",
    "bacon": "3 for 2",
    "crisps": "4 for 3"
}

order = {}


def display_options():
    print("\npress 1 to see items, prices and offers, press 2 to view basket, "
          "press 3 to edit basket, press 4 to finish and print receipt")


def display_items_and_offers():
    print("\nGoods available")
    for item in goods:
        price = correct_decimal(goods[item])
        print(f'{item}: £{price}')

    print("\nSpecial offers:")
    for offer in offers:
        print(f'{offer}: {str(offers[offer])}')
    display_options()


def edit_basket():
    editing = True
    while editing:
        print("press 1 to add items, press 2 to remove items")
        decision = input()
        if decision == "1":
            while True:
                print("Adding item, choose good")
                good = input().lower()
                if good not in goods:
                    print("Invalid choice, choose again")
                else:
                    while True:
                        print("Choose quantity")
                        try:
                            quantity = int(input())
                            if quantity < 1:
                                print("Invalid choice, choose again")
                            else:
                                if good in order:
                                    order[good] += quantity
                                elif quantity > 0:
                                    order[good] = quantity
                                print("Item added")
                                break
                        except:
                            print("Invalid choice, choose again")
                    break
            editing = False

        elif decision == "2":
            while True:
                print("Removing item, choose good")
                good = input().lower()
                if good not in goods:
                    print("Invalid choice, choose again")
                else:
                    if good not in order:
                        print(f'no {good} in basket')
                        break
                    while True:
                        print("Choose quantity")
                        try:
                            quantity = int(input())
                            if quantity < 1 :
                                print("Invalid choice, choose again")
                            else:
                                if good in order:
                                    order[good] -= quantity
                                    if order[good] <= 0:
                                        order.pop(good)
                                    print("item removed")
                                    break

                        except:
                            print("Invalid choice, choose again")
                    break
            editing = False
        else:
            print("Invalid choice, choose again")

    display_options()


def sum_up():
    print("Basket\n")
    print("goods: quantity")
    print("Cost\n")
    total_cost = 0
    for good in order:
        if good != "total cost":
            if good not in offers:
                cost = round(goods[good] * order[good],2 )
            else:
                a = int(offers[good][0])
                b = int(offers[good][-1])
                quantity = order[good]
                price = goods[good]
                quantity_not_offer = int(quantity % a)
                quantity_offer = quantity - quantity_not_offer
                cost = round(((quantity_not_offer + quantity_offer * (b/a)) * price),2)
            total_cost += round(cost, 2)
            print(f'{good}: {order[good]}')
            print("cost: £", correct_decimal(cost), "\n" )
    print(f'\ntotal cost: £{correct_decimal(total_cost)}')
    display_options()


def correct_decimal(number):
    decimal = str(round(number - math.floor(number), 2))
    # print(number[1])
    if len(decimal) == 3:
        return str(number) + "0"
    else:
        return str(number)


def receipt():
    print("Receipt")
    total_cost = 0
    for good in order:
        if good != "total cost":
            if good not in offers:
                cost = goods[good] * order[good]
                total_cost += cost
            else:
                a = int(offers[good][0])
                b = int(offers[good][-1])
                quantity = order[good]
                price = goods[good]
                quantity_not_offer = int((quantity/a - quantity//a) * a)
                quantity_offer = quantity - quantity_not_offer
                cost = (quantity_not_offer + quantity_offer * (b/a)) * price
                total_cost += cost
            print(f'{good}: {order[good]}')
            print("cost: £", correct_decimal(cost), "\n" )
    print(f'\ntotal cost: £{correct_decimal(total_cost)}')


# Script
print("Welcome to the store, what would you like to buy?")
display_options()
shopping = True
while shopping:
    choice = input()
    if choice == "1":
        display_items_and_offers()
    elif choice == "2":
        sum_up()
    elif choice == "3":
        edit_basket()
    elif choice == "4":
        receipt()
        shopping = False
    else:
        print("Invalid choice, choose again")




