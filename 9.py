class Calculator:

    # __init__ not used as we dont need to store any values when creating the object
    def square(self, number):
        return number**2
    
# Create object
calc = Calculator()


#call
num = int(input("Enter a number: "))
print("Square of", num, "is", calc.square(num))