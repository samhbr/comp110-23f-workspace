"""EX05 - Beach Scene Turtle Art Project!"""

__author__ = "730563340"

from turtle import Turtle, colormode, done

# Set the color mode for RGB values 0-255
colormode(255)

def draw_beach(turtle, x, y):
    """Draw the beach to fill the entire screen."""
    turtle.penup()
    turtle.goto(-400, -300)  # coordinates to fill the screen
    turtle.pendown()
    turtle.color(255, 200, 100)  # Light sandy color
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(800)  # Adjusted the width to fill the screen
        turtle.left(90)
        turtle.forward(150)  # Adjusted the height of the beach
        turtle.left(90)
    turtle.end_fill()

def draw_water(turtle, x, y):
    """Draw the water to fill the entire screen."""
    turtle.penup()
    turtle.goto(-400, -300)  # Start at the left-bottom corner
    turtle.pendown()
    turtle.color(0, 119, 190)  # Blue color
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(800)  # Match the width of the beach
        turtle.left(90)
        turtle.forward(600)  # Extend the height to fill the screen
        turtle.left(90)
    turtle.end_fill()

def draw_sun(turtle):
    """Draw a circular sun in the corner."""
    turtle.penup()
    turtle.goto(200, 200)
    turtle.pendown()
    turtle.color(255, 255, 0)  # Yellow color
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()

def draw_palm_tree(turtle, x, y):
    """Draw a palm tree (vertical line)."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(139, 69, 19)  # Brown color
    turtle.fillcolor(139, 69, 19)
    turtle.begin_fill()
    
    for _ in range(3):
        turtle.forward(10)
        turtle.left(120)
    turtle.end_fill()

def draw_seagull(turtle, x, y):
    """Draw a seagull at position (x, y)."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    
    for _ in range(2):
        turtle.forward(20)
        turtle.left(120)
        
    turtle.end_fill()

# Main code
screen = Turtle()
screen.speed(0)
screen.hideturtle()
screen.bgcolor("lightblue")

# Draw the beach and ocean
draw_beach(screen)
draw_water(screen)

# Draw the sun
draw_sun(screen)

# Draw palm trees (you can adjust the positions)
draw_palm_tree(screen, -150, -150)
draw_palm_tree(screen, 100, -150)

# Draw seagulls (you can adjust the positions)
draw_seagull(screen, 50, 50)
draw_seagull(screen, 100, 80)

done()
