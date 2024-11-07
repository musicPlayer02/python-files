bill = float(input("what is your bill: "))
tip= int(input("tip amount: in percent"))
people = int(input("number of people splitting the bill: "))
tip_as_percent = tip/100
tip_amount= bill * tip_as_percent
amount_to_pay = (bill + tip_amount)/people
print("amount to be paid by each = " + str(round(amount_to_pay,2)))