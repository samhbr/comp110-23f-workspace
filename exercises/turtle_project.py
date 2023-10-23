"""EX05 - Beach Scene Turtle Art Project!"""

__author__ = "730563340"

from turtle import Turtle, colormode, done, Screen

# Set the color mode for RGB values 0-255
colormode(255)

def main() -> None:
    """The entrypoint of my scene."""
    turtle = Turtle()
    turtle.speed(50)
    turtle.hideturtle()
    draw_beach(turtle)
    draw_sky(turtle, -400, 400, 600)
    draw_water(turtle)
    draw_birds(turtle, -200, 0)
    draw_sun(turtle)
    done()

def draw_sky(turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draws a sky of the given width."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(135, 206, 250)  # Sky blue color
    turtle.begin_fill()
    i: int = 0
    while i < 2:
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(width)  # Adjusted the height of the sky
        turtle.right(90)
        i += 1
    turtle.end_fill()

def draw_beach(turtle: Turtle) -> None:
    """Draws the beach to fill the entire screen."""
    turtle.penup()
    turtle.goto(-400, -200)  # Coordinates to fill the screen
    turtle.pendown()
    turtle.color(255, 228, 196)  # Light sandy color
    turtle.begin_fill()
    i: int = 0
    while i < 2:
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
        i += 1
    turtle.end_fill()

def draw_water(turtle: Turtle) -> None:
    """Draws the water."""
    turtle.penup()
    turtle.goto(-400, -100)
    turtle.pendown()
    turtle.color(0, 119, 190)  # Blue color
    turtle.begin_fill()
    i: int = 0
    while i < 2:
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        i += 1
    turtle.end_fill()

def draw_birds(turtle: Turtle, x: float, y: float) -> None:
    """Draws two birds flying above the water."""
    turtle.left(90)
    turtle.fillcolor(139, 69, 19)
    i: int = 0
    while i < 2:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        draw_wings(turtle)
        turtle.left(180)
        x += 150
        i += 1
  

def draw_wings(turtle: Turtle) -> None:
    "Draws a wing of a bird."
    turtle.color("gray")
    turtle.circle(20, 180)
    # Turns turtle around for second wing
    turtle.left(180)
    turtle.circle(20, 180)
    

def draw_sun(turtle: Turtle) -> None:
    """Draw a simple sun."""
    turtle.penup()
    turtle.goto(200, -75)
    turtle.pendown()
    turtle.color(255, 255, 0)  # Yellow color
    i: int = 0
    while i < 40:
        turtle.forward(30)
        turtle.right(150)
        i += 1


if __name__ == "__main__":
    main()
