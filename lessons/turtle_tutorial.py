"Practice with turtles."

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.color(255, 51, 243)

leo.penup()
leo.goto(-120, -80)
leo.pendown()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
i = i + 1

leo.speed(50)
leo.begin_fill()
# code for shape to be filled 
leo.fillcolor(32, 67, 93)
leo.end_fill()
leo.hideturtle()


bob: Turtle = Turtle()
bob.color(143, 113, 141)
bob.penup()
bob.goto(-120, -80)
bob.pendown()
bob.speed(80)

side_length: int = 300
 
i: int = 0
while (i < 3):
     bob.forward(side_length)
     bob.left(121)
i = i + 1
side_length = side_length * 0.97
done()

