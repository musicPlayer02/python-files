letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def caeser_cipher(msg, n, direction):
  n = n % 26
  cipher_text = ""
  if direction == "decode":
    n *= -1
  for i in msg:
    if i not in letters:
      cipher_text += i
    else:
      pos = letters.index(i) + n
      cipher_text += letters[pos]
  print(f"The {direction}d message is {cipher_text}")
   
"""def encode(i,n):
  new_index = letters.index(i) + n
  if new_index > 25:
    new_index = (new_index % 25) - 1
  return new_index
   
def decode(i,n):
  new_index = letters.index(i) - n
  while new_index < 0:
    new_index = new_index + 25 + 1
  return new_index"""
should_end = False
while not should_end:
  choice = input("Enter 'decode' or 'encode' as per your choice: ")
  text = input("Enter the message: ").lower()
  shift = int(input("Enter the shift number: "))
  caeser_cipher(text,shift,choice)
  restart = input("Type 'yes' if you want to continue, otherwise, type 'no'. ")
  if restart == 'no':
    should_end = True
    print("Goodbye...")