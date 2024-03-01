# Imagine you're developing a graphics application that requires calculating the areas
# of different shapes. Currently, you have a base Shape class with an abstract
# get_area method that each concrete shape class (e.g., Circle, Square, Rectangle)
# must implement.
# Question: WAP to design this system to adhere to the Open-Closed Principle (OCP).
# This means you should be able to add new shapes without modifying existing code.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod

    def get_area(self) -> str:
        print("Calculated area of the shape: ...")

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * self.radius ** 2
    
class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def get_area(self) -> float:
        return self.radius ** 2
    
class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def get_area(self) -> float:
        return 0.5 * self.base * self.height
    
class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def get_area(self) -> float:
        return self.length * self.width
    
class add_shape:
    @staticmethod

    def add_shape(shape_type, *args):
        if shape_type == "Circle":
            return Circle(*args)
        elif shape_type == "Square":
            return Square(*args)
        elif shape_type == "Triangle":
            return Triangle(*args)
        elif shape_type == "Rectangle":
            return Rectangle(*args)
        else:
            raise ValueError("Invalid shape type")