from time import sleep
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_pos = [-40,-20,0]
snake_segments=[]
for i in range(0,3):
    segment = Turtle()
    segment.shape("square")
    segment.color("white")
    segment.penup()
    segment.goto(snake_pos[i], 0)
    snake_segments.append(segment)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range (len(snake_segments)-1,0,-1):
        new_x = snake_segments[seg_num-1].xcor()
        new_y = snake_segments[seg_num-1].ycor()
        snake_segments[seg_num].goto(new_x,new_y)
    snake_segments[0].forward(20)








screen.exitonclick()