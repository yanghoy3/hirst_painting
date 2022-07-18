import turtle

import colorgram
import random
from turtle import Turtle, Screen

turtle.colormode(255)
def extract_color(num_color):
    color_tuple = []
    colors = colorgram.extract('image.jpg', num_color)
    for i in range(0, num_color):
        rgb = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)
        color_tuple.append(rgb)
    return color_tuple


palette = extract_color(34)

tim = Turtle()
tim.hideturtle()
tim.penup()


for i in range(0, 10):
    tim.goto(-225, -200+i*50)
    for _ in range(0, 10):
        tim.dot(20, random.choice(palette))
        tim.forward(50)









screen = Screen()
screen.exitonclick()

