# functions as input - higher order function
# turtle.listen() ->  set focus on turtle screen in order to collect key events.
# turtle.onkey(fun,key) -> bind fun to key-release event of key.

from turtle import *

tim = Turtle()
myScreen = Screen()

def move_forwards():
      tim.forward(100)
      
myScreen.listen()
myScreen.onkey(key = "space", fun=move_forwards)





myScreen.exitonclick()