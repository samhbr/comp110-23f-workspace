"""EX05 - Beach Scene Turtle Art Project!"""

__author__ = "730563340"

from turtle import Turtle, colormode, done

# Set the color mode for RGB values 0-255
colormode(255)

def draw_beach(turtle):
    """Draw the beach."""
    turtle.penup()
    turtle.goto(-150, -50)
    turtle.pendown()
    turtle.color(245, 222, 179)  # Sand color
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

def draw_water(turtle):
    """Draw the water."""
    turtle.penup()
    turtle.goto(-150, -150)
    turtle.pendown()
    turtle.color(0, 119, 190)  # Blue color
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

def draw_sun(turtle):
    """Draw a simple sun in the corner."""
    turtle.penup()
    turtle.goto(200, 200)
    turtle.pendown()
    turtle.color(255, 255, 0)  # Yellow color
    turtle.begin_fill()
    for _ in range(12):
        turtle.forward(20)
        turtle.right(150)
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

def create_beach_scene():
    """Create the beach scene."""
    beach_turtle = Turtle()
    water_turtle = Turtle()
    sun_turtle = Turtle()
    palm_tree_turtle = Turtle()

    draw_beach(beach_turtle)
    draw_water(water_turtle)
    draw_sun(sun_turtle)
    
    for i in range(5):
        draw_palm_tree(palm_tree_turtle, -50 + i * 50, -50)  # Draw palm trees in a loop

if __name__ == "__main__":
    create_beach_scene()
    done()
