weight = float(input ("enter you weight (in kgs): "))
height = float(input("enter your height (in metres): "))
bmi = weight/(height**2)
print(bmi)
bmi = round(bmi,2)
print(bmi)
if bmi<18.5:
  print("underweight")
elif bmi<25:
  print("healthy weight")
elif bmi<30:
  print("overweight")
else:
  print("obese")