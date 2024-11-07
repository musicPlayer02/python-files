from coffee_data import  MENU, resources, profit

def check_ingredients(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("Sorry, not enough resources available to make the coffee.")
            return False
        else:
             return True
   

def update_resources(order_ingredients) :
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]              

def collect_money():
    bills_of_hundred = int(input("How many 100rs notes? "))
    bills_of_fifty = int(input("How many 50rs notes? "))
    bills_of_twenty = int(input("How many 20rs notes? "))
    bills_of_ten = int(input("How many 10rs notes? "))
    return (100*bills_of_hundred) + (50*bills_of_fifty) + (20*bills_of_twenty) + (10*bills_of_ten)
     
def compute_change(money_paid, coffee_cost):
    return money_paid - coffee_cost
    
is_on = True
while is_on:
    print("Enter 'off' to exit the machine.")
    choice = input("What would you like to have? (latte/ cappuccino/ espresso): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs.{profit}")
    else:
        coffee = MENU[choice]
        if check_ingredients(coffee['ingredients']):
            print(f"Your bill is Rs.{coffee['cost']}.") 
            money_paid = collect_money()
            change = compute_change(money_paid, coffee['cost'])
            if change < 0:
                print(f"Sorry, amount paid by you is less by {-(change)}rs. Cannot fulfil your request. Thank you. ")
            else:
                update_resources(coffee['ingredients'])
                profit += coffee['cost']
                print(f"Your  change is {change}rs and {choice} ☕️")
                print("Thank you for visiting us. Have a nice day!")