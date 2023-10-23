"""EX05 - Beach Scene Turtle Art Project!"""

__author__ = "730563340"

from turtle import Turtle, Screen

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("sky blue")

# Function to draw the beach.
def draw_beach(turtle):
    """Draw the beach."""
    turtle.penup()
    turtle.goto(-400, -300)
    turtle.pendown()
    turtle.color("sandy brown")  # Sandy color
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(800)
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
    turtle.end_fill()

# Function to draw the water.
def draw_water(turtle):
    """Draw the water."""
    turtle.penup()
    turtle.goto(-400, -300)
    turtle.pendown()
    turtle.color("deep sky blue")  # Blue color
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(800)
        turtle.left(90)
        turtle.forward(300)
        turtle.left(90)
    turtle.end_fill()

# Function to draw the sun.
def draw_sun(turtle):
    """Draw a simple sun in the corner."""
    turtle.penup()
    turtle.goto(-350, 250)  # Position sun in the corner
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for _ in range(12):
        turtle.forward(40)
        turtle.right(150)
    turtle.end_fill()

# Function to draw a palm tree (vertical line).
def draw_palm_tree(turtle, x, y):
    """Draw a palm tree."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    # Draw the trunk
    turtle.color("sienna")  # Brown color
    turtle.begin_fill()
    turtle.goto(x, y - 80)
    turtle.goto(x + 20, y - 80)
    turtle.goto(x + 10, y)
    turtle.end_fill()
    
    # Draw the leaves
    turtle.color("forest green")  # Green color
    turtle.penup()
    turtle.goto(x - 10, y - 70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x + 30, y - 70)
    turtle.goto(x + 10, y + 30)
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
    
    # Draw multiple palm trees
    for i in range(5):
        draw_palm_tree(palm_tree_turtle, -350 + i * 150, -100)

if __name__ == "__main__":
    create_beach_scene()
    screen.exitonclick()
