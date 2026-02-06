from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
screen.listen()
is_race_on = False

user_bet = screen.textinput(title="Make a Bet", prompt="Choose which turtle will win the race?")
colors = ["red", "blue", "yellow", "green", "black"]
position = [80, 40, 0, -40, -80]
all_turtle = []

for i in range(0,5):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, position[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:

        if turtle.xcor() >= 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False

            if winning_turtle == user_bet:
                print(f"You won! The winning turtle is {winning_turtle}")

            else:
                print(f"You lost! The winning turtle is {winning_turtle}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()