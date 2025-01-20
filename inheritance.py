class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Generic animal makes sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def make_sound(self):
        print("Woof!")

# Create object from class Dog
dog = Dog("Buddy", "Labrador")
dog.make_sound()