# class Counter:
#     instances_count = 0
    
#     def __init__(self):
#         Counter.instances_count += 1

# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b
    
#     @staticmethod
#     def multiply(a, b):
#         return a * b
    
#     @staticmethod
#     def factorial(n):
#         if n == 0:
#             return 1
#         return n * MathUtils.factorial(n - 1)

# class User:
#     total_users = 0
    
#     def __init__(self, name):
#         self.name = name
#         User.total_users += 1


# class EmptyClass(object):
#     def __str__(self):
#         return "This is an empty class"

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __eq__(self, other):
#         if not isinstance(other, Point):
#             return False
#         return self.x == other.x and self.y == other.y
    


# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
    
#     def __str__(self):
#         return f"'{self.title}' by {self.author} ({self.year})"
    
#     def __repr__(self):
#         return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
    
#     def add_grade(self, grade):
#         self.grades.append(grade)
    
#     def __str__(self):
#         avg = sum(self.grades) / len(self.grades) if self.grades else 0
#         return f"Student: {self.name}, Average grade: {avg:.2f}"
    


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
    
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
    
#     def __mul__(self, other):
#         if isinstance(other, Vector):
#             return self.x * other.x + self.y * other.y
#         return Vector(self.x * other, self.y * other)
    
#     def __str__(self):
#         return f"Vector({self.x}, {self.y})"

# class Fraction:
#     def __init__(self, numerator, denominator=1):
#         self.numerator = numerator
#         self.denominator = denominator
    
#     def __add__(self, other):
#         new_num = self.numerator * other.denominator + other.numerator * self.denominator
#         new_den = self.denominator * other.denominator
#         return Fraction(new_num, new_den)
    
#     def __sub__(self, other):
#         new_num = self.numerator * other.denominator - other.numerator * self.denominator
#         new_den = self.denominator * other.denominator
#         return Fraction(new_num, new_den)
    
#     def __mul__(self, other):
#         return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
#     def __truediv__(self, other):
#         return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
    
#     def __str__(self):
#         return f"{self.numerator}/{self.denominator}"

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def area(self):
#         return self.width * self.height
    
#     def __eq__(self, other):
#         if not isinstance(other, Rectangle):
#             return False
#         return self.area() == other.area()
    



# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return math.pi * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * math.pi * self.radius

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
    
#     def area(self):
#         return self.side ** 2
    
#     def perimeter(self):
#         return 4 * self.side

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"

# class DatabaseConnector(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
    
#     @abstractmethod
#     def disconnect(self):
#         pass

# class PostgresConnector(DatabaseConnector):
#     def connect(self):
#         return "Connected to PostgreSQL database"
    
#     def disconnect(self):
#         return "Disconnected from PostgreSQL database"