# Concept of functions in Python

# A function is a reusable block of code that performs a specific task.
# Functions help organize code, avoid repetition, and make programs easier to read.

# 1. Function definition and call

def greet():
    """Print a greeting message."""
    print("Hello! Welcome to Python functions.")

# Call the function
greet()

# 2. Function with parameters

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

result = add_numbers(5, 7)
print("Sum:", result)

#3#3
def marriage(boy, girl):
    print(f"boy is {boy}")
    print(f"girl is {girl}")
    print(f"{boy} married {girl}")


# Function calls outside the definition
marriage("chandhan", "shreya")   # positional arrangement
marriage(boy="chandhan", girl="chandana") # keyword arrangement



# 4. Function with return value and multiple outputs

def min_max(numbers):
    """Return the minimum and maximum values from a list."""
    return min(numbers), max(numbers)

values = [10, 3, 8, 25, 1]
minimum, maximum = min_max(values)
print("Min:", minimum, "Max:", maximum)

# 5. Scope: local vs global variables

count = 0

def increment():
    global count
    count += 1
    return count

print("Count after increment:", increment())


#tables 
def tables(num):
    for i in range (1,11):
        print (f"{num}x{i}={num*i})")
