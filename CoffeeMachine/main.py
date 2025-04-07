# Coffee Machine Code
from menu import MENU, resources, coins_inserted

'''input is the money inside the machine
no return, just print'''


def report(money_stored):
    print(f"Water: {resources['water']}\n"
          f"Milk: {resources['milk']}\n"
          f"Coffee: {resources['coffee']}\n"
          f"Money: {money_stored}€")
    return


'''inputs are the users money and the cost of the chosen drink
it shows if the user gets change at all or if he had to pay more
return is True or false, at least the person had paid for the drink'''


def money_change(input_money, user_drink):
    change = input_money - MENU[user_drink]["cost"]
    change = round(change, 2)
    if change >= 0:
        print(f"You get {change}€ change.")
        return True
    else:
        change *= -1
        print(f"You have to pay {change}€  more.")
        return False


'''input is the amount of money the user put in
it asks the user how much coins and which he wants to insert
the overall money got returned'''


def pay(money_input):
    for amount_of_coin in coins_inserted:
        coins_inserted[amount_of_coin]["coins"] = int(input(f"How much {amount_of_coin} insert? "))
        money_input += coins_inserted[amount_of_coin]["coins"] * coins_inserted[amount_of_coin]["worth"]
    return money_input


'''input is the chosen drink by the user
proofing if there are enough resources for the drink
if there is enough, the resource get subtracted for every resource
if any resource is missing, the return get false, either it is True'''


def resources_check(user_drink):
    for ingredients in resources:
        if resources[ingredients] >= MENU[user_drink]["ingredients"][ingredients]:
            resources[ingredients] -= MENU[user_drink]["ingredients"][ingredients]
        else:
            return False
    return True


# money inside the machine
money_in_machine = 0
next_drink = True

while next_drink:
    # other variables defined
    money_paid = 0
    not_paid = True

    # Starting with the user input
    user_input = input("What would you like? (espresso/latte/cappuccino?) ").lower()

    if user_input == "report":
        report(money_in_machine)

    elif user_input == "off":
        print("System shut down.")
        next_drink = False

    elif user_input == "refill":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100

    else:
        if resources_check(user_input):
            print(f"You have to pay {MENU[user_input]['cost']} €.")
            while not_paid:
                money_paid = pay(money_paid)

                if money_change(money_paid, user_input):
                    not_paid = False

            money_in_machine = MENU[user_input]["cost"]
            print(f"Enjoy your {user_input}")

        else:
            print("Not enough resources")

