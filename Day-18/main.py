import random
from turtle import Turtle, Screen
import  random as r
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
# Creating a square using turtle functions
# for i in range (4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# creating a dashed line
# for _ in range(15):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)

# creating an overlay of different shapes

# for i in range (3,10):
#     angle = 360/i
#     for j in range(i):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

# creating a random walk
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
def random_direction():
    l=[timmy_the_turtle.forward(40), timmy_the_turtle.left(40), timmy_the_turtle.right(40), timmy_the_turtle.back(40)]
    return random.random(l)
timmy_the_turtle.pensize(20)
for i in range(100):
    color= random_color()
    timmy_the_turtle.pencolor(color)
    random_direction()
screen = Screen()
screen.exitonclick()