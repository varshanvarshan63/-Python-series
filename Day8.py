# IF, elif, else / conditional statements
# Conditional statements are used to make decisions in Python.
# They execute different blocks of code depending on the condition.

# Example 1: simple if statement
x = 10
if x == 10:
    print("Yes, x is 10")



# Example 2: if/else statement
signal = "red"
if signal == "red":
    print("STOP")
else:
    print("GO")

signal = "yellow"
if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("READY")
else:
    print("GO")

# Example 3: if/elif/else statement
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")


# OR

gender = "male"
age = 22
if gender == "female":
    print("ticket is free.")
elif age < 5:
    print("ticket is free.")
elif age <= 12:
    print("you get a child discount.")
elif age >= 60:
    print("you get a senior citizen discount.")
else:
    print("you pay the full price.")

# Example 4: checking multiple conditions
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Important note:
# Use == for comparison, not =
# = is used to assign a value to a variable
