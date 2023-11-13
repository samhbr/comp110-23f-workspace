"""CQ07!"""

from __future__ import annotations


class Point: 
    """Attributes in point class."""
    x: float | int 
    y: float | int 

    def __init__(self, x_init: float | int = 0.0, y_init: float | int = 0.0):
        """Constructor that takes inputs x and y."""
        self.x = x_init
        self.y = y_init 

    def scale_by(self, factor: int) -> None: 
        """A method that belongs to the Point class and mutates a Point."""
        self.x = self.x * factor
        self.y = self.y * factor
    
    def scale(self, factor: int) -> Point: 
        """Creates a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point 
    
    def __str__(self) -> str:  
        """Magic method to print out points in a readable way!"""
        readable: str = (f"x: {self.x}; y: {self.y}") 
        return readable 
    
    def __mul__(self, factor: int | float) -> Point: 
        """Overloads the * operator for multiplication with a factor."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, value: int | float) -> Point: 
        """Overloads the + operator for addition with a value."""
        return Point(self.x + value, self.y + value) 