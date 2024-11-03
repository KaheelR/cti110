# Kaheel Rowe
# 11/03/2024
# P4LAB1B
# This program will draw my first and last initials

import turtle

tess = turtle.Turtle()

tess.pensize(5)
tess.color("purple")

tess.penup()
tess.goto(-50, 0) 
tess.pendown()

tess.setheading(90)  
tess.forward(100)   


tess.right(180)      
tess.forward(50)
tess.left(45)
tess.forward(70)
tess.left(180)
tess.forward(70)
tess.right(90)
tess.forward(70)

tess.penup()
tess.goto(30,0)
tess.pendown()

tess.setheading(90)  
tess.forward(100)

tess.right(90)       
tess.circle(-25, 180)  
tess.left(120)
tess.forward(60)

tess.penup()
turtle.done()

