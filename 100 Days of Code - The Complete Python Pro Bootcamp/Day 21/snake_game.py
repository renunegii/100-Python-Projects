from turtle import Turtle, Screen

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")

snake_pos = [0,-20,-40]
for i in range(0,3):
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.goto(snake_pos[i],0)




screen.exitonclick()