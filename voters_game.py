from voters_game_data import data
import random

def format_data(account):
  account_name = account['name']
  account_fan = account['follower_count']
  account_desp = account['description']
  return f"{account_name} is a/an {account_desp}."
  
def check_answer(guess, aFan, bFan):
  if aFan > bFan:
    return guess == "A"
  else:
    return guess == "B"
 
score = 0   
continue_game = True
 
 #generate a random account from game data
accountA = random.choice(data)
accountB = random.choice(data)
  
while continue_game:  
  if accountA == accountB:
    accountB = random.choice(data)
    
  # format random data into printable format
  print(f"A: {format_data(accountA)}")
  print(f"B: {format_data(accountB)}")
  
  #get follower count
  aFan = accountA['follower_count']
  bFan = accountB['follower_count']
  
  # ask user for a guess 
  guess = input("Guess the account with more followers(a/b): ").upper()
  
  # check if user is correct
  result = check_answer(guess, aFan, bFan)
       
  #feedback
  if result:
    print("You are right.")
    score += 1
    accountA = accountB
  else:
    print(f"Sorry, you are wrong. Your score is {score}.")
    continue_game = False
