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

timmy_the_turtle.pensize(20)
turtle_colors = [
    "blue","IndianRed","Red", "purple","DarkOrchid","DeepSkyBlue","LightSeaGreen","SeaGreen","CornFlowerBlue"]
turtle_direction=[0,90,180,270]
for i in range(200):
    timmy_the_turtle.speed(10)
    timmy_the_turtle.color(random.choice(turtle_colors))
    timmy_the_turtle.setheading(random.choice(turtle_direction))
    timmy_the_turtle.forward(40)


screen = Screen()
screen.exitonclick()