water = 400
milk = 500
coffee = 250
amount = 0
#Menu starts here
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}
# TODO 1: Ask What would you like to the user.
# TODO 2: Check if there's enough resources to buy that item.
# TODO 3: Ask the user to insert coins and then calculate the final amount given by user.
# TODO 4: Check Transaction is enough or not, if not print "not enough" if yes give remaining money back and give item and next time report should be updated.
#Report function
#water
#milk
#coffee
def report():
    print(f"water: {water}")
    print(f"milk: {milk}")
    print(f"coffee: {coffee}")
    print(f"money: {amount}")
#function to check resources
def check_resources(item):
    if water >= MENU[item]["ingredients"]["water"]:
        if milk >= MENU[item]["ingredients"]["milk"]:
            if coffee >= MENU[item]["ingredients"]["coffee"]:
                return True
            else: return False
        else: return False
    else: return False

def money_calc():
    penny = 0.01 * int(input("How many penny? "))
    nickel = 0.05 * int(input("How many nickel? "))
    dime = 0.10 * int(input("How many dime? "))
    quarter = 0.25 * int(input("How many quarter? "))
    total_money = penny + nickel + dime + quarter
    return total_money

def process_trans(money, item):
    global amount, water, milk, coffee
    if money > MENU[item]["cost"]:
        left_amount = money - MENU[item]["cost"]
        print(f"Your {left_amount} left change.")
        print(f"Here's your order! Enjoy {item}!")
        amount += MENU[item]["cost"]
        deduct_resources(item)
        # return amount
    elif money == MENU[item]["cost"]:
        print(f"Here's your order! Enjoy {item}!")
        amount += MENU[item]["cost"]
        deduct_resources(item)
        # return amount
    else:
        print(f"Sorry, this amount is not enough to buy a {item}, Refund Successful.")
        # return amount

def deduct_resources(item):
    global water, milk, coffee
    water = water - MENU[item]["ingredients"]["water"]
    milk = milk - MENU[item]["ingredients"]["milk"]
    coffee = coffee - MENU[item]["ingredients"]["milk"]



def choose_menu():
    choose = input("What would you like? (espresso/latte/cappuccino): ")
    if choose == "report":
        report()
    elif choose == "espresso":
        if check_resources(choose):
            money = money_calc()
            process_trans(money, choose)
        else:
            print("Sorry, there's no enough material! See you again")

    elif choose == "latte":
        if check_resources(choose):
            money = money_calc()
            process_trans(money, choose)
        else:
            print("Sorry, there's no enough material! See you again")

    elif choose == "cappuccino":
        if check_resources(choose):
            money = money_calc()
            process_trans(money, choose)
        else:
            print("Sorry, there's no enough material! See you again")

    else:
        print("You entered a wrong item.")

while True:
    choose_menu()
    cont = input("Type 'y' to buy again and 'n' to quit. ")
    if cont == 'n':
        break
