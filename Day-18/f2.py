from turtle import Turtle,Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

#Creating a spirograph
timmy_the_turtle.pensize(2)
timmy_the_turtle.fillcolor("black")
timmy_the_turtle.speed(0)
timmy_the_turtle.hideturtle()
for i in range(6):
    for color in ('red', 'magenta', 'blue',
                  'cyan', 'green', 'white',
                  'yellow'):
        timmy_the_turtle.color(color)
        timmy_the_turtle.circle(100)
        timmy_the_turtle.left(10)


screen = Screen()
screen.exitonclick()