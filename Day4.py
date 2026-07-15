#operators

#arithmetic operators
    #operators that perform mathematical operations on numbers

from ast import compare


a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation

#assignment operators:
    #operators that assign values to variables

x = 5
x += 3  # Equivalent to x = x + 3
print(x)  # Output: 8

x -= 2  # Equivalent to x = x - 2
print(x)  # Output: 6

x *= 4  # Equivalent to x = x * 4
print(x)  # Output: 24  

x /= 6  # Equivalent to x = x / 6
print(x)  # Output: 4.0 

x %= 3  # Equivalent to x = x % 3
print(x)  # Output: 1.0

x **= 2  # Equivalent to x = x ** 2
print(x)  # Output: 1.0

x = 5
print(x)  # Output: 5


#comparison operators:
      # compare two values and return a boolean result (True or False)

a = 10
b = 5
print(a == b)  # Equal
print(a != b)  # Not equal
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal
print(a <= b)  # Less than or equal


#logical operators:
    #used to combine conditional statements
x=5
y=10

print(x < 10 and y > 5)  # True, both conditions are true
print(x < 10 or y < 5)   # True, at least one condition is true
print(not(x < 10 and y > 5))  # False, the opposite of the original result


#membership operators:
    #used to test if a sequence is presented in an object
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True, "banana" is in the list
print("orange" not in fruits)  # True, "orange" is not in the list

        #OR EXAMPLE

my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True, 3 is in the list
print(6 not in my_list)  # True, 6 is not in the list   
print(2 not in my_list) # false, 2 is in the list

#bitwise operator
# It performs operations on binary representation of integers

a = 5   #binary:100
b = 3   #binary:011

#binary AND

print( a & b ) # output 1(binary 1001)
