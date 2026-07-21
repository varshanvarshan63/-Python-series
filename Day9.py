 #day :9
                #loops statements

#while loops


#Python while Loop – Complete Explanation with Lots of Examples
#A while loop is used to execute a block of code repeatedly as long as a condition is True.
#Instead of writing the same code multiple times, we use a loop.


#Example 1: Basic While Loop

count = 1

while count <= 5:
    print(count)#Output 1 2 3 4 5 
    count += 1


#Example 2: Print Hello 5 Times
i = 1

while i <= 5:
    print("Hello")
    i += 1



#Example 3: Print Numbers from 10 to 1
num = 10

while num >= 1:
    print(num)
    num -= 1



#Example 4: Print Even Numbers
#example:
num = 2

while num <= 20:
    print(num)
    num += 2





#break Statement
#Stops the loop immediately.

i = 1

while i <= 10:
    if i == 6:
        break

    print(i)
    i += 1

#continue Statement
#Skips the current iteration and moves to the next one.

i = 0

while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)


#else with while
#The else block executes only if the loop finishes normally (not because of break).

i = 1

while i <= 5:
    print(i)
    i += 1
else:
    print("Loop Finished")

#Loop Finished
#Example with break
i = 1

while i <= 5:
    if i == 3:
        break

    print(i)
    i += 1
else:
    print("Finished")

#Nested While Loop
#A while loop inside another while loop.

i = 1

while i <= 3:
    j = 1

    while j <= 3:
        print(i, j)
        j += 1

    i += 1
#pattern Example
row = 1

while row <= 5:
    col = 1

    while col <= row:
        print("*", end=" ")
        col += 1

    print()
    row += 1

#Real-Life Example: ATM PIN
correct_pin = "1234"
pin = ""

while pin != correct_pin:
    pin = input("Enter PIN: ")

print("Transaction Allowed")

# Real-Life Example: Countdown Timer
time = 5

while time > 0:
    print(time)
    time -= 1

print("Time's Up!")


# output:Time's Up!


#Real-Life Example: Guess the Number
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))

print("Correct!")


