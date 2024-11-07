print("********* Welcome to treasure island ************* \n Your mission is to find the treasure.")
choice1 = input("You are stuck at crossroads. \nWhere do you want to go? (left or right): ").lower()
if choice1 == "left":
  choice2 = input("By following the left path you have come to a lake with a bridge. \nDo you want to swim or cycle? ").lower()
  if choice2 == "cycle":
    choice3 = input("After crossing the river, you have three doors to choose from. \nEnter a door; red, yellow or black: ").lower()
    if choice3 == "red":
      print("Congrats...you have found the treasure. YOU WON")
    else:
      print("You have entered a dragon's lair. YOU LOSE.")  
  else:
    print("You drowned in the river. YOU LOSE.")
else:
  print("You fell into a hole. YOU LOSE.")
  