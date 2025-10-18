from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
# Creating a square using turtle functions
# for i in range (4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# creating a dashed line
for _ in range(15):
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)

screen = Screen()
screen.exitonclick()