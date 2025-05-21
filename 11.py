# Create a base class Animal and a subclass Dog that inherits and adds new behavior.

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound.")

# Subclass
class Dog(Animal):
    def bark(self):
        print(self.name, "says: Woof! Woof!")

# Create an object of Dog
my_dog = Dog("Buddy")

# Call methods
my_dog.speak()  # Inherited from Animal
my_dog.bark()   # Specific to Dog .
