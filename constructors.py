class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

# Creating an instance of a class
point = Point(5,3)
print(f"Coordinates: ({point.x}, {point.y}).")

"""
Let’s break down the provided code:

Class Definition (Point Class):

We define a class named Point using the class keyword. Classes are like blueprints for creating objects in Python. Inside the class, we have a special method called __init__, which is a constructor method. It is automatically called when we create a new object of the class
The __init__ method takes parameters x and y along with self. self represents the instance of the class (the object itself) and is used to access variables and methods within the class.
Constructor Method (__init__):

The __init__ method initializes the object with initial values for its attributes (x and y in this case).
Inside __init__, we set the attributes self.x and self.y with the values passed during object creation (Point(3, 5)).
Creating an Object (point Object):

We create an object named point of the Point class by calling Point(3, 5). This invokes the __init__ method with x=3 and y=5.
The point object now has attributes x and y initialized to 3 and 5, respectively.
Accessing Object Attributes:

We use dot notation (point.x and point.y) to access the attributes of the point object.
Finally, we print the coordinates of the point using print(f"Point coordinates: ({point.x}, {point.y})"), which outputs Point coordinates: (3, 5).
"""
