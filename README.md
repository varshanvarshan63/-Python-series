# Python Series

A beginner-friendly Python repository that covers the fundamentals of Python programming through simple examples and practice programs. This repository is intended for students and anyone starting their Python learning journey.

## Overview

This repository contains Python programs that demonstrate:

* Basic output using `print()`
* Variables and data types
* Arithmetic operations
* Simple expressions
* Python syntax and formatting
* Hands-on practice examples

Each program is designed to explain a specific Python concept in a simple and understandable way.

## Topics Covered

  
* Hello World Program
* Print Statements
* Variables
* Data Types

  * String
  * Integer
  * Float
  * Boolean
* Arithmetic Operators

  * Addition (`+`)
  * Subtraction (`-`)
  * Multiplication (`*`)
  * Division (`/`)
  * Modulus (`%`)
  * Floor Division (`//`)
  * Exponentiation (`**`)
* Output Formatting

## Sample Program

```python


## Learning Outcomes

After completing this repository, you will understand:

* How Python programs are written and executed
* How to create and use variables
* Different built-in data types
* Basic arithmetic operations
* How to display output using the `print()` function

## Requirements

* Python 3.x

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/varshanvarshan63/-Python-series.git
```

2. Navigate to the project directory.

```bash
cd -Python-series
```

3. Run the Python program.

```bash
python filename.py
```

Replace `filename.py` with the name of the Python file you want to execute.

## Repository Structure

```text
Python-Series/
│
├── basics.py
├── variables.py
├── operators.py


# Python Input, Output, String Formatting & Comments

## Overview

This project demonstrates the basics of Python programming, including taking user input, displaying output, converting data types, formatting strings using f-strings, calculating values, and writing comments. It is designed for beginners who are learning Python fundamentals.

---

## Features

* Accepts user input using the `input()` function.
* Displays output using the `print()` function.
* Converts string input to integers using `int()`.
* Uses formatted strings (f-strings) for clean and readable output.
* Calculates the age difference between two people.
* Demonstrates the use of the `abs()` function.
* Shows examples of single-line and multi-line comments.

---

## Concepts Covered

### User Input

* Reading input from the keyboard.
* Storing user input in variables.

### Output

* Printing values using the `print()` function.
* Displaying multiple values together.

### Type Conversion

* Converting string input into integers using `int()`.

### Formatted Strings

* Using f-strings to embed variables directly into strings.

### Mathematical Operations

* Calculating the absolute difference between two ages using `abs()`.

### Comments

* Writing single-line comments using `#`.
* Understanding multi-line comment conventions using triple quotes (`'''` or `"""`).

---

## Sample Output

```text
Age: 20
Your age is: 20

Enter your name: Varshan
Enter your age: 21

Boy's name: Rahul
Girl's name: Priya
Boy's name is: Rahul
Girl's name is: Priya

Boy's name: Rahul
Boy's age: 22
Girl's name: Priya
Girl's age: 20

Boy's name is Rahul, Boy's age is 22, and Girl's name is Priya and Girl's age is 20

Rahul loves Priya. The age difference is 2.

This is a single line comment example.
This is a multi-line comment example.
```

---

## Functions Used

| Function  | Purpose                                |
| --------- | -------------------------------------- |
| `input()` | Accepts input from the user            |
| `print()` | Displays output on the screen          |
| `int()`   | Converts a string to an integer        |
| `abs()`   | Returns the absolute value of a number |
| `f""`     | Creates formatted strings              |

---

## Learning Outcomes

After completing this program, you will understand how to:

* Take input from users.
* Display formatted output.
* Convert data types.
* Perform simple calculations.
* Use f-strings effectively.
* Write clean and well-documented Python code with comments.

---

## Requirements

* Python 3.x

---

## How to Run

1. Save the code as `Day3.py`.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the program using:

```bash
python Day3.py
```

---

## Project Structure

```text
Python-Series/
│── Day3.py
└── README.md


````markdown
# Python String Manipulation

## Overview

This project demonstrates fundamental string manipulation techniques in Python. It covers string concatenation, repetition, changing letter case, removing whitespace, replacing text, finding string length, accessing characters, string slicing, and using escape sequences. This program is ideal for beginners learning Python string operations.

---

## Features

- Concatenates two strings.
- Repeats a string multiple times.
- Converts strings to lowercase and uppercase.
- Removes leading and trailing whitespace.
- Replaces text within a string.
- Finds the length of a string.
- Accesses characters using indexing.
- Extracts substrings using slicing.
- Accesses characters using negative indexing.
- Demonstrates escape sequences such as `\n` and `\t`.

---

## Concepts Covered

### String Concatenation
- Combines multiple strings using the `+` operator.

### String Repetition
- Repeats a string multiple times using the `*` operator.

### String Methods
- `lower()` – Converts all characters to lowercase.
- `upper()` – Converts all characters to uppercase.
- `strip()` – Removes leading and trailing whitespace.
- `replace()` – Replaces a specified substring with another.
- `len()` – Returns the total number of characters in a string.

### String Indexing
- Accesses individual characters using their index position.

### String Slicing
- Extracts a portion of a string using start and end indices.

### Negative Indexing
- Accesses characters from the end of the string.

### Escape Sequences
- `\n` – Prints text on a new line.
- `\t` – Inserts a horizontal tab.

---

## Sample Output

```text
Varshan gowda

HELLO!HELLO!HELLO!

hello!
HELLO!
HELLO!
WARNING!
6

a

and

a

chandan
 is a good boy

chandan     is a good boy
```

---

# README.md

````markdown
# Python Operators

## Overview

This project demonstrates the basic operators available in Python. It is designed for beginners to understand how different types of operators work through simple examples.

The program covers arithmetic calculations, variable assignments, comparisons, logical operations, membership testing, and bitwise operations.

## Features

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Membership Operators
- Bitwise Operators
- Well-commented examples for easy learning

## Operator Types Covered

### 1. Arithmetic Operators

Used to perform mathematical calculations.

Operators:
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Modulus
- `**` Exponentiation

Example:

```python
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
```

---

### 2. Assignment Operators

Used to assign or update variable values.

Operators:

- `=`
- `+=`
- `-=`
- `*=`
- `/=`
- `%=`
- `**=`

Example:

```python
x = 5
x += 3
x -= 2
x *= 4
```

---

### 3. Comparison Operators

Compare two values and return either `True` or `False`.

Operators:

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

Example:

```python
print(a == b)
print(a != b)
print(a > b)
```

---

### 4. Logical Operators

Used to combine multiple conditions.

Operators:

- `and`
- `or`
- `not`

Example:

```python
x = 5
y = 10

print(x < 10 and y > 5)
print(x < 10 or y < 5)
print(not(x < 10 and y > 5))
```

---

### 5. Membership Operators

Check whether a value exists inside a sequence.

Operators:

- `in`
- `not in`

Example:

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("orange" not in fruits)
```

---

### 6. Bitwise Operators

Perform operations on the binary representation of integers.

Operators:

- `&` (AND)
- `|` (OR)
- `^` (XOR)
- `~` (NOT)
- `<<` (Left Shift)
- `>>` (Right Shift)

Example:

```python
a = 5
b = 3

print(a & b)
```

---
 #DAY 4
## Operator Summary

| Operator Type | Operators |
|---------------|-----------|
| Arithmetic | `+`, `-`, `*`, `/`, `%`, `**`, `//` |
| Assignment | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=` |
| Comparison | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Logical | `and`, `or`, `not` |
| Membership | `in`, `not in` |
| Identity | `is`, `is not` |
| Bitwise | `&`, `|`, `^`, `~`, `<<`, `>>` |


## Learning Outcomes

After completing this program, you will understand:

- Performing mathematical operations in Python
- Updating variable values using assignment operators
- Comparing values using comparison operators
- Combining conditions with logical operators
- Checking membership in lists and other sequences
- Performing basic binary operations using bitwise operators

## Project Structure

```
python-operators/
│
├── operators.py
└── README.md
```


## Methods Used

| Method | Description |
|---------|-------------|
| `+` | Concatenates two strings |
| `*` | Repeats a string |
| `lower()` | Converts text to lowercase |
| `upper()` | Converts text to uppercase |
| `strip()` | Removes leading and trailing whitespace |
| `replace()` | Replaces part of a string |
| `len()` | Returns the length of the string |
| `[]` | Accesses characters using indexing |
| `[start:end]` | Extracts a substring |
| `\n` | Prints text on a new line |
| `\t` | Inserts a tab space |

---

## Learning Outcomes

After completing this program, you will understand how to:

- Work with Python strings.
- Concatenate and repeat strings.
- Use common string methods.
- Access characters using indexing.
- Extract substrings using slicing.
- Use negative indexing.
- Display formatted text using escape sequences.

---

## Requirements

- Python 3.x

---

## How to Run

1. Save the program as `Day4.py`.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the following command:

```bash
python Day4.py
```

---

## Project Structure

```text
Python-Series/
│── Day3B..py
└── README.md
```


#
---

# 📘 Lists in Python

## **1. What is a List?**
A **list** is a collection of items that are:
- **Ordered** → Elements maintain their position.
- **Mutable** → You can change, add, or remove elements.
- **Allow duplicates** → Same value can appear multiple times.
- Can store **different data types** (integers, strings, booleans, even other lists).

### **Syntax**
```python
my_list = [element1, element2, element3, ...]
```

### **Examples**
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["apple", 3, True]
```

---

## **2. Accessing List Elements**
Python uses **zero-based indexing**.

### **Syntax**
```python
list_name[index]
```

### **Examples**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[2])   # cherry
```

🔹 Negative indexing:
```python
print(fruits[-1])  # cherry
print(fruits[-2])  # banana
```

---

## **3. Modifying Lists**

### **Change an element**
```python
fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'cherry']
```

### **Add elements**
- `append()` → Add to end
- `insert()` → Add at specific index
```python
fruits.append("grape")
fruits.insert(1, "kiwi")
```

### **Remove elements**
- `remove()` → Remove by value
- `pop()` → Remove by index (default last)
- `clear()` → Remove all
```python
fruits.remove("orange")
fruits.pop(0)
fruits.clear()
```

---

## **4. Slicing Lists**
Extract portions using `[start:stop:step]`.

```python
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])   # [1, 2, 3]
print(numbers[:4])    # [0, 1, 2, 3]
print(numbers[2:])    # [2, 3, 4, 5, 6]
print(numbers[::2])   # [0, 2, 4, 6]
```

---

## **5. List Functions & Methods**

### **Functions**
- `len(list)` → Length
- `sorted(list)` → Returns new sorted list
- `sum(list)` → Sum of numeric elements

### **Methods**
- `index(element)` → Position of element
- `count(element)` → Frequency
- `reverse()` → Reverse in place
- `sort()` → Sort in place

---

## **6. Nested Lists**
Lists can contain other lists (like matrices).

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])     # [1, 2, 3]
print(matrix[1][1])  # 5
```

---


---


##
## Future Topics

* User Input
* Conditional Statements
* Loops
* Functions
* Strings
* Lists
* Tuples
* Dictionaries
* Sets
* File Handling
* Exception Handling
* Object-Oriented Programming
* Modules and Packages
* Mini Projects

## Contributing

Contributions are welcome. Feel free to fork the repository, improve the code, and submit a pull request.

## License

This repository is intended for educational purposes. You are free to use, modify, and share the code for learning and practice.

## Author

**Varshan**

GitHub: [https://github.com/varshanvarshan63](https://github.com/varshanvarshan63)
