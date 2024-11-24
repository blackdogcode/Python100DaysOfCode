import data

profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "bean": 100
}


def coffee_machine_status(resource: dict, income: float):
    for item in resource:
        print(f"{item.title()}: {resource[item]}")
    print(f"Money: ${income:.2f}")


def is_resource_sufficient(resource: dict, beverage: dict):
    for ingredient, quantity in beverage['ingredients'].items():
        if resource[ingredient] < quantity:
            print(f"Sorry, that's not enough {ingredient}")
            return False
    return True


def get_money():
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


while True:
    coffee = input("What would you like to drink?☕ 'espresso' or 'latte' or 'cappuccino': ")
    # hidden command for owner
    if coffee == "report":
        coffee_machine_status(resources, profit)
        continue
    if coffee == "off":
        break
    # process coffee
    if is_resource_sufficient(resources, data.MENU[coffee]):
        print("Resource is sufficient")
        menu_cost = data.MENU[coffee]['cost']
        print("Please insert coins")
        insert_money = get_money()
        if menu_cost > insert_money:
            print("Sorry,that's not enough money. Money refunded")
            continue
        else:
            if menu_cost < insert_money:
                print(f"Here is ${insert_money - menu_cost:.2f} dollar in change")
            print(f"Here is your {coffee}. Enjoy!")
            # deduct the ingredients amount from resources machine has
            for ingredient, quantity in data.MENU[coffee]['ingredients'].items():
                resources[ingredient] -= quantity
            profit += menu_cost
    else:
        continue
