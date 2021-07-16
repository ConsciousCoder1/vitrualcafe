from menu import MENU, resources
from art import mug

print("\nWelcome to the Virtual Py Cafe!\nYou may not be able to physically drink your beverage,\nbut you can enjoy ordering it!\n")
print(mug)


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
        print(f"Revenue: $0")
    # else (beverage == "espresso", "latte", "cappuccino"):
    else:
        user_beverage_cost = MENU[beverage]['cost']
        print(f"\nYour Selection >> {beverage}\nDue: ${user_beverage_cost}0\n")
        
        print("Please insert coins:")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        total_quarters = .25 * quarters
        total_dimes = .10 * dimes
        total_nickels = .05 * nickels
        total_pennies = .01 * pennies
        
        total_change = total_quarters + total_dimes + total_nickels + total_pennies
        total_change = float("{:.2f}".format(total_change))
        print(f"You paid: ${total_change}.")
        
        if total_change < user_beverage_cost:
            print("Sorry, your payment is insufficient. Refunding Change...")
            print("Come back soon!")
        elif total_change > user_beverage_cost:
            change_refund = total_change - user_beverage_cost
            change_refund = float("{:.2f}".format(change_refund))
            print(f"Your change is ${change_refund}.")
            print("Thank you! Enjoy your virtual drink.")
        else:
            print("Thank you! Enjoy your virtual drink.")
            