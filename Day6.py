# Tuples and Lists
# ----------------
# Topic: Collections in Python
# ----------------
# #tuple
# A tuple is an ordered collection.
# It is immutable, so its values cannot be changed after creation.
# Syntax: my_tuple = (item1, item2, item3)

numbers = (1, 2, 3, 4)
print("Tuple:", numbers)
print("First element:", numbers[0])

# #list
# A list is an ordered collection.
# It is mutable, so we can add, remove, or update items.
#written inside square brackets []

# Syntax: my_list = [item1, item2, item3]

names = ["Alice", "Bob", "Charlie"]
print("List before:", names)

names.append("David")
print("List after append:", names)

names[0] = "Anna"
print("List after changing item:", names)

names.append("David")      # add at end
print(names.append)
names.insert(1, "Eve")     # insert at index 1
names.remove("Bob")        # remove by value
names.pop()                # remove last item
names[0] = "Anna"          # change item
print(names)

['Anna', 'Eve', 'Charlie', 'David']

#common list methods
nums = [5, 2, 9, 1]
print(len(nums))           # length
print(nums[0])             # first item
print(nums[-1])            # last item
print(nums[1:3])           # slice
print(nums.count(2))       # count of 2
print(nums.index(9))       # index of 9
nums.sort()                # sort in ascending order
print(nums)


#2. Tuple
#A tuple is a collection of items that is:
#ordered,immutable,written inside parentheses ()

numbers = (1, 2, 3, 4)
print(numbers)#o/p(1, 2, 3, 4)

#You cannot change a tuple after it is created.
numbers = (1, 2, 3)
# numbers[0] = 10   # This will give an error

point = (10, 20)
print(point[0])            # 10
print(point[1])            # 20
print(len(point))          # 2
print(point.count(10))     # 1
print(point.index(20))     # 1

#Example
# List example
students = ["Rahul", "Priya", "Kiran"]
students.append("Asha")
print("List:", students)

# Tuple example
coordinates = (10, 20)
print("Tuple:", coordinates)

# Accessing elements
print(students[0])     # Rahul
print(coordinates[1])  # 20

#outputList: ['Rahul', 'Priya', 'Kiran', 'Asha']
#Tuple: (10, 20)
#Rahul
#20

#5. Nested examples
# list can contain a tuple, and a tuple can contain a list.

student_data = [("Rahul", 90), ("Priya", 85)]
print(student_data)

#[('Rahul', 90), ('Priya', 85)]

#6. Important syntax notes
    #Empty list
empty_list = []
empty_tuple = ()
single_item = (5,)


#7. Simple rule to remember
#Use list when the data may change.
#Use tuple when the data should remain fixed.
# Use list for changing data

days = ["Mon", "Tue"]
days.append("Wed")

# Use tuple for fixed data
weekend = ("Sat", "Sun")

#8. Short summary
#list = mutable, uses []
#tuple = immutable, uses ()
#Both are ordered
#Both support indexing and slicing



# #difference
# Tuple uses () and cannot be modified.
# List uses [] and can be modified.

# #error_example
# numbers[0] = 10
# This will raise an error because tuples are immutable.

# #extra_examples
marks = [90, 85, 80]
marks.sort()
print("Sorted marks:", marks)

point = (10, 20)
print("Tuple point:", point)
print("Point x value:", point[0])