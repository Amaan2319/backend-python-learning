class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __str__(self):
        return f"{self.name} ({self.age})"
    
test1 = Test("Alice", 23)
test2 = Test("Bob", 25)

print(test1 < test2)  
print(test1, test2)

class Animal:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Animal: {self.name}"
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    

goldie = Dog("Goldie", "Golden Retriever")
print(goldie)


# MRO

class A:
    def method(self):
        print("Method from class A")

class B(A):
    def method(self):
        print("Method from class B")

class C(A):
    def method(self):
        print("Method from class C")

class D(B, C):
    def method(self):
        print("Method from class D")
        super().method()  # Call the method from the next class in MRO
print(D.__mro__)  # Print the Method Resolution Order
p = D()
p.method()  # This will call the method from class D, then B, then C

# composition
class Vehicle:
    def __init__(self,engine,os):
        self.engine = engine
        self.os = os
    def get_info(self):
        return f"Vehicle with {self.engine.type} engine and {self.os.name} OS"

class Engine:
    def __init__(self, type):
        self.type = type


class OS:
    def __init__(self, name):
        self.name = name

engine = Engine("V8")
os = OS("Linux")
vehicle = Vehicle(engine, os)
print(vehicle.get_info())


from abc import ABC, abstractmethod

class parent(ABC):
    @abstractmethod
    def my_method(self):
        pass

class Child(parent):
    def my_method(self):
        print("Implementation of abstract method in Child class")

child_instance = Child()
child_instance.my_method()  # This will print the implementation message 

# dataclass 
from dataclasses import dataclass

@dataclass
class Example:
    name: str
    age: int


# task Day 3
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius

class Rectangle(Shape):
    def area(self, length, width):
        return length * width

class Triangle(Shape):
    def area(self, base, height):
        return 0.5 * base * height

circle = Circle()
rectangle = Rectangle()
triangle = Triangle()
areas = [circle.area(5),rectangle.area(4, 6),  triangle.area(3, 8) ]
# Area of circle with radius 5
  # Area of rectangle with length 4 and width 6  # Area of triangle with base 3
for area in areas:
    print(area)

