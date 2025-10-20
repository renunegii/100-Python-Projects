from turtle import Turtle, Screen

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

for i in range (3,10):
    angle = 360/i
    for j in range(i):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

screen = Screen()
screen.exitonclick()