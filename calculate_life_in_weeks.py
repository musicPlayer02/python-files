#assuming there are no leap years.
age = int(input("Enter your age(as integer): "))
weeks_lived = age*52
days_lived = weeks_lived*7
hours_lived = days_lived*24
print(f"you have been living for {weeks_lived} weeks.")
print(f"you have been living for {days_lived} days.")
print(f"you have been living for {hours_lived} hours.")
