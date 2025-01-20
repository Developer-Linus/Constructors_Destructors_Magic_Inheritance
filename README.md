# Advanced Python Classes and Objects

This page delves into the world of Python classes, equipping you with the knowledge to create robust and reusable object-oriented programs. You’ll explore core concepts like constructors, destructors, magic methods, inheritance, and composition.

# Concept Overview
Topics:
Deep Dive into Python Classes

- Constructors (__init__)
- Destructors (__del__)
- Magic Methods (e.g., __str__, __repr__)
- Class Inheritance and Composition
    - Inheritance Basics
    - Composition as an Alternative
# Learning Objectives
- Understand the fundamental principles of Python classes and object-oriented programming (OOP).
- Effectively use constructors, destructors, and magic methods to define object behavior and properties.
- Implement inheritance to create class hierarchies and extend functionalities.
- Apply composition to build complex objects from simpler ones
# Introduction
Classes are blueprints for creating objects in Python. They encapsulate data (attributes) and functionality (methods) specific to a particular type of object. OOP allows you to model real-world entities and their relationships in your code, promoting modularity, code re-usability, and maintainability.

## Detailed Explanation
Deep Dive into Python Classes
### Constructors (__init__):
The __init__ method, also known as the constructor, is a special method that automatically gets called when you create an object of a class. It’s responsible for initializing the object’s attributes (variables) with starting values.
```bash python
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Create a Point object
point = Point(3, 5)
print(f"Point coordinates: ({point.x}, {point.y})")  # Output: Point coordinates: (3, 5)
```

Let’s break down the provided code:

Class Definition (Point Class): <br>

We define a class named Point using the class keyword. Classes are like blueprints for creating objects in Python. Inside the class, we have a special method called __init__, which is a constructor method. It is automatically called when we create a new object of the class
The __init__ method takes parameters x and y along with self. self represents the instance of the class (the object itself) and is used to access variables and methods within the class.

Constructor Method (__init__): <br>

The __init__ method initializes the object with initial values for its attributes (x and y in this case).
Inside __init__, we set the attributes self.x and self.y with the values passed during object creation (Point(3, 5)).

Creating an Object (point Object): <br>

We create an object named point of the Point class by calling Point(3, 5). This invokes the __init__ method with x=3 and y=5.
The point object now has attributes x and y initialized to 3 and 5, respectively.

Accessing Object Attributes: <br>

We use dot notation (point.x and point.y) to access the attributes of the point object.
Finally, we print the coordinates of the point using print(f"Point coordinates: ({point.x}, {point.y})"), which outputs Point coordinates: (3, 5).
Destructors (__del__):
When you create an object in Python, it occupies memory to store its data and code. Objects are automatically destroyed (garbage collected) by Python when they are no longer in use or when the program exits.

## The __del__ Method:

The __del__ method is a special method in Python classes that gets called when an object is about to be destroyed (garbage collected). You can define this method in your class to perform cleanup tasks or release resources held by the object before it is destroyed.

Let’s consider an example where we want to close a file automatically when the object representing that file is no longer needed.
```bash python
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')  # Open the file for reading

    def read_data(self):
        return self.file.read()

    def __del__(self):
        self.file.close()  # Close the file when the object is destroyed

# Create an object of FileHandler
file_obj = FileHandler('sample.txt')
print(file_obj.read_data())

# Object is no longer needed, it will be garbage collected, and __del__ method will be called automatically to close the file
```

`Important Note`: Relying on destructors for critical tasks is generally not recommended in Python as garbage collection is not deterministic. Use context managers or the with statement for ensuring proper resource management.

## Magic Methods
Magic methods are special methods in Python that start and end with double underscores (also known as dunder methods). They allow you to define specific behaviors for your objects in various contexts, such as arithmetic operations, comparisons, string representations, and more. Here are some common examples:

__str__: Defines how an object is represented as a string.
__repr__: Defines the official string representation of an object.
```bash python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"Name: {self.name}, Age: {self.age}"

person = Person("Alice", 30)
print(person)  # Output: Name: Alice, Age: 30
```

## Class Inheritance and Composition:
### Inheritance

Inheritance allows you to create new classes (subclasses) that inherit properties and behaviors from existing classes (parent classes). Think of inheritance as a parent-child relationship. The child inherits characteristics and behaviors from its parent. This promotes code re-usability and facilitates the creation of class hierarchies.
```bash python
class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name)  # Call parent class constructor
    self.breed = breed

  def make_sound(self):
    print("Woof!")

dog = Dog("Buddy", "Labrador")
dog.make_sound()  # Output: Woof!
```

### Composition as an Alternative

Composition is another technique for code reuse that involves creating objects of one class within another class. This allows you to combine functionalities from different classes without directly inheriting from them.
```bash python
class Car:
  def __init__(self, engine):
    self.engine = engine  # Engine object as an attribute

  def start(self):
    self.engine.start()

class Engine:
  def start(self):
    print("Engine starting...")

car = Car(Engine())
car.start()  # Output: Engine starting...
```

##### YouTube Resources
1. https://youtu.be/Ej_02ICOIgs <br>
2. https://youtu.be/L4v9gKC7QxY 

## Practice Exercises
#### Exercise 1: Constructors and Destructors Instructions:

- Create a Person class with attributes like name and age. Implement a constructor (__init__) to initialize these attributes.
- Also, implement a destructor (__del__) method to print a farewell message when an object is deleted.
#### Exercise 2: Magic Methods (str and repr) Instructions:

- Create a Book class with attributes like title, author, and pages.
- Implement both __str__ and __repr__ magic methods to provide different string representations of the book object.
#### Exercise 3: Class Inheritance Instructions:

- Create a base class Animal with methods like eat and sleep.
- Create a subclass Dog that inherits from Animal and adds a method bark.
- Create instances of both classes and demonstrate method inheritance.

## Additional Resources
- [Python Composition Example](https://intranet.alxswe.com/rltoken/bJz5Zq4ucHJilLFWI8mp_Q)
[Inheritance and composition in Python](https://intranet.alxswe.com/rltoken/0r9sND5DWxEMBC75Dg6G1Q)