import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",     
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["@","%","&","*","$","(",")","!","?","<",">"]
print("************* welcome to easy password generator ************")
nr_letters1 = int(input("How many letters do you want in password? "))
nr_numbers1 = int(input("How many numbers do you want in password? "))
nr_symbols1 = int(input("How many symbols do you want in password? "))

# easy level
password1 = ""
for i in range(nr_letters1):
  password1 += random.choice(letters)
for i in range(nr_symbols1):
  password1 += random.choice(symbols)
for i in range(nr_numbers1):
  password1 += random.choice(numbers)
#print(password1)
password_list = list(password1)
random.shuffle(password_list)
#print(password_list)

password = ""
for i in password_list:
  password += i
print(password) 

"""
# hard level

print("************* welcome to hard password generator ************")
nr_letters = int(input("How many letters do you want in password? "))
nr_numbers = int(input("How many numbers do you want in password? "))
nr_symbols = int(input("How many symbols do you want in password? "))

password = ""
count_letters = 0
count_numbers = 0
count_symbols = 0
while len(password) < (nr_letters + nr_numbers + nr_symbols):
  select = random.randint(1,3)
  if select == 1 and count_letters < nr_letters:
    password += random.choice(letters)
    count_letters += 1
  if select == 2 and count_numbers < nr_numbers:
    password += random.choice(numbers)
    count_numbers += 1
  if select == 3 and count_symbols < nr_symbols:
    password += random.choice(symbols)
    count_symbols += 1
print(password)

"""
