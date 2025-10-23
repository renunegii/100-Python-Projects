# import colorgram
#
# colors = colorgram.extract('image.jpg', 15)
# lst_color = []
#
# for i in colors:
#     first_color = i.rgb
#     red = first_color.r
#     green = first_color.g
#     blue = first_color.b
#
#     rgb= [red, green, blue]
#     lst_color.append(tuple(rgb))
#
# print(lst_color)
import turtle
from turtle import Turtle, Screen
import random
color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251)]

timmy = Turtle()
timmy.shape("turtle")
turtle.screensize(1000,1000)
timmy.color("green")
timmy.pensize(20)
turtle.colormode(255)
# print(random.choice(color_list))
for i in range (10):
    for j in range (10):
        timmy.color(random.choice(color_list))
        timmy.pendown()
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)

screen = Screen()
screen.exitonclick()