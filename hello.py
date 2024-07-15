#Question 3 print hello world.
print("Hello, Wolrd!")

#Question 4 data types.
# Integer
age = 30
print("Age:", age, "Type:", type(age))

# Float
height = 5.9
print("Height:", height, "Type:", type(height))

# String
name = "Alice"
print("Name:", name, "Type:", type(name))

# Boolean
is_student = True
print("Is Student:", is_student, "Type:", type(is_student))

# List
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits, "Type:", type(fruits))

# Tuple
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates, "Type:", type(coordinates))

# Dictionary
person = {"name": "Alice", "age": 30}
print("Person:", person, "Type:", type(person))


#Question 5 exapmle of if-statement and for loop.
#if-statement
number = 10

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

#for loop
for i in range(1, 6):
    print(i)

#Question 6 function that takes two arguments and returns their sum.
#sum fuction
def add_numbers(a, b):
    return a + b
#calling function
result = add_numbers(5, 10)
print("The sum is:", result)


#Question 7 script that creates a list of numbers and a dictionary with some key-value pairs, then demonstrates basic operations on both.
# Create a list of numbers
numbers = [10, 20, 30, 40, 50]

# Demonstrating basic operations on the list
print("Original list:", numbers)

# Append a number to the list
numbers.append(60)
print("After appending 60:", numbers)

# Remove a number from the list
numbers.remove(30)
print("After removing 30:", numbers)

# Access a number by index
print("First number in the list:", numbers[0])

# Create a dictionary with key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Demonstrating basic operations on the dictionary
print("\nOriginal dictionary:", person)

# Add a new key-value pair
person["email"] = "alice@example.com"
print("After adding email:", person)

# Update a value
person["age"] = 31
print("After updating age:", person)

# Access a value by key
print("Person's name:", person["name"])

# Remove a key-value pair
del person["city"]
print("After removing city:", person)


#Qusetion 8 exception handling
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Please provide numbers only.")
    finally:
        print("Execution of divide_numbers complete.")

# Test with valid input
divide_numbers(10, 2)

# Test with zero division
divide_numbers(10, 0)

# Test with incorrect input type
divide_numbers(10, "five")



#Question 9 import math module.
import math

# Using math functions
radius = 5
area = math.pi * radius ** 2  # Calculate area of a circle
print(f"Area of the circle with radius {radius} is: {area}")

# Using another math function
square_root = math.sqrt(16)  # Calculate square root
print(f"Square root of 16 is: {square_root}")



#Question 10 reading and writing.
# Read from a file
file_path = 'example.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file {file_path} does not exist.")

# Write to a file
file_path = 'output.txt'
lines = ["Hello, World!", "This is a test.", "Writing to a file in Python."]

with open(file_path, 'w') as file:
    for line in lines:
        file.write(line + "\n")

print(f"Data written to {file_path}.")

