import turtle
from turtle import Turtle,Screen
import random
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

# creating a random walk

timmy_the_turtle.pensize(10)
turtle.colormode(255)
def random_color():
    r= random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
turtle_direction=[0,90,180,270]
for i in range(200):
    timmy_the_turtle.speed(10)
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.setheading(random.choice(turtle_direction))
    timmy_the_turtle.forward(40)

screen = Screen()
screen.exitonclick()

