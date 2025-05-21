# Write a program that catches multiple exceptions (e.g., ValueError, IndexError).

my_list = [12, 4, 31, 3, "Hello"]

try:
    num = int(input("Enter a number: "))  # Might raise ValueError
    index = int(input("Enter an index (0-4): "))  # Might raise IndexError
    print(f"Value at index {index}: {my_list[index]}")
except ValueError:
    print("Error: Please enter a valid number.")
except IndexError:
    print("Error: Index is out of range.")
else:
    print("Success! No errors occurred.")
finally:
    print("Program execution finished.")
