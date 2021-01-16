# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.png', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as turtle_module
import random

caspar = turtle_module.Turtle()
turtle_module.colormode(255)
color_list = [(192, 163, 119), (126, 185, 156), (213, 213, 132), (187, 222, 201), (155, 212, 186), (137, 168, 182), (220, 217, 177), (181, 141, 159), (91, 155, 110), (145, 149, 76), (74, 123, 94), (133, 107, 67), (137, 84, 108), (191, 98, 84), (78, 106, 125), (170, 102, 123), (195, 211, 219), (220, 202, 211), (13, 45, 53), (148, 209, 215), (19, 44, 35), (226, 175, 163), (89, 146, 154), (118, 119, 153), (214, 177, 189), (53, 38, 10), (38, 81, 62), (83, 84, 16), (184, 186, 208), (33, 79, 84)]
caspar.hideturtle()
caspar.penup()
caspar.speed("fastest")
caspar.setheading(225)
caspar.forward(300)
caspar.setheading(0)
number_dots = 100

for dot_counts in range(1, number_dots + 1):
    caspar.dot(20, random.choice(color_list))
    caspar.fd(50)
    if dot_counts % 10 == 0:
        caspar.setheading(90)
        caspar.forward(50)
        caspar.setheading(180)
        caspar.forward(500)
        caspar.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()