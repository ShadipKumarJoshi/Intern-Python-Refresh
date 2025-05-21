
# Write a class Person with attributes name and age and create an object to display the data.

# Define class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dispaly(self):
        print("Name:", self.name)
        print("Age: ", self.age)

# Object of class person
person1 = Person("Anil", 20)

# call
person1.dispaly()

