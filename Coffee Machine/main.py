MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def calculate_resource(choice, need_ingredients):
    for item in need_ingredients:
        resources[item] -= need_ingredients[item]
    return resources

def calculate_money(drink):
    cost = drink["cost"]
    print("Please insert coins.")
    quarters = int(input('How many querters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    inserted_money = 0.25 * quarters + 0.1 * dimes + 0.05  * nickles + 0.01 * pennies

    if inserted_money < cost :
        print('Sorry, that is not enough money. Money refunded. ')
        return
    else:
        returned_money = inserted_money - cost
        print(f'Here is ${round(returned_money,2)} in change.')
        print(f'Here is your {choice} ☕️. Enjoy!')
        global profit
        profit += cost

is_on = True

while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        is_on = False
        print('You just turned the coffee mahcine off.')
    elif choice == 'report':
        print(f'Water : {resources["water"]}')
        print(f'Milk : {resources["milk"]}')
        print(f'Coffee : {resources["coffee"]}')
    else:
        drink = MENU[choice]
        calculate_resource(choice, drink["ingredients"])
        if resources["water"] <= 0 :
            print('Sorry, there is not enough water. ')
        elif resources["milk"] <= 0:
            print('Sorry, there is not enough milk. ')
        elif resources["coffee"] <= 0:
            print('Sorry, there is not enough coffee. ')
        else:
            calculate_money(drink)



