from menu import MENU, revenue, resources
from art import mug

print("\nWelcome to the Virtual Py Cafe!\nYou may not be able to physically drink your beverage,\nbut you can enjoy ordering it!\n")
print(mug)

def resources_sufficient(bev_ingredients):
    """Returns True when resources for order are available, False when not"""
    for item in bev_ingredients:
        if bev_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item} to complete this order.")
            return False
    return True

def prep_beverage(beverage, bev_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in bev_ingredients:
        resources[item] -= bev_ingredients[item]
    print(f"Here is your {beverage} ☕️. Enjoy!")

def successful_transaction(user_payment, beverage_cost):
    """Return True when user payment is sufficient, False when not"""
    if user_payment < user_beverage_cost:
        print("\nSorry, your payment is insufficient. Refunding Change...")
        print("Come back soon!")
        return False
    elif user_payment >= user_beverage_cost:
        change_refund = round(user_payment - user_beverage_cost, 2)
        print(f"Your change is ${change_refund}.")
        global revenue
        revenue += beverage_cost
        return True
                
def process_payment():
    """Returns total calculation of coins inserted by user"""
    print("Please insert coins:")
    total = int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .1
    total += int(input("How many nickels?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    total = round(total, 2)
    print(f"You paid: ${total}.")
    return total
    
is_on = True
while is_on: 
    print("Type 'Report' for report or 'Off' to Exit.")
    beverage = input("\nWhat would you like? (Espresso/Latte/Cappuccino): ").lower()
    if beverage == "off":
        is_on = False
    elif beverage == "report":
        print(f"\nWater: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Revenue: ${revenue}")
    else:
        user_beverage = MENU[beverage]
        if resources_sufficient(user_beverage["ingredients"]):  
            user_beverage_cost = MENU[beverage]['cost']
            print(f"\nYour Selection >> {beverage}\nDue: ${user_beverage_cost}0\n")
            payment = process_payment()
            if successful_transaction(payment, user_beverage_cost):
                prep_beverage(beverage, user_beverage["ingredients"])
            
            
