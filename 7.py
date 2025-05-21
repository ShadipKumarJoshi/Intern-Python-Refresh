# Write a program that raises a custom exception if the user enters a negative number.

# Define a custom exception
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))

    # Raise the custom exception if the number is negative
    if num < 0:
        raise NegativeNumberError("Negative number is not allowed.")
    print("You entered:", num)

# Catch the custom exception
except NegativeNumberError as e:
    print("Custom Exception:", e)
    
# Catch if the input is not a number
except ValueError:
    print("Invalid input! Please enter a number.")
