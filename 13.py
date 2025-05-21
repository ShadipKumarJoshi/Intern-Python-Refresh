# Implement the str() method in a class to return a custom string representation.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student Name: {self.name}, Grade: {self.grade}"

# Create an object
s1 = Student("Aarav", "A+")

# Print the object (will call __str__ automatically)
print(s1)
