print("********* welcome to pizza delivery **********")
size = input("enter pizza size (s,m or l): ")
add_onion = input("do you want to add onion (y or n): ")
extra_cheese = input("do you want extra cheese (y or n): ")
bill = 0
if size == 's':
  bill += 100
elif size == 'm':
  bill += 200
elif size == 'l': 
  bill += 300
if add_onion == 'y':
  if size == 's':
    bill += 10
  elif size == 'm':
    bill += 20
  elif size == 'l': 
    bill += 30
if extra_cheese == 'y':
  bill += 50
  
print(f"total bill is {bill}.")
  
  