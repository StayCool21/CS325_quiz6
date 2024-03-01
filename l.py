# You're developing a 2D geometry drawing application that uses various shapes.
# There are currently base classes for Shape and specific subclasses for Circle,
# Rectangle, and Triangle. Each subclass implements a get_area() method to calculate
# its respective area.
# Question:
# WAP to ensure compliance with the Liskov Substitution Principle (LSP). Consider the
# following challenges and Name your program l.py.:
# Circle and Rectangle have a set_width() and set_height() method, while Triangle
# doesn't. How can you handle this difference without violating LSP?
# The get_area() method implementation varies across shapes. Is this a violation of
# LSP. If so, propose solutions to maintain consistency while accommodating specific
# area calculations.
# Imagine adding a new Polygon shape with multiple sides. How would you integrate it
# into the hierarchy without compromising LSP principles?

from abc import ABC, abstractmethod
import math

class HasWidth:
    def set_width(self, width: float) -> None:
        raise NotImplementedError("This shape does not have a width")
    
class HasHeight:
    def set_height(self, height: float) -> None:
        raise NotImplementedError("This shape does not have a height")

class Shape(ABC):
    @abstractmethod
    def get_area(self) -> str:
        print("Calculated area of the shape: ...")

class Circle(HasWidth, HasHeight, Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def get_area(self) -> float:
        return math.pi * self.radius ** 2
    
    def set_width(self, width: float) -> None:
        self.radius = width/2

    def set_height(self, height: float) -> None:
        self.radius = height/2

class Rectangle(HasWidth, HasHeight, Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
    
    def get_area(self) -> float:
        return self.width * self.height
    
    def set_width(self, width: float) -> None:
        self.width = width

    def set_height(self, height: float) -> None:
        self.height = height

class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height
    
    def get_area(self) -> float:
        return 0.5 * self.base * self.height
        