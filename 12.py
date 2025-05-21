# Write a class with private attributes and provide getter and setter methods.

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")

# Create object
p = Person("Ram", 25)

# Access private attributes using getters
print("Name:", p.get_name())
print("Age:", p.get_age())

# Modify attributes using setters
p.set_name("Shyam")
p.set_age(30)

print("Updated Name:", p.get_name())
print("Updated Age:", p.get_age())
