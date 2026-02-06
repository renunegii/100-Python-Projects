from turtle import Turtle,Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")

screen = Screen()
screen.listen()

def forward():
    tim.forward(20)

def backward():
    tim.backward(20)

def clockwise():
    tim.left(30)

def anticlockwise():
    tim.right(30)

def cleardrawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=anticlockwise, key="a")
screen.onkey(fun=cleardrawing, key="c")
screen.exitonclick()