from turtle import Turtle, Screen

#  OR

#import turtle
#tommy = turtle.Turtle()
#screen = turtle.Screen()

#  OR

#from turtle import *  
# tommy = Turtle()
# screen = Screen()

#  OR

#import turtle as t
# tommy = t.Turtle()
# screen = t.Screen()

tommy = Turtle()
print(tommy)
tommy.shape("turtle")
tommy.color("blue")
tommy.forward(100)
tommy.left(90)
tommy.forward(50)
tommy.left(135)
tommy.backward(200)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()