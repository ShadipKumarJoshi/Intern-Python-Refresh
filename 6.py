# Write a program that uses try-except-else-finally to handle errors during file reading.

try:
    file = open("data.txt", "r")  # Try to open the file
    content = file.read()         # Try to read the content

except FileNotFoundError:
    print("File not found.")

else:
    print("File content:")
    print(content)

finally:
    try:
        file.close()
        print("File closed.")
    except:
        print("No file to close.")
