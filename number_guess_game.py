import random

def no_of_chances(level):
  if level == "Easy" or "easy":
    return 10
  else:
    return 5
    
print("------- Welcome to number guessing game ------------")
print("------ I have chosen a number between 1 and 100.--------")
print(" --------- Now its your turn to guess it.-----------")
level = input("But first chose the difficulty level. 'Easy' or 'Hard': ")


def game():
  chances = no_of_chances(level)
  answer = random.randint(1,100)
  
  while chances > 0:
    print(f"You have {chances} chances!")
    guess = int(input("Guess the number: "))
    
    if guess < answer:
      print("Guess a higher number.")
    elif guess > answer:
      print("Guess a smaller number.")
    else:
      print(f"Hurray! You have won. You guessed the right number: {answer}.")
      break
    chances -= 1

  if chances == 0:
    print(f"Sorry, you lose. The correct answer was {answer}.")
    
game()