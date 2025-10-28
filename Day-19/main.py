#Python High Order Functions and Event Listeners
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
#jbefu wq
def move_forward():
    tim.forward(40)

def move_left():
    tim.left(90)
    tim.forward(40)

def move_right():
    tim.right(90)
    tim.forward(40)

screen.listen()
screen.onkey(move_forward, "space")
screen.onkey(move_left, "1")
screen.onkey(move_right, "2")
screen.exitonclick()