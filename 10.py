# Write a class Car with a constructor to initialize model and price, and display method.

class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def display(self):
        print("Car Model:", self.model)
        print("Car Price:", self.price)

# Create an object of Car class
car1 = Car("BMW", 3000000)
car2 = Car("TOYATA", 230000)


# Call 
car1.display()
car2.display()
