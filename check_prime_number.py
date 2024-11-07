import math
def prime_check(n):
  res = True
  if n in [1,2,3]:
    print(f"{n} is a prime number.")
  else:
    for i in range(2,math.ceil(math.sqrt(n))+1):
      if n%i == 0:
        res = False
        break
    if res:
      print(f"{n} is a prime number.")
    else:
      print(f"{n} is not a prime number.")
     
num = int(input("Enter a number: "))
prime_check(num)