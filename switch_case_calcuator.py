# calculator using dictionaries with functions

def addition(a,b):
  return a+b

def sub(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  return a/b
  
operations = {
  "-": sub,
  "+" : addition,
  "*" : multiply,
  "/" : divide,
}

def calculator():
  should_continue = True
  print("Operation List is:")
  for symbol in operations:
      print(symbol)

  num1 = float(input("\nWhat is the first number? "))

  while should_continue:
    num2 = float(input("What is the next number? "))    
    op = input("Pick an operation from the above list: ")
    calculation_function = operations[op]
    answer = calculation_function(num1,num2)
    print(f"{num1} {op} {num2} = {answer}")
  
    ifcontinue = input(f"\n Do you want to continue calculation with {answer}?  Type 'y',\n or  'n'  if you want to start a new calculation:  ")
    if ifcontinue == "y":
      num1 = answer
    else:
      should_continue = False
      calculator() 
      
calculator()